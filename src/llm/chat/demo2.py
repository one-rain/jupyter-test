import uuid

from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
    trim_messages,
)
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_core.tools import tool

class Table(BaseModel):
    """List tables name in SQL database."""
    name: List[str] = Field(description="List of tables name in SQL database.")

from typing import List

def get_tables(table):
    print('get_tables', type(table), table)
    tables_results = []
    response_text = ""
    for table_name in table.name:
        tables_results.append(table_name)
        response_text += f"Table: {table_name} "
        response_text += f" Columns:{', '.join(schema[table_name]['columns'])}"

    return response_text

@tool
def extract_list_tables_relavance(query: str):
    """ Return the names of ALL the SQL tables that MIGHT be relevant to the user question. """
    print("call tool:extract_list_tables_relavance", query)
    system = f"""
        Return the names of ALL the SQL tables that MIGHT be relevant to the user question. \
        The tables are:
        {table_name_list}
        Remember to include ALL POTENTIALLY RELEVANT tables, even if you're not sure that they're needed.
        Output:
        "table_name1", "table_name2"
        """

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system),
            ("human", "{input}"),
        ]
    )

    prompt = prompt | model.with_structured_output(Table)

    prompt_value = prompt.invoke({"input": query})
    response_text = get_tables(prompt_value)
    print("prompt_value", response_text)
    return response_text



https://blog.gopenai.com/automating-sql-query-generation-with-langchain-and-openai-512aa26afd34


https://zhuanlan.zhihu.com/p/27979994852
