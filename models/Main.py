import json
from itertools import product

import requests
from dataclass_wizard import fromdict
from models.ApiResponse import APIResponse

response = requests.get("https://dummyjson.com/products")
data1 = response.json()
product_list = fromdict(APIResponse, data1)



# data_String = json.dumps(data1)
# my_obj = json.loads(data_String, object_hook=lambda data: Product(**data))

