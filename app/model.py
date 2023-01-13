from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    marca = db.Column(db.String(255))
    preco = db.Column(db.Float(20))
    quantidade = db.Column(db.Integer)
    

    def __init__(self, nome, marca, preco, quantidade):
        self.nome = nome
        self.marca = marca
        self.preco = preco
        self.quantidade = quantidade
