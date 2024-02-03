import asyncio
import json
from fastapi import HTTPException
from fastapi.responses import JSONResponse
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

    response = await ProductsController().get_products(available_product_list_doc, limit, offset, min_price, max_price)

    if isinstance(response, JSONResponse):
        try:
            products_data = json.loads(response.body)
            print(products_data)

        except ValueError:
            raise HTTPException(status_code=500, detail="Failed to parse JSON response")
    else:

        raise HTTPException(status_code=500, detail="Unexpected response type")


async def create_order():
    order_doc = order_sample_doc
    order_creation = OrderController()
    order_response = await order_creation.create_order(order_doc)

    if isinstance(order_response, JSONResponse):
        try:
            products_data = json.loads(order_response.body)
            print(products_data)

        except ValueError:
            raise HTTPException(status_code=500, detail="Failed to parse JSON response")

    else:
        raise HTTPException(status_code=500, detail="Unexpected response type")


async def create_dummy_products():
    dummy_product_doc = create_dummy_product_doc
    dummy_product_create_response = ProductsController().create_dummy_products(dummy_product_doc)

    if isinstance(dummy_product_create_response, JSONResponse):
        try:
            products_data = json.loads(dummy_product_create_response.body)
            print(products_data)

        except ValueError:
            raise HTTPException(status_code=500, detail="Failed to parse JSON response")

    else:
        raise HTTPException(status_code=500, detail="Unexpected response type")


if __name__ == "__main__":
    # asyncio.run(get_products())

    # asyncio.run(create_order())

    asyncio.run(create_dummy_products())





