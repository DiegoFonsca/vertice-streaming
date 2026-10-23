
from sqlalchemy import text

from run import app
from app import database

with app.app_context():
    try:
        resultado = database.session.execute(
            text("SELECT version()")
        )

        versao = resultado.scalar()

        print("Conexão com PostgreSQL realizada com sucesso!")
        print(versao)

    except Exception as erro:
        print("Não foi possível conectar ao PostgreSQL.")
        print(type(erro).__name__)
        print(erro)
