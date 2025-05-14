import os
import getpass
from serpapi import GoogleSearch
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain_ollama.llms import OllamaLLM
from langchain.agents import AgentType

if not os.environ.get("SERPAPI_API_KEY"):
    os.environ["SERPAPI_API_KEY"] = getpass.getpass("Enter API key for serpapi: ")

llm = OllamaLLM(
        base_url = 'http://localhost:11434', 
        model = 'qwen3'
        )

# tools = load_tools(["serpapi"])

# 如果搜索完想再计算一下可以这么写
tools = load_tools(['serpapi', 'llm-math'], llm=llm, serpapi_api_key='your key')

# 如果搜索完想再让他再用python的print做点简单的计算，可以这样写
# tools=load_tools(["serpapi","python_repl"])

# 工具加载后都需要初始化，verbose 参数为 True，会打印全部的执行详情
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 运行 agent
agent.run("历史的今天发生过什么重点事情？")