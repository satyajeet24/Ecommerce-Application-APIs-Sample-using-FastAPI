from pydantic import BaseModel
from typing import List


# Data models (data classes) for creating respective APIs response obj
class Product(BaseModel):
    id: str
    name: str
    price: float
    quantity: int


class OrderItem(BaseModel):
    productId: str
    boughtQuantity: int
    totalAmount: float


class UserAddress(BaseModel):
    city: str
    country: str
    zipCode: str


class Order(BaseModel):
    items: List[OrderItem]
    userAddress: UserAddress

