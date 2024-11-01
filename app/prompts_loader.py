import os

# 定义一个工具函数，用于加载不同的 prompt
def load_prompt(prompt_name: str) -> str:
    prompt_path = os.path.join("prompts", prompt_name)
    
    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"Prompt file '{prompt_name}' not found in prompts directory.")
    
    with open(prompt_path, "r", encoding="utf-8") as file:
        prompt_content = file.read()
    
    return prompt_content
