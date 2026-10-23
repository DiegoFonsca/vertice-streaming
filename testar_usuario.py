
from sqlalchemy import select
from werkzeug.security import check_password_hash

from run import app
from app import database
from app.models import Usuario


with app.app_context():
    email = "teste@vertice.local"
    senha_digitada = "SenhaTeste123!"

    consulta = select(Usuario).where(
        Usuario.email == email
    )

    usuario = database.session.execute(
        consulta
    ).scalar_one_or_none()

    if usuario is None:
        print("Usuário não encontrado.")

    elif check_password_hash(
        usuario.senha,
        senha_digitada
    ):
        print("Senha correta! Login autorizado.")

    else:
        print("Senha incorreta! Acesso negado.")
