from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    name = 'taro'
    return render_template('index.html', name=name)

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=true)
