from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello, World!<h1>\n<h2>вот какой-то текст для проверки после добавления devcontainer<h2>"

if __name__ == '__main__':
   app.run(host='0.0.0.0')