from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config.from_object('config')

    # Blueprints
    from .routes import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
