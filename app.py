from flask import Flask
from flask_cors import CORS
from routes.todos import todos_bp
from utils.db_helper import init_db
import os
import sys


# Add the server directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# SQLite database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(todos_bp, url_prefix='/api')

# Initialize the database
init_db()

if __name__ == '__main__':
    app.run(debug=True)