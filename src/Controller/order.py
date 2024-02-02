from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from src.validations import order_validations
from src.data_models import Order
from src.Service.order_service import OrderService
from src.exception import OrderCreationError


app = FastAPI()


class OrderController:
    def __init__(self):
        pass

    # API to create a new order
    @app.post("/orders/", response_model=Order)
    async def create_order(self, order: Order):
        try:
            # validate current order before inserting into database
            order_validations(order)

            result = OrderService.create_order_service(order)
            response_data = {"order_id": str(result.inserted_id), "message": "Order created successfully"}

            print(response_data)

            return JSONResponse(content=response_data)

        except OrderCreationError as e:
            print(f"An exception occurred while creating order:  {e}")

        except HTTPException as hte:
            print(f"http exception occurred while creating order: {hte}")