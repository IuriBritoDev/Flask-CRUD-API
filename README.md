# Flask-CRUD-API
 Api de estoque de produtos

# Descrição do projeto
 O sistema se constitui de uma API de um CRUD de um estoque, que permite cadastrar, editar, deletar e visualizar produtos.

# Construindo o projeto

## Intalando as bibliotecas
 pip install flask 
 
 pip install Flask-SQLAlchemy 
 
 pip install flask-marshmallow
 
 pip install marshmallow-sqlalchemy
 
 pip install Flask-Migrate

## Criando as migrações
 flask db init
 
 flask db migrate
 
 flask db upgrade

## Rodando o servidor
 flask run
 
## Rotas
 http://127.0.0.1:5000/cadastrar
 
 http://127.0.0.1:5000/editar/1
 
 http://127.0.0.1:5000/deletar/1
 
 http://127.0.0.1:5000/mostrar

## Modelo de Json
 {
 
     "nome": "Nome",
     
     "marca": "Marca",
     
     "preco": 5.5,
     
     "quantidade": 10   
     
 }
