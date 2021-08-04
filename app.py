from flask import Flask,request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST'])
@cross_origin()
def form():
    print(request.data)
    return 0


if __name__ == "__main__":
    app.run()
