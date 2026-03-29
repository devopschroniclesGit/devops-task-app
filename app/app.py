from flask import Flask, request, jsonify
from db import engine, SessionLocal
from models import Base, Task

app = Flask(__name__)

# Create tables
Base.metadata.create_all(bind=engine)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json

    if not data or "title" not in data:
        return {"error": "Title is required"}, 400

    db = SessionLocal()

    try:
        task = Task(title=data["title"])
        db.add(task)
        db.commit()
        db.refresh(task)

        return {"id": task.id, "title": task.title, "status": task.status}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}, 500

    finally:
        db.close()

@app.route("/tasks", methods=["GET"])
def get_tasks():
    db = SessionLocal()

    try:
        tasks = db.query(Task).all()

        return jsonify([
            {"id": t.id, "title": t.title, "status": t.status}
            for t in tasks
        ])

    finally:
        db.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
