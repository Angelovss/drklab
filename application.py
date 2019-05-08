from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "DANI MALKA MI6KOOOO!"