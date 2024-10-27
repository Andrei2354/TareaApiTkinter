

from models.ProductApi import Product
from dataclasses import dataclass

@dataclass
class APIResponse:
    products: list[Product]
    total: int
    skip: int
    limit: int