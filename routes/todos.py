from flask import request, jsonify
from models import db, Todo
from services.todo_service import TodoService
from . import todos_bp

todo_service = TodoService()

@todos_bp.route('/api/todos', methods=['GET'])
def get_todos():
    return todo_service.get_all_todos()

@todos_bp.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.json
    return todo_service.create_todo(data)

@todos_bp.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    return todo_service.update_todo(todo_id, data)