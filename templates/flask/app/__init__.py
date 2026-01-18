from flask import Flask
from .extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../.env.example', silent=True)
    app.config.from_object('app.config.Config')
    db.init_app(app)

    @app.route('/hello')
    def hello():
        return {'message': 'Hello, World!'}

    return app
