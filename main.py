import gradio as gr
from agent import Translator
import pyperclip
import os
from dotenv import load_dotenv


load_dotenv()
os.environ["NO_PROXY"] = "127.0.0.1"

agent_types = ["通用翻译", "学术翻译"]
agent = Translator()

target_languages = ["English", "中文"]

if __name__ == "__main__":
    with gr.Blocks(theme=gr.themes.Soft(text_size='lg'), title="LLM Translator", fill_height=True) as demo:
        with gr.Row():
            input_text = gr.Textbox(label="输入", lines=10, scale=1)
            output_text = gr.Textbox(label="结果", lines=10, scale=1)
        with gr.Row():
            infer_button = gr.Button("翻译", variant="primary")
            clear_button = gr.Button("清除", variant="secondary")
            paste_button = gr.Button("粘贴", variant="secondary")
            copy_button = gr.Button("复制", variant="secondary")
        with gr.Row():
            with gr.Column():
                model_text = gr.Textbox(label="模型", lines=1, value=os.getenv("OPENAI_MODEL"))
                temperature_slider = gr.Slider(label="温度", minimum=0, maximum=1.3, value=1.3, step=0.1)
            with gr.Column():
                agent_type_dropdown = gr.Dropdown(label="选择Agent类型",choices=agent_types, value=agent_types[0])
                target_language_dropdown = gr.Dropdown(label="目标语言", choices=target_languages, value=target_languages[0])
        
        def stream_output(text, model, temperature, target_language, agent_type):
            for output in agent.infer(text, model, temperature, target_language, agent_type):
                yield output
        
        infer_button.click(
            fn=stream_output,
            inputs=[input_text, model_text, temperature_slider, target_language_dropdown, agent_type_dropdown],
            outputs=output_text
        )
        copy_button.click(fn=lambda x: pyperclip.copy(x), inputs=output_text, outputs=None)
        paste_button.click(fn=lambda: pyperclip.paste(), inputs=None, outputs=input_text)
        clear_button.click(fn=lambda: "", inputs=None, outputs=input_text)

    # 运行
    if os.getenv("APP_PORT") is not None:
        demo.launch(server_port=int(os.getenv("APP_PORT")))
    else:
        demo.launch()
