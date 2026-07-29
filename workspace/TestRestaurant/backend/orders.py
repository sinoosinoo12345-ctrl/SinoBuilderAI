
from fastapi import APIRouter


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


orders = []


@router.get("/")
def get_orders():

    return orders



@router.post("/")
def create_order(
    order: dict
):

    orders.append(order)

    return {
        "message": "Order created",
        "order": order
    }
