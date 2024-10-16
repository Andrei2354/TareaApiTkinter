
import requests

URL = "https://dummyjson.com/products"
response = requests.get(URL)
print('Data:', response.json())

