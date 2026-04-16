from flask import Flask, request, jsonify
from db import engine, SessionLocal
from models import Base, Task
import socket
import os

app = Flask(__name__)

# Create tables
Base.metadata.create_all(bind=engine)


def task_to_dict(task):
    return {
        "id": task.id,
        "title": task.title,
        "status": task.status
    }


@app.route("/")
def home():
    db = SessionLocal()

    try:
        tasks = db.query(Task).all()

        return jsonify({
            "service": "task-manager-api",
            "version": "1.0",
            "environment": os.getenv("ENV", "dev"),
            "total_tasks": len(tasks),
            "tasks": [task_to_dict(task) for task in tasks]
        })
    finally:
        db.close()


@app.route("/health"), methods=['GET'])
def health():
    db = SessionLocal()

    try:
        task_count = db.query(Task).count()

        return {
            "status": "healthy",
            "service:" "task-app",
            "database": "connected",
            "hostname": socket.gethostname(),
            "total_tasks": task_count
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e)
        }, 500
    finally:
        db.close()


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json

    if not data or "title" not in data:
        return {"error": "Title is required"}, 400

    db = SessionLocal()

    try:
        task = Task(
            title=data["title"],
            status=data.get("status", "pending")
        )

        db.add(task)
        db.commit()
        db.refresh(task)

        return task_to_dict(task), 201

    except Exception as e:
        db.rollback()
        return {"error": str(e)}, 500

    finally:
        db.close()


@app.route("/tasks", methods=["GET"])
def get_tasks():
    db = SessionLocal()

    try:
        status_filter = request.args.get("status")

        query = db.query(Task)

        if status_filter:
            query = query.filter(Task.status == status_filter)

        tasks = query.all()

        return jsonify([task_to_dict(task) for task in tasks])

    finally:
        db.close()


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    db = SessionLocal()

    try:
        task = db.query(Task).filter(Task.id == task_id).first()

        if not task:
            return {"error": "Task not found"}, 404

        if "title" in data:
            task.title = data["title"]

        if "status" in data:
            task.status = data["status"]

        db.commit()
        db.refresh(task)

        return task_to_dict(task)

    except Exception as e:
        db.rollback()
        return {"error": str(e)}, 500

    finally:
        db.close()


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    db = SessionLocal()

    try:
        task = db.query(Task).filter(Task.id == task_id).first()

        if not task:
            return {"error": "Task not found"}, 404

        db.delete(task)
        db.commit()

        return {"message": "Task deleted successfully"}

    finally:
        db.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
