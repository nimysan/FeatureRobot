# 1. 首先，引入必要的库, 并创建一个llm实例作为底座
from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import initialize_agent
from agents.tool_eksctl import eksctl_tool, kubectl_tool, shell_tool

from langchain import OpenAI

llm = OpenAI(temperature=0)

# 接下来制作第二个工具，制作一个LLMChain来专门进行翻译
# prompt = PromptTemplate(
#     input_variables=["input"],
#     template="""
#      你需要根据以下信息回复用户关于商品价格的查询，如果你无法从以下信息中解答用户问题，请说我不知道。
#      商品信息列表如下：
#       可口可乐5元1瓶
#       百事可乐3元1瓶
#
#      这是用户输入的问题：
#     {input}"""
# )

#  接下来，我们定义tool kit,即将所有工具存进一个数组中
# tools = [math_tool, search_tool, eksctl_tool]
tools = [eksctl_tool, kubectl_tool, shell_tool]

# 7. 初始化zero-shot agent

zero_shot_agent = initialize_agent(
    agent="zero-shot-react-description",
    tools=tools,
    llm=llm,
    verbose=True,
)

# 8.来试运行一下吧1
# zero_shot_agent("可口可乐的价格减去百事可乐的价格得到的结果的三次方是多少？")
