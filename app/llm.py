from openai import OpenAI
import os
from prompts_loader import load_prompt

# 初始化 DeepSeek 客户端
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

def call_llm_with_prompt(prompt: str, user_input: str) -> str:
    """
    调用 LLM，并将用户输入动态插入到 Prompt 中，生成任务或响应。
    
    :param prompt: 要使用的 Prompt 模板
    :param user_input: 用户输入的文本
    :return: LLM 的响应结果
    """
    # 将用户输入插入到 Prompt 中
    final_prompt = prompt.format(user_input=user_input)
    
    try:
        # 调用 DeepSeek API
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": final_prompt},
            ],
            stream=False
        )
    except Exception as e:  # 捕获所有异常
        return f"Error occurred: {str(e)}"  # 返回错误信息
    
    return response.choices[0].message.content
