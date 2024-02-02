from src.mongo_client import MongoClientUtil


class ProductsService:
    def __init__(self):
        self.mongo_client = MongoClientUtil()

    def get_products(self, query_obj, limit, offset):
        products_collection = self.mongo_client.get_products_collection_object()

        products = list(products_collection.find(query_obj).skip(offset).limit(limit))
        total_records = products_collection.count_documents(query_obj)

        next_offset = offset + limit if offset + limit < total_records else None
        prev_offset = offset - limit if offset - limit >= 0 else None

        products = self.clean_products_details(products)

        response_data = {
            "data": products,
            "page": {
                "limit": limit,
                "nextOffset": next_offset,
                "prevOffset": prev_offset,
                "total": total_records,
            },
        }

        print(response_data)

        return response_data

    def create_dummy_products(self, dummy_products_document):
        # mongo transaction obj of products table
        products_collection = self.mongo_client.get_products_collection_object()

        result = products_collection.insert_one(dummy_products_document)

        return result

    @staticmethod
    def clean_products_details(products):
        products = [
            {
                "id": product.get("id"),
                "name": product.get("name"),
                "price": product.get("price"),
                "quantity": product.get("quantity")
            }
            for product in products
        ]

        return products

