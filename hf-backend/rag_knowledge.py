import json

# Load your fruit knowledge base
with open("knowledge_base/fruits.json", "r") as f:
    FRUIT_KB = json.load(f)

def retrieve_info(fruit_name: str):
    return FRUIT_KB.get(fruit_name.lower(), {})

