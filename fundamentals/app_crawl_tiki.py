import requests
from lxml import html
import random
import json
import urllib.request


# viết dữ liệu vào file
def write_to_json(filename, data):
    f = open(filename, 'w')
    f.write(json.dumps(data))
    f.close()

reps = requests.get(url = "https://tiki.vn/quan-jeans-nam/c920?src=c.915.hamburger_menu_fly_out_banner&_lc=Vk4wMjUwMDMwMDU=")
tree = html.fromstring(html=reps.text)

root = tree.xpath("//*[@class='product-box-list']/*")

i = 0
data = []

for e in root:
    
    url = "https://tiki.vn" + e.xpath(".//a/@href")[0]
    repsLoop = requests.get(url = url)
    treeLoop = html.fromstring(html=repsLoop.text)

    name = treeLoop.xpath("//h1/text()")[0]
    description = ""
    image = ""
    quantity = ""
    price = ""
    rate_avg = ""

    if i == 16: # maximum record
        break
    if name != 'Xin lỗi, trang bạn đang tìm kiếm ':
        
        descriptions = treeLoop.xpath("//*[@class='group border-top']/ul[@class='list']/li")
        for d in descriptions:
            description += d.xpath(".//text()")[0] + "/"
        
        #lấy link hình
        image = treeLoop.xpath("//*[@class='container']/img/@src")[0]
        f = open("fundamentals/images/image" + str(i) + ".jpg", 'wb')
        f.write(requests.get(image).content)

        quantity = random.randrange(100)
        
        price = treeLoop.xpath("//*[@class='summary']/*/*/p[1]/text()")[0]
        #remove dấu chấm
        price = price.replace('.','')
        #convert qua int
        price = int(price)

        rate_avg = random.randrange(5)

        i = i + 1
        # add vào cây json
        product = {
            'name': name,
            'description': description,
            'image': image,
            'quantity': quantity,
            'price': price,
            'category_id': 1,
            'rate_avg': rate_avg
        }
        data.append(product)
        # print
        print(name)
        print(description)
        print(image)
        print(quantity)
        print(price)
    print("---------------------------------------------")
    
write_to_json("data.json", data)