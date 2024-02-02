from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from src.validations import filter_validations
from src.Service.products_service import ProductsService
from src.data_models import Product
from src.exception import DummyProductCreationError, GetProductsError


app = FastAPI()


class ProductsController:
    def __init__(self):
        pass

    # API to list all available products
    @app.get("/products/", response_model=Product)
    async def get_products(self, filter_dict,
                           limit: int = Query(10, alias="limit", description="Number of records per page"),
                           offset: int = Query(0, alias="offset", description="Offset for pagination"),
                           min_price: Optional[float] = Query(None, description="Minimum product price filter"),
                           max_price: Optional[float] = Query(None, description="Maximum product price filter"),
                           ):
        try:
            # validate the given filters
            filter_validations(filter_dict)

            query_obj = {}
            if min_price:
                query_obj["price"] = {"$gte": min_price}
            if max_price:
                query_obj["price"] = {"$lte": max_price}

            response_data = ProductsService().get_products(query_obj, limit, offset)

            return JSONResponse(content=response_data)

        except GetProductsError as exc:
            print(f"An exception occurred while fetching products: {exc}")

        except HTTPException as hte:
            print(f"http exception occurred while fetching products: {hte}")

    # API to create dummy products
    @app.post("/create_dummy_products/", response_model=Product)
    def create_dummy_products(self, dummy_products: Product):
        try:
            response_data = ProductsService().create_dummy_products(dummy_products)

            # Prepare the response data with the relevant information
            inserted_id = response_data.inserted_id
            response_data = {
                "inserted_id": str(inserted_id),
                "message": "Dummy product created successfully",
            }

            print(response_data)

            return JSONResponse(content=response_data)

        except DummyProductCreationError as exc:
            print(f"An exception occurred while dummy product creation: {exc}")

        except HTTPException as hte:
            print(f"http exception occurred while creating dummy products: {hte}")
