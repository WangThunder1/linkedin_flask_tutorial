# pylint: disable=import-outside-toplevel, no-name-in-module
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'randomstringgoeshereasasecretkey'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app