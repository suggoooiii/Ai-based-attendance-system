# app/views.py
from flask import request, jsonify

def configure_routes(app):
    print(app)

    @app.route('/')
    def home():
        return "<h1>Welcome to the AI Attendance<h1/>"

    @app.route('/register', methods=['POST'])
    def register_user():
        data = request.get_json()
        print("data",data)
        return jsonify({"message": "User registered successfully", "data": data}), 201

    @app.route('/attendance', methods=['POST'])
    def mark_attendance():
        data = request.get_json()
        return jsonify({"message": "Attendance marked", "user": data['user']}), 200
