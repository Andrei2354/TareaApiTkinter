import json
import requests

import ProductApi
from ProductApi import Products

URL = "https://dummyjson.com/products"
response = requests.get(URL)
data1 = response.json()
data_String = json.dumps(data1)
# print('Data:', response.json())

data_String1 = '{"id": 1}'

my_obj = json.loads(data_String1, object_hook=lambda data: Products(**data))
print(data_String)
print(my_obj)
