
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from sqlalchemy import select

from app import database
from app.models import Usuario, Favorito


main_bp = Blueprint("main", __name__)


# Identificadores dos filmes do catálogo
FILMES = {
    "big-buck-bunny": {
        "titulo": "Big Buck Bunny",
        "descricao": "2008 · Animação / Comédia",
        "rota": "main.assistir"
    },
    "nosferatu": {
        "titulo": "Nosferatu",
        "descricao": "1922 · Terror / Suspense",
        "rota": "main.nosferatu"
    },
    "cidade-lunar": {
        "titulo": "Cidade Lunar",
        "descricao": "2026 · Ficção científica",
        "rota": None
    },
    "entre-mundos": {
        "titulo": "Entre Mundos",
        "descricao": "2024 · Aventura",
        "rota": None
    },
    "noite-eterna": {
        "titulo": "Noite Eterna",
        "descricao": "2025 · Drama",
        "rota": None
    },
    "codigo-fantasma": {
        "titulo": "Código Fantasma",
        "descricao": "2026 · Ação",
        "rota": None
    },
    
    "oceano-azul": {
        "titulo": "Oceano Azul",
        "descricao": "2024 · Drama",
        "rota": None
    },
    "interestelar": {
        "titulo": "Interestelar",
        "descricao": "2014 · Ficção científica / Drama",
        "rota": None
    },
    "a-origem": {
        "titulo": "A Origem",
        "descricao": "2010 · Ficção científica / Suspense",
        "rota": None
    },
    "matrix": {
        "titulo": "Matrix",
        "descricao": "1999 · Ação / Ficção científica",
        "rota": None
    },
    "blade-runner-2049": {
        "titulo": "Blade Runner 2049",
        "descricao": "2017 · Ficção científica / Drama",
        "rota": None
    }

}


# Página inicial
@main_bp.route("/")
def home():
    usuario = None
    favoritos_ids = set()

    usuario_id = session.get("usuario_id")

    if usuario_id is not None:
        usuario = database.session.get(Usuario, usuario_id)

        if usuario is None:
            session.clear()
        else:
            consulta = select(Favorito.filme_id).where(
                Favorito.usuario_id == usuario.id
            )
            favoritos_ids = set(
                database.session.execute(consulta).scalars().all()
            )

    return render_template(
        "index.html",
        usuario=usuario,
        favoritos_ids=favoritos_ids
    )


# Criar conta
@main_bp.route("/criar-conta", methods=["GET", "POST"])
def criar_conta():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")

        if not nome or not email or not senha:
            flash("Preencha todos os campos.", "erro")
            return render_template("criar_conta.html")

        if len(senha) < 8:
            flash(
                "A senha deve ter pelo menos 8 caracteres.",
                "erro"
            )
            return render_template("criar_conta.html")

        consulta = select(Usuario).where(Usuario.email == email)
        usuario_existente = database.session.execute(
            consulta
        ).scalar_one_or_none()

        if usuario_existente:
            flash("Este e-mail já está cadastrado.", "erro")
            return render_template("criar_conta.html")

        novo_usuario = Usuario(
            nome=nome,
            email=email,
            senha=generate_password_hash(senha)
        )

        try:
            database.session.add(novo_usuario)
            database.session.commit()
        except Exception:
            database.session.rollback()
            flash(
                "Não foi possível concluir o cadastro. Tente novamente.",
                "erro"
            )
            return render_template("criar_conta.html")

        session.clear()
        session["usuario_id"] = novo_usuario.id

        flash("Conta criada com sucesso!", "sucesso")
        return redirect(url_for("main.home"))

    return render_template("criar_conta.html")


# Login
@main_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")

        consulta = select(Usuario).where(Usuario.email == email)
        usuario = database.session.execute(
            consulta
        ).scalar_one_or_none()

        if usuario is None or not check_password_hash(
            usuario.senha, senha
        ):
            flash("E-mail ou senha inválidos.", "erro")
            return render_template("login.html")

        session.clear()
        session["usuario_id"] = usuario.id

        flash("Login realizado com sucesso!", "sucesso")
        return redirect(url_for("main.home"))

    return render_template("login.html")


# Logout
@main_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("Você saiu da sua conta.", "sucesso")
    return redirect(url_for("main.home"))


# Página do Big Buck Bunny
@main_bp.route("/assistir")
def assistir():
    return render_template("assistir.html")


# Página do Nosferatu
@main_bp.route("/nosferatu")
def nosferatu():
    return render_template("nosferatu.html")


# Adicionar ou remover favorito
@main_bp.route("/favoritar/<string:filme_id>", methods=["POST"])
def favoritar(filme_id):
    usuario_id = session.get("usuario_id")

    if usuario_id is None:
        flash("Entre na sua conta para salvar favoritos.", "erro")
        return redirect(url_for("main.login"))

    if filme_id not in FILMES:
        flash("Filme não encontrado no catálogo.", "erro")
        return redirect(url_for("main.home"))

    consulta = select(Favorito).where(
        Favorito.usuario_id == usuario_id,
        Favorito.filme_id == filme_id
    )

    favorito = database.session.execute(
        consulta
    ).scalar_one_or_none()

    try:
        if favorito:
            database.session.delete(favorito)
            mensagem = "Filme removido da sua lista."
        else:
            favorito = Favorito(
                usuario_id=usuario_id,
                filme_id=filme_id
            )
            database.session.add(favorito)
            mensagem = "Filme adicionado à sua lista!"

        database.session.commit()
        flash(mensagem, "sucesso")

    except Exception:
        database.session.rollback()
        flash(
            "Não foi possível atualizar sua lista. Tente novamente.",
            "erro"
        )

    origem = request.form.get("origem")

    if origem == "minha-lista":
        return redirect(url_for("main.minha_lista"))

    return redirect(url_for("main.home"))


# Minha Lista
@main_bp.route("/minha-lista")
def minha_lista():
    usuario_id = session.get("usuario_id")

    if usuario_id is None:
        flash("Entre na sua conta para ver sua lista.", "erro")
        return redirect(url_for("main.login"))

    usuario = database.session.get(Usuario, usuario_id)

    if usuario is None:
        session.clear()
        flash("Entre na sua conta para ver sua lista.", "erro")
        return redirect(url_for("main.login"))

    consulta = select(Favorito).where(
        Favorito.usuario_id == usuario_id
    )

    favoritos = database.session.execute(
        consulta
    ).scalars().all()

    filmes = []

    for favorito in favoritos:
        dados_filme = FILMES.get(favorito.filme_id)

        if dados_filme:
            filmes.append({
                "id": favorito.filme_id,
                **dados_filme
            })

    return render_template(
        "minha_lista.html",
        usuario=usuario,
        filmes=filmes
    )
