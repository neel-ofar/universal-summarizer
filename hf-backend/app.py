import gradio as gr
from PIL import Image

from sam_segment import segment_fruit
from dino_classifier import classify_fruit
from rag_knowledge import retrieve_info
from llm_explainer import explain_prediction


def process(image):
    # 1. Segment fruit
    segmented = segment_fruit(image)

    # 2. Classify fruit
    fruit_name = classify_fruit(segmented)

    # 3. Retrieve extra info
    info = retrieve_info(fruit_name)

    # 4. LLM explanation
    explanation = explain_prediction(fruit_name, info)

    return fruit_name, info, explanation


demo = gr.Interface(
    fn=process,
    inputs=gr.Image(type="pil"),
    outputs=[
        gr.Text(label="Fruit"),
        gr.Text(label="Information"),
        gr.Text(label="Explanation")
    ],
    title="Fruit AI Backend",
    description="Upload an image of a fruit to classify & get explanation."
)

demo.launch()
