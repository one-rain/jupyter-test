from itertools import chain
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_community.embeddings import DashScopeEmbeddings

model = 'qwen3'
# base_url='https://dashscope.aliyuncs.com/compatible-mode/v1'
# api_key = os.getenv("DASHSCOPE_API_KEY")
# model = 'qwen-plus'

def test_local1():
    llm = ChatOpenAI(
        api_key = 'ollama',
        base_url = 'http://localhost:11434/v1',
        model = model
        # other params...
    )
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"}]
    response = llm.invoke(messages)
    print(response)


def test_local2():
    '''
    template
    '''
    llm = OllamaLLM(
        base_url = 'http://localhost:11434', 
        model = model)
    
    template = """Question: {question}
        Answer: Let's think step by step."""

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm
    response = chain.invoke({"question": "你是谁？"})
    print(response)


def test_local3():
    '''
    Embedding
    '''
    embeddings = DashScopeEmbeddings(
        model="text-embedding-v2",
        # other params...
    )

    text = "This is a test document."

    query_result = embeddings.embed_query(text)
    print("文本向量长度：", len(query_result), sep='')

    doc_results = embeddings.embed_documents(
        [
            "Hi there!",
            "Oh, hello!",
            "What's your name?",
            "My friends call me World",
            "Hello World!"
        ])
    print("文本向量数量：", len(doc_results), "，文本向量长度：", len(doc_results[0]), sep='')


def test_loca4():
    ''''
    stream
    '''
    

test_local3()