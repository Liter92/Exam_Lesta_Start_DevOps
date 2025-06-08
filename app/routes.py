from flask import request, jsonify
from app import app, db
from app.models import Result

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    if not data or "name" not in data or "score" not in data:
        return jsonify({"error": "Invalid data"}), 400

    result = Result(name=data["name"], score=data["score"])
    db.session.add(result)
    db.session.commit()

    return jsonify({"message": "Data saved"}), 201

@app.route("/results", methods=["GET"])
def get_results():
    results = Result.query.all()
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "score": r.score,
        "timestamp": r.timestamp
    } for r in results]), 200, {"Content-Type": "application/json; charset=utf-8"}
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok"})