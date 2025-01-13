from models import db, Todo
from flask import jsonify

class TodoService:
    def get_all_todos(self):
        todos = Todo.query.all()
        return jsonify([{
            'id': todo.id,
            'task_name': todo.task_name,
            'description': todo.description,
            'assignee': todo.assignee,
            'assigned_to': todo.assigned_to,
            'created_at': todo.created_at.isoformat(),
            'completed': todo.completed
        } for todo in todos])

    def create_todo(self, data):
        new_todo = Todo(
            task_name=data['task_name'],
            description=data['description'],
            assignee=data['assignee'],
            assigned_to=data['assigned_to'],
            completed=False
        )
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({
            'id': new_todo.id,
            'task_name': new_todo.task_name,
            'description': new_todo.description,
            'assignee': new_todo.assignee,
            'assigned_to': new_todo.assigned_to,
            'created_at': new_todo.created_at.isoformat(),
            'completed': new_todo.completed
        })

    def update_todo(self, todo_id, data):
        todo = Todo.query.get_or_404(todo_id)
        todo.completed = data.get('completed', todo.completed)
        db.session.commit()
        return jsonify({
            'id': todo.id,
            'task_name': todo.task_name,
            'description': todo.description,
            'assignee': todo.assignee,
            'assigned_to': todo.assigned_to,
            'created_at': todo.created_at.isoformat(),
            'completed': todo.completed
        })