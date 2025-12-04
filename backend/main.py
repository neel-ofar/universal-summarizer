from fastapi import FastAPI, UploadFile
from PIL import Image
from sam_segment import segment_fruit
from dino_classifier import classify_fruit
from rag_knowledge import retrieve_info
from llm_explainer import explain_prediction

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile):

    # 1. Load Image
    img = Image.open(file.file).convert("RGB")

    # 2. Segment fruit
    segmented = segment_fruit(img)

    # 3. Classify fruit
    fruit_name = classify_fruit(segmented)

    # 4. Retrieve knowledge
    info = retrieve_info(fruit_name)

    # 5. Generate LLM explanation
    explanation = explain_prediction(fruit_name, info)

    return {
        "fruit": fruit_name,
        "info": info,
        "explanation": explanation
    }

