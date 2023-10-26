import openai
import os
openai.api_key = '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'

# response = openai.Completion.create(
#     engine="gpt-3.5-turbo-16k",  # 更新引擎版本
#     prompt="Translate the following English text to French: 'Hello, World!'",
#     max_tokens=60
# )


# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
while True:
    user_input = input("请输入你的问题（输入'q'退出）：")
    if user_input.lower() == 'q':
        break
    chat_completion = openai.ChatCompletion.create(model="text-davinci-003", messages=[{"role": "user", "content": user_input}])
    gpt_reply = chat_completion['choices'][0]['message']['content']
    print(f"GPT回答：{gpt_reply}\n")  # 输出 "Hello! How can I assist you today?"
    # 使用 text-davinci-003 模型进行补全

