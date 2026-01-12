import re
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import (CharacterTextSplitter, RecursiveCharacterTextSplitter)
import chromadb
from langchain_chroma import Chroma
from chromadb.utils.embedding_functions.ollama_embedding_function import OllamaEmbeddingFunction
from langchain_ollama import OllamaEmbeddings

file_path = '/opt/apps/data/docs/射雕英雄传.txt'

# 配置ChromaDB客户端
chroma_client = chromadb.PersistentClient(path="/opt/apps/data/chromadb")


# 预处理文本内容
def preprocess_text(text: str) -> str:
    # 合并连续空行
    text = re.sub(r'\n+', '\n', text)
    # 去除首尾空格
    return text.strip()


def store_one():
    '''
    基于原生的chromadb调用
    '''
    with open(file_path) as f:
        file_content = f.read()
    
    clean_content = preprocess_text(file_content)
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 800,
        chunk_overlap  = 10,
        length_function = len
    )
    documents = text_splitter.split_text(clean_content)
    #documents = text_splitter.create_documents([clean_content])
    print(len(documents))
    #print(documents[0])
    #print(documents[1])

    # 初始化向量嵌入模型（使用本地部署的模型）
    ollama_ef = OllamaEmbeddingFunction(
        url="http://localhost:11434/api/embeddings",
        model_name="bge-m3",
        timeout=600
    )

    # 创建或获取集合
    collection = chroma_client.get_or_create_collection(
        name="xiaoshuo",
        #metadata=[{"title": "射雕英雄传"}, {"author": "金庸"}],
        embedding_function=ollama_ef,
    )
    
    size = len(documents)
    offset = 10000000
    ids = []
    for i in range(offset, offset + size):
        ids.append(f"shediaoyingxiongzhuan_{i}")
        
    #print(docs)
    #print(ids)
    
    #collection.add(documents=documents, ids=ids)
    collection.upsert(documents=documents, ids=ids)
    print("---")
    results = collection.query(
        query_texts=["郭靖跟谁学的降龙十八掌？"],
        n_results=2
        )
    
    for result in results['documents']:
        print(result)


def store_two():
    '''
    基于langchain调用chromadb
    '''
    raw_documents = TextLoader(file_path).load()
    #print(type(raw_documents[0]))
    
    splitter = RecursiveCharacterTextSplitter(
                    chunk_size=800, 
                    chunk_overlap=10,
                    length_function=len,
                    add_start_index = True,
                    separators=["\n\n", "\n", " ",
                        "\u200b",  # Zero-width space
                        "\uff0c",  # Fullwidth comma
                        "\u3001",  # Ideographic comma
                        "\uff0e",  # Fullwidth full stop
                        "\u3002",  # Ideographic full stop
                        ""]
                    )
    
    documents = splitter.create_documents([raw_documents[0].page_content])
    print(len(documents))
    #print(documents[0])
    #print(documents[1])
    size = len(documents)
    offset = 10000000
    ids = []
    for i in range(offset, offset + size):
        ids.append(f"shediaoyingxiongzhuan_{i}")
    
    ollama_embed = OllamaEmbeddings(
        model="bge-m3",
        base_url = 'http://localhost:11434'
        # other params...
    )
    
    vector_store = Chroma(
        collection_name="test",
        embedding_function=ollama_embed,
        persist_directory="/opt/apps/data/chromadb",
    )
    vector_store.add_documents(documents=documents, ids=ids)
    #vector_store.update_documents(documents=documents, ids=ids)
    results = vector_store.similarity_search(
        "谁教郭靖学的降龙十八掌？",
        k=2,
    )
    for res in results:
        print(f"* {res.page_content} [{res.metadata}]")
        

chroma_client.delete_collection('test')
store_two()