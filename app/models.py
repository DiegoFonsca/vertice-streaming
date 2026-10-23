
from app import database


class Usuario(database.Model):
    __tablename__ = "usuarios"

    id = database.Column(
        database.Integer,
        primary_key=True
    )

    nome = database.Column(
        database.String(100),
        nullable=False
    )

    email = database.Column(
        database.String(150),
        unique=True,
        nullable=False
    )

    senha = database.Column(
        database.String(255),
        nullable=False
    )

    def __repr__(self):
        return f"<Usuario {self.email}>"


class Favorito(database.Model):
    __tablename__ = "favoritos"

    id = database.Column(
        database.Integer,
        primary_key=True
    )

    usuario_id = database.Column(
        database.Integer,
        database.ForeignKey("usuarios.id"),
        nullable=False
    )

    filme_id = database.Column(
        database.String(100),
        nullable=False
    )

    __table_args__ = (
        database.UniqueConstraint(
            "usuario_id",
            "filme_id",
            name="uq_usuario_filme"
        ),
    )

    def __repr__(self):
        return f"<Favorito usuario={self.usuario_id} filme={self.filme_id}>"
