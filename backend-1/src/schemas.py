from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    username: str
    email: str

class Product(BaseModel):
    id: int
    title: str
    description: str
    price: float
    image: Optional[str] = None

class Message(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    text: str

class Purchase(BaseModel):
    product_id: int
    user_id: int

class SearchQuery(BaseModel):
    q: str

class UserResponse(BaseModel):
    user: User

class ProductResponse(BaseModel):
    product: Product

class MessageResponse(BaseModel):
    message: Message

class ProductsResponse(BaseModel):
    products: List[Product]