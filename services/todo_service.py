from models.todo import Todo

class TodoService:
    def __init__(self):
        self.todos = []
        self.counter = 1

    def get_all_todos(self):
        return [todo.to_dict() for todo in self.todos]

    def add_todo(self, task):
        todo = Todo(self.counter, task)
        self.todos.append(todo)
        self.counter += 1
        return todo.to_dict()

    def toggle_todo(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                todo.completed = not todo.completed
                return todo.to_dict()
        return None