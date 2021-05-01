# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getcalculation/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    A = request.args.get("A", None)

    response = {}
    print(f"got name {name}")
    # Check if user sent a name at all
    if not A:
        response["ERROR"] = "no parameter found, please send a parameter"
    # Check if the user entered a number not a name
    elif not str(name).isdigit():
        response["ERROR"] = "name must be numeric."
    # Now the user entered a valid name
    else:
        response["A"] = f"Hallo {A}"

    # Return the response in json format
    return jsonify(response)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to Temperature Calculation !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)