from flask_marshmallow import Marshmallow, fields
from .model import Produto


ma = Marshmallow()


def configure(app):
    ma.init_app(app)

class EstoqueSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = Produto
        load_instance = True
       
        