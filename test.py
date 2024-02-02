import asyncio
from src.Controller.products import ProductsController
from src.Controller.order import OrderController
from src.sample_objects import (
    order_sample_doc,
    create_dummy_product_doc,
    available_product_sample_doc

)


async def get_products():
    available_product_list_doc = available_product_sample_doc

    limit = available_product_list_doc.get("limit", 10)
    offset = available_product_list_doc.get("offset", 0)
    min_price = available_product_list_doc.get("min_price")
    max_price = available_product_list_doc.get("max_price")

    await ProductsController().get_products(available_product_list_doc, limit, offset, min_price, max_price)


async def create_order():
    order_doc = order_sample_doc
    order_creation = OrderController()
    await order_creation.create_order(order_doc)


async def create_dummy_products():
    dummy_product_doc = create_dummy_product_doc
    ProductsController().create_dummy_products(dummy_product_doc)


if __name__ == "__main__":
    asyncio.run(get_products())

    # asyncio.run(create_order())

    # asyncio.run(create_dummy_products())





