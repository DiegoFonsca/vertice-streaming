
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from sqlalchemy import URL

load_dotenv()

database = SQLAlchemy()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)

    # Configuração da aplicação
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # Configuração da conexão com PostgreSQL
    app.config["SQLALCHEMY_DATABASE_URI"] = URL.create(
        drivername="postgresql+psycopg",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "5432")),
        database=os.getenv("DB_NAME"),
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializa o banco de dados
    database.init_app(app)

    # Inicializa a proteção CSRF
    csrf.init_app(app)

    # Registra as rotas
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
