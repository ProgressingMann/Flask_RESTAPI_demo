from flask import Flask
from flask_smorest import Api

# from app.settings import Config
# from app import api as api_resources
from settings import Config
import api as api_resources


def create_app(config=Config):
    app = Flask(config.APP_NAME)
    app.config.from_object(config)

    api = Api(
        app,
        spec_kwargs={
            "title": Config.APP_NAME,
            "version": Config.VERSION,
        },
    )

    api_resources.init_app(api)

    return app
