from dataclasses import dataclass
from typing import Optional
from Dimension import Dimensions
from Meta import Meta
from Review import Reviews
@dataclass
class Products(object):
    def __init__(self, id: int):
        self.id = id

    def __repr__(self):
        return f"{self.id}"

# , title: str, description: str, category: str, price: int, discountPercentage: int, rating: int, stock: int, tags: list[str], sku: str, weight: int, dimensions: Dimensions, warrantyInformation: str, shippingInformation: str, availabilityStatus: str, reviews: Reviews, returnPolicy: str, minimumOrderQuantity: int, meta: Meta, images: list[str], thumbnail: str, brand: Optional[str] = None

    # id: int
    # title: str
    # description: str
    # category: str
    # price: int
    # discountPercentage: int
    # rating: int
    # stock: int
    # tags: list[str]
    # sku: str
    # weight: int
    # dimensions: Dimensions
    # warrantyInformation: str
    # shippingInformation: str
    # availabilityStatus: str
    # reviews: Reviews
    # returnPolicy: str
    # minimumOrderQuantity: int
    # meta: Meta
    # images: list[str]
    # thumbnail: str
    # brand: Optional[str] = None