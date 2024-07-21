import gradio as gr
from ngram_text_gen import (
    generate_output as ngram_text_gen,
    NGRAM_TEXT_GEN_EXAMPLES,
)

ngram_generate = gr.Interface(
    fn=ngram_text_gen,
    inputs=[
        gr.Slider(minimum=2, maximum=4, value=2, step=1, label="N-gram"),
        gr.Textbox(label="Input text"),
        gr.Number(label="Token length", value=10),
    ],
    outputs=[
        gr.Textbox(label="Generated text"),
        gr.HTML(label="Other possible outputs"),
    ],
    examples=NGRAM_TEXT_GEN_EXAMPLES,
    title="N-gram Text Generator",
    description="Generate text using N-grams.",
    allow_flagging="never",
)

with gr.Blocks() as demo:
    ngram_generate.render()

demo.launch()
