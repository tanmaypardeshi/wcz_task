from apis import app
from flask import jsonify, request


@app.route("/", methods=['GET'])
def home():
    return jsonify({"message": "HI"})
