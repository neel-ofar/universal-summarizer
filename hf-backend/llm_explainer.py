from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("mistral-7b-instruct")
model = AutoModelForCausalLM.from_pretrained("mistral-7b-instruct")

def explain_prediction(fruit, info):
    prompt = f"""
Explain why this image was predicted as {fruit}.
Give a friendly, clear explanation based on color, shape, and common characteristics.

Also summarize:
- Nutrition
- Health Benefits
- How to tell if it's ripe
{info}
"""

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=150)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

