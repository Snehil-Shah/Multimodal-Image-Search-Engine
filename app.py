import gradio as gr
import os
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("clip-ViT-B-32")

qdrant_client = QdrantClient(
    url = os.environ['QDRANT_URL'],
    port= 443,
    api_key = os.environ['QDRANT_API_KEY']
)

def search_images(modality, count, input_text, input_image):
    query = str(input_text) if modality=='Text' else input_image

    results = qdrant_client.search(
    collection_name = "images",
    query_vector = model.encode(query).tolist(),
    with_payload = True,
    limit = count
    )

    return [gr.update(value="## Results\nThe image data is limited, don't expect to find everything!")]+[gr.Image(value=result.payload['url'], visible=True) for result in results]+[gr.Image(visible=False)]*(100-count)

def clear():
    return [gr.update(value="")]+[gr.Image(visible=False)]*100

def input_interface(choice):
    if choice == "Text":
        return [gr.update(visible=True), gr.update(visible=False)]
    else:
        return [gr.update(visible=False), gr.update(visible=True)]

with gr.Blocks() as interface:
    gr.Markdown("# Multi-Modal Image Search Engine\nSemantically search over 15k images using text or image inputs!")

    # Input Interface
    with gr.Column(variant='compact'):
        input_type = gr.Radio(choices=["Text", "Image"], type="value", label="Modality", value="Text")
        with gr.Column() as text_area:
            text_input = gr.Textbox(label="Text", lines=1, placeholder="Try 'Golden Retriever'")
        with gr.Column(visible=False) as image_uploader:
            image_input = gr.Image(type="pil")
    input_type.change(input_interface, input_type, [text_area, image_uploader])

    # Search Controls
    with gr.Column(variant="panel"):
        count = gr.Slider(minimum=1, maximum=40, step=1, value=8, label="No. of Results")
        images_btn = gr.Button(value="Search Images", variant="primary")

    # Output Interface
    images = []
    images.append(gr.Markdown())
    with gr.Column() as output_images:
        for i in range(10):
            with gr.Row():
                for j in range(4):
                    images.append(gr.Image(visible=False))
    images_btn.click(clear, outputs=images).then(search_images, inputs=[input_type, count, text_input, image_input], outputs=images)

    interface.launch()
