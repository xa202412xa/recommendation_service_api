from pydantic import BaseModel

class Purchase(BaseModel):
    item_id: str
    category: str

class PurchaseRequest(BaseModel):
    user_id: str
    cart: list[Purchase]

class Recommendation(BaseModel):
    user_id: str
    item_id: str
