import os
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict
from chromadb.utils.embedding_functions.ollama_embedding_function import OllamaEmbeddingFunction
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings


#file_path = '/opt/apps/data/docs/射雕英雄传.txt'
file_path = '/opt/apps/data/docs/demo.txt'

api_key = os.getenv("DASHSCOPE_API_KEY")

llm = ChatOpenAI(
        api_key = api_key,
        base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1',
        model = 'qwq-plus-latest'
        # other params...
    )


# Define state for application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


# Define application steps
def retrieve(state: State, vector_store: Chroma):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}


def generate(state: State):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", ""),
            ("human", "{input}"),
        ]
    )
    
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}


def demo1():
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
    
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}

    graph_builder = StateGraph(State).add_sequence([retrieve, generate])
    graph_builder.add_edge(START, "retrieve")
    graph = graph_builder.compile()

    response = graph.invoke({"question": "谁教郭靖学的降龙十八掌？"})
    print(response["answer"])


def test():
    messages = [
        {"role": "system", "content": "你是一位翻译助手，能做中英文互译，翻译用户句子。"}, 
        {"role": "user", "content": "请翻译下面语句：我想成为一位超人！"}]

    stream = llm.stream(messages)
    full = next(stream)
    for chunk in stream:
        full += chunk
    print(full)


test()
