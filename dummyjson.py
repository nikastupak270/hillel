import json
import requests

URL = 'https://dummyjson.com/products?limit=200'

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    products = data['products']
    total_premium_brand_price = 0
    print(f'id продуктів бренду TechGear')
    for product in products:
        if 'brand' in product and product['brand'] == 'TechGear':
            print(product['id'])
        if product['id'] == 135:
            images = product['images']
            for image in images:
                with open(image.split('/')[-1], 'wb') as f:
                    f.write(requests.get(image).content)
        if product['price'] > 800:
            total_premium_brand_price += product['price'] * product['stock']

print(f'Загальна вартість преміальних товарів: {total_premium_brand_price}')
