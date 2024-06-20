from models import *

def initialize_database():
    db.connect()
    db.create_tables([Category, Supplier, Product, Order], safe=True)
    db.close()
