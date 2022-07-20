from datetime import datetime
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask-Heroku"
    return render_template(
        "hello_there.html",
        now=datetime.now,
    )

@app.route("/api/<name>", methods=['GET'])
def api(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    content = [{
        "name": name,
        "now_format" : formatted_now,
        "now": now
        }]
    return jsonify(content)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )





if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')