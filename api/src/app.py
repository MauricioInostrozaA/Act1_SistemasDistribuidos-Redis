from flask import Flask, jsonify
from inventory import inventory

app = Flask(__name__)

@app.route("/", methods=["GET"])
def ping():
    return jsonify({"response": "pong!"}) 

@app.route('/inventory')
def inventoryHandler():
    return jsonify({"inventory": inventory})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

