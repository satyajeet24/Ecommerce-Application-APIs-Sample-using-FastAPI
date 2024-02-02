from pymongo import MongoClient


# MongoDB connection setup and getter methods to provide respective db tables
class MongoClientUtil:
    def __init__(self):
        client = MongoClient("mongodb://localhost:27017/")
        self.db = client["ecommerce"]

    def get_products_collection_object(self):
        products_collection = self.db["products"]

        return products_collection

    def get_orders_collection_object(self):
        orders_collection = self.db["orders"]

        return orders_collection
