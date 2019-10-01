from flask import Flask
from redis import Redis
from logging import getLogger, INFO
from handlers import blueprint
import config


def create_app() -> Flask:
    app = Flask(__name__)

    redis = Redis(host=DB_HOST, port=DB_PORT, db=0)

    logger = getLogger('Logger')
    logger.setLevel(INFO)

    app.redis = redis
    app.logger = logger
    app.register_blueprint(blueprint)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host=APP_HOST, port=APP_PORT, debug=True)
