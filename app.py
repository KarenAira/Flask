from flask import Flask, make_response, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

person_list = [
    {
        "name": "Frank",
        "age":0,
        "title": ["job", "position"]
    },
    {
        "name": "Frank",
        "age":0,
        "title": ["job", "position"]
    }
]

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/person",methods=["GET"])
def get_person():
    return jsonify({"person_list": person_list})

@app.route("/person",methods=["POST"])
def create_person():
    new_person = request.get_json()

    return jsonify()


if __name__ == "__main__":
    app.run(debug=True)
