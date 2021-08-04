from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/', methods=['POST'])
def form():
    return print(request.data)

if __name__ == "__main__":
    app.run()
