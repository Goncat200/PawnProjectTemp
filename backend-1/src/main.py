from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ideally specify the frontend address in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
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

# Sample data
users = [User(id=1, username="admin", email="admin@mail.com")]
products = [
    Product(id=1, title="Chess Bot", description="AI chess bot", price=10.0, image="https://placehold.co/200"),
    Product(id=2, title="Opening Book", description="PDF openings", price=5.0, image="https://placehold.co/200"),
]
messages = []

# Endpoints
@app.get("/products", response_model=List[Product])
def get_products():
    return products

@app.get("/featured", response_model=List[Product])
def get_featured():
    return products[:3]

@app.post("/search", response_model=List[Product])
def search_products(q: str):
    return [p for p in products if q.lower() in p.title.lower()]

@app.post("/purchase")
def purchase(product_id: int, user_id: int):
    # Purchase logic here
    return {"status": "success", "product_id": product_id, "user_id": user_id}

@app.get("/user", response_model=User)
def get_user():
    return users[0]

@app.post("/chat/send", response_model=Message)
def send_message(msg: Message):
    messages.append(msg)
    return msg

@app.get("/chat/{user_id}", response_model=List[Message])
def get_messages(user_id: int):
    return [m for m in messages if m.receiver_id == user_id or m.sender_id == user_id]