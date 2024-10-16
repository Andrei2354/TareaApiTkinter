from ProductApi import *

@dataclass
class APIResponse:
    products: list[Product]
    total: int
    skip: int
    limit: int