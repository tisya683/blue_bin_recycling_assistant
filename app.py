import gradio as gr
from predict import predict_img

with gr.Blocks() as demo:

    gr.Markdown("# Blue Bin Recycling Assistant")

    image = gr.Image(type="pil")

    is_clean = gr.Checkbox(label="Clean?")
    is_dry = gr.Checkbox(label="Dry?")
    is_rigid = gr.Checkbox(label="Rigid?")

    output = gr.JSON()

    submit = gr.Button("Classify")

    submit.click(
        fn=predict_img,
        inputs=[image, is_clean, is_dry, is_rigid],
        outputs=output
    )

demo.launch()
