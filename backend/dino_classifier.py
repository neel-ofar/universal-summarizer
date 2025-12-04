from transformers import AutoModel, AutoProcessor
import torch
from PIL import Image

model_id = "facebook/dinov2-base"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModel.from_pretrained(model_id)

# List of fruits we want to support
FRUITS = [
    "apple", "banana", "orange", "grape", "pineapple",
    "mango", "papaya", "watermelon", "pear", "kiwi",
    "pomegranate", "guava", "dragon fruit", "strawberry"
]

def classify_fruit(image: Image.Image):

    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    
    vector = outputs.last_hidden_state.mean(dim=1)

    # Compute similarity to text prompts
    text_inputs = processor(text=FRUITS, return_tensors="pt", padding=True)
    with torch.no_grad():
        text_embeddings = model.get_text_features(**text_inputs)
        image_embedding = model.get_image_features(pixel_values=inputs.pixel_values)

    similarities = torch.matmul(image_embedding, text_embeddings.T)
    idx = torch.argmax(similarities).item()

    return FRUITS[idx]

