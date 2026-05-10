from transformers import pipeline

pipe = pipeline("text-generation", model="ceilf6/frontagent-planner-7B-lora")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)