import gradio as gr
from chain import zero_shot_agent


def echo(message, history):
    """
     {'input': '可口可乐的价格？', 'output': '可口可乐5元1瓶。'}
    :param message:
    :param history:
    :return:
    """
    return zero_shot_agent(message)['output']


demo = gr.ChatInterface(fn=echo,
                        examples=["集群有几个node？", "美西2区域EKS集群eks-workshop有几个节点组？",
                                  "merhaba"], title="Jarvis智能运维")
demo.launch()
