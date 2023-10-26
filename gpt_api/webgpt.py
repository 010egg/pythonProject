from flask import Flask, request, render_template_string
import openai
openai.api_key = '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'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('<form action="/chat" method="post"><input type="text" name="user_input"><input type="submit" value="发送"></form>')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    messages = [{"role": "user", "content": user_input}]
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    gpt_reply = chat_completion['choices'][0]['message']['content']
    return f'<p>{gpt_reply}</p><a href="/">返回</a>'

if __name__ == "__main__":
    engines = openai.Engine.list()
    for engine in engines["data"]:
        print(engine["id"])
    app.run(host='0.0.0.0', port=5000)
    # 获取并列出所有可用的引擎

# export FLASK_APP=webgpt.py
# nohup flask run --host=0.0.0.0 &

# 后台运行
# nohup flask run --host=0.0.0.0 --port=5000 &
# ssh -i ~/.ssh/id_rsa root@121.199.55.133

# python webgpt.py
# scp gpt_api/test.py root@121.199.55.133:/root/
