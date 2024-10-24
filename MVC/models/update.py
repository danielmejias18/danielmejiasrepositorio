from models.db import engine, base
from Pygubu.Pygubu.controller.product import Product

if __name__ == "__main__":
    base.metadata.create_all(engine)
