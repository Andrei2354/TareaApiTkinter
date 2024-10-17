from dataclasses import dataclass
from typing import Optional, List
from models.Dimension import Dimensions
from models.Metas import Meta
from models.Review import Reviews

@dataclass
class Product(object):
        title: str
        description: str
        category: str
        price: float
        discountPercentage: float
        rating: float
        stock: int
        tags: List[str]
        sku: str
        weight: int
        dimensions: dict[Dimensions]
        warrantyInformation: str
        shippingInformation: str
        availabilityStatus: str
        reviews: List[Reviews]
        returnPolicy: str
        minimumOrderQuantity: int
        meta: dict[Meta]
        images: List[str]
        thumbnail: str
        brand: Optional[str] = None
