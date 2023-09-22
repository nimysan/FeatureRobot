import subprocess

from langchain.tools import Tool


def shell_function(input):
    # subprocess.call(input.split(" "), shell=False)
    try:
        output = subprocess.check_output(input.split(" "))
        return output.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(f"{e}")
    # return "3"


# 执行eksctl命令的工具
eksctl_tool = Tool(
    name='执行eksctl工具',
    func=shell_function,
    description='用于执行eksctl命令'
)

# 执行eksctl命令的工具
kubectl_tool = Tool(
    name='执行kubectl工具',
    func=shell_function,
    description='执行kubectl指令'
)

# common shell指令
shell_tool = Tool(
    name='执行shell命令行',
    func=shell_function,
    description='执行通用shell命令'
)
