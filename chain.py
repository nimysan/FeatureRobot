from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

prompt_template = """
假设你是一个运维专家，需要帮助公司团队调查一些事故的根本原因和给出故障排查建议。
请回答以下问题
{message}

专家回答:
"""

llm = OpenAI(temperature=0)
llm_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(prompt_template)
)
# llm_chain("colorful socks")
