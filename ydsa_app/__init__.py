# ydsa_app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY="change-me",
        SQLALCHEMY_DATABASE_URI="sqlite:///site.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # If you have these modules, keep the relative imports:
    try:
        from .extensions import db, migrate
        db.init_app(app)
        migrate.init_app(app, db)
        from . import models
    except Exception:
        pass

    try:
        from .routes import bp
        app.register_blueprint(bp)
    except Exception:
        @app.get("/")
        def home():
            return "OK"

    return app
