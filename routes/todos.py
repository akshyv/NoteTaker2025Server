from flask import Blueprint, request, jsonify
from utils.db_helper import add_todo, get_todos, init_db

todos_bp = Blueprint('todos', __name__)

@todos_bp.route('/todos', methods=['GET'])
def get_all_todos():
    todos = get_todos()
    return jsonify([todo.to_dict() for todo in todos])

@todos_bp.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    task = data.get('task')
    if not task:
        return jsonify({'error': 'Task is required'}), 400

    todo = add_todo(task)
    return jsonify(todo.to_dict()), 201