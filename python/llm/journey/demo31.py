import gradio as gr

def print_text(text):
    return "Hello World, " + text

interface = gr.Interface(fn=print_text, inputs="text", outputs="text")
interface.launch(share=True, server_port=7860)