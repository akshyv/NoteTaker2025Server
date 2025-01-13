from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from models import db
import os
from routes import todos_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Create instance directory if it doesn't exist
    instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
    os.makedirs(instance_path, exist_ok=True)

    # Configure database URI with absolute path
    db_path = os.path.join(instance_path, 'todos.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(todos_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)