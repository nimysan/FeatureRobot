import gradio as gr
from chain import llm_chain

def echo(message, history):
    return llm_chain(message)['text']

demo = gr.ChatInterface(fn=echo, examples=["Pod退出的原因是什么？", "hola", "merhaba"], title="Jarvis智能运维")
demo.launch()