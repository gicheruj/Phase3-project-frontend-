from peewee import *

db = SqliteDatabase('inventory.db')

class BaseModel(Model):
    class Meta:
        database = db

class Category(BaseModel):
    name = CharField(unique=True)

class Supplier(BaseModel):
    name = CharField(unique=True)
    contact_info = CharField()

class Product(BaseModel):
    name = CharField(unique=True)
    description = CharField()
    category = ForeignKeyField(Category, backref='products')
    supplier = ForeignKeyField(Supplier, backref='products')
    stock_quantity = IntegerField(default=0)
    price = IntegerField()

class Order(BaseModel):
    product = ForeignKeyField(Product, backref='orders')
    quantity = IntegerField()
    order_date = DateField()
