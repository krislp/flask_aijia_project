
from flask import Flask

from app.user_views import user_blueprint
from utils.functions import init_ext
from utils.settings import TEMPLATE_DIR, STATIC_DIR


def create_app(Config):

    app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')

    app.config.from_object(Config)

    app.debug = True

    init_ext(app)

    return app