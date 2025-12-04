from transformers import SamProcessor, SamModel
from PIL import Image

processor = SamProcessor.from_pretrained("facebook/sam-vit-huge")
model = SamModel.from_pretrained("facebook/sam-vit-huge")

def segment_fruit(image: Image.Image):
    inputs = processor(image, return_tensors="pt")
    outputs = model(**inputs)
    mask = outputs.pred_masks[0][0] > 0.5
    
    # Apply mask to image
    segmented = Image.fromarray((image * mask.numpy()).astype("uint8"))
    return segmented

