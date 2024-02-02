from src.mongo_client import MongoClientUtil
from datetime import datetime


class OrderService:
    def __init__(self):
        pass

    @staticmethod
    def create_order_service(order_dict):
        # Calculate total amount for the order
        product_items = order_dict.get("items")
        total_amount = sum(item.get("totalAmount") for item in product_items)
        user_address = order_dict.get("userAddress")

        # Create order document
        order_doc = {
            "createdOn": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
            "items": product_items,
            "totalAmount": total_amount,
            "userAddress": user_address,
        }

        mongo_client = MongoClientUtil()
        orders_collection = mongo_client.get_orders_collection_object()

        # Insert the order document into the MongoDB collection
        result = orders_collection.insert_one(order_doc)

        return result