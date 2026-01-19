from flask import Flask

from .extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    # Import and register controllers
    from .interfaces.hello_controller import hello_bp
    app.register_blueprint(hello_bp)

    return app