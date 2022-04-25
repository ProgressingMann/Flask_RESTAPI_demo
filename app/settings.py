import os


class Config:
    APP_NAME = "Skills API"
    VERSION = "1"

    # Open API
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_URL_PREFIX = "/doc"
    OPENAPI_SWAGGER_UI_PATH = "/swagger"
    OPENAPI_SWAGGER_UI_URL = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.47.1/"

    FLASK_ENV = "development"


class TestConfig(Config):
    TESTING = True
