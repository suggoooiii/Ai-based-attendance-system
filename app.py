from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configuring MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"

mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)
