from main import db
from main import ProductModel

db.create_all()

product_1 = ProductModel(name='Produto Um', description='Uma descrição')
db.session.add(product_1)
db.session.commit()
