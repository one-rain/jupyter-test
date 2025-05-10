import os
from langchain_community.llms import Tongyi
from langchain_core.prompts import PromptTemplate

DASHSCOPE_API_KEY = os.environ.get("DASHSCOPE_API_KEY")
print(DASHSCOPE_API_KEY)
llm = Tongyi(
    model="qwq-plus",
    api_key = DASHSCOPE_API_KEY,
)

def test1():
    '''
    简单的对话
    '''
    input_text = "用50个字左右阐述，生命的意义在于"
    response = llm.invoke(input_text)
    print(response)


def test2():
    '''
    '''
    template = """Question: {question} 
        Answer: Let's think step by step.
        """
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"
    response = chain.invoke({"question": question})
    print(response)


test1()