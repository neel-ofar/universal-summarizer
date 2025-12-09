from fastapi import FastAPI, UploadFile, File
from PIL import Image

from sam_segment import segment_fruit
from dino_classifier import classify_fruit
from rag_knowledge import retrieve_info
from llm_explainer import explain_prediction
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"msg": "Fruit AI backend running successfully on HuggingFace!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

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

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=7860,
        reload=False
    )
