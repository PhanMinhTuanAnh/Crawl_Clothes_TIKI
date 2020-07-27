import requests
from lxml import html
import random
import json
import urllib.request
import json

# viết dữ liệu vào file
def write_to_json(filename, data):
    f = open(filename, 'w')
    f.write(json.dumps(data))
    f.close()

ff = open('data.json', 'r')
products = json.load(ff)

data = []

for i in range(1,101):
    
    order_id = i
    
    product_iter = 2 + random.randrange(3)
    random_range = [0,]
    rangee = 352

    for j in range(1, product_iter) :
        rangee = rangee - random_range[j - 1]
        
        if rangee == 0:
            break
        random_range.append(1 + random.randrange(rangee))
        
        print(random_range[j])

        product_id = 1 + random_range[j - 1] + random.randrange(random_range[j])

        quantity = 1 + random.randrange(3)

        price_unit = products[product_id - 1]['price']

        price_total = price_unit * quantity

        orderItem = {
            'order_id': order_id,
            'product_id': product_id,
            'quantity': quantity,
            'price_unit': price_unit,
            'price_total': price_total,
        }
        
        data.append(orderItem)
            # print
        
        print(orderItem)
        
        print("---------------------------------------------")
    
write_to_json("orderItem.json", data)