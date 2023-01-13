from flask import Blueprint, current_app, request, jsonify
from .model import Produto
from .serealizer import EstoqueSchema


bp_produto = Blueprint('produtos', __name__)


@bp_produto.route('/mostrar', methods=['GET'])
def mostrar():
    es = EstoqueSchema(many=True)
    result = Produto.query.all()

    return es.jsonify(result), 200


@bp_produto.route('/deletar/<id>', methods=['GET'])
def deletar(id):
    Produto.query.filter(Produto.id == id).delete()
    current_app.db.session.commit()

    return jsonify('deletado!')


@bp_produto.route('/editar/<id>', methods=['POST'])
def editar(id):
    es = EstoqueSchema()
    query = Produto.query.filter(Produto.id == id)
    query.update(request.json)
    current_app.db.session.commit()

    return es.jsonify(query.first())


@bp_produto.route('/cadastrar', methods=['POST'])
def cadastrar():
    es = EstoqueSchema()
    produto = es.load(request.json)
    current_app.db.session.add(produto)
    current_app.db.session.commit()

    return es.jsonify(produto), 201
