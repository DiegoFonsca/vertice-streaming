
from run import app
from app import database
from app import models

with app.app_context():
    database.create_all()
    print("Tabelas criadas com sucesso!")
