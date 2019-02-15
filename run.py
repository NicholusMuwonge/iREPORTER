"""
app root of the api endpoints. this module runs the application
"""

from flask import Flask, json, jsonify
from api.views.routes import Routes
from flask_jwt_extended import JWTManager
from api.models.database import DatabaseConnection
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
app.env = 'development'
Routes.generate(app)
app.config['JWT_SECRET_KEY'] = 'nicks'
jwt = JWTManager(app)
CORS(app)
Swagger(app)


@app.before_first_request
def admin():
    data = DatabaseConnection()
    data.check_admin()


@app.route('/')
def index():
    return jsonify({'message': 'Welcome dear concerned citizen'})


if __name__ == '__main__':
    app.run(debug=True)
