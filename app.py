from flask import Flask,render_template
from flask_restful import Api, Resource

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("index.html")
@app.route("/<name>")
def user(name):
    return f"Hello {name}"
if __name__ == "__main__":
    app.run()