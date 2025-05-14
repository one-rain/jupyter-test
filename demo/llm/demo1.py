from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy

query = 'apples'
passages = [
        'I like apples', 
        'I like oranges', 
        'Apples and oranges are fruits'
    ]
  
# init embedding model
model_name = 'maidalun1020/bce-embedding-base_v1'
model_kwargs = {'device': 'cuda'}
encode_kwargs = {'batch_size': 64, 'normalize_embeddings': True, 'show_progress_bar': False}

embed_model = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
  )

# example #1. extract embeddings
query_embedding = embed_model.embed_query(query)
passages_embeddings = embed_model.embed_documents(passages)

# example #2. langchain retriever example
faiss_vectorstore = FAISS.from_texts(passages, embed_model, distance_strategy=DistanceStrategy.MAX_INNER_PRODUCT)

retriever = faiss_vectorstore.as_retriever(search_type="similarity", search_kwargs={"score_threshold": 0.5, "k": 3})

related_passages = retriever.get_relevant_documents(query)

print(related_passages)