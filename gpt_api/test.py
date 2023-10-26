from flask import Flask, render_template_string, request

app = Flask(__name__)

html_page = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>美丽的Flask程序</title>
</head>
<body>
    <h1>欢迎来到美丽的Flask程序！</h1>
    <form method="post">
        <label for="name">请输入你的名字：</label>
        <input type="text" id="name" name="name" required>
        <input type="submit" value="提交">
    </form>
    {% if name %}
    <h2>你好, {{ name }}! 欢迎你！</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    name = ''
    if request.method == 'POST':
        name = request.form['name']
    return render_template_string(html_page, name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
