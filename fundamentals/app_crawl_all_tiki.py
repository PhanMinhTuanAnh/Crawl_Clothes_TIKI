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

urls = {
        # Áo nam
        "1-3-9":"https://tiki.vn/ao-thun-nam/c917?_lc=Vk4wMjUwMDMwMDU%3D", # thun
        "1-3-10":"https://tiki.vn/ao-so-mi-nam/c918?_lc=Vk4wMjUwMDMwMDU%3D", # sơ mi
        "1-3-11":"https://tiki.vn/ao-hoodie-nam/c10382?_lc=Vk4wMjUwMDMwMDU%3D", # hoodie
        "1-3-12":"https://tiki.vn/ao-len-nam/c27554?_lc=Vk4wMjUwMDMwMDU%3D", # len
        "1-3-13":"https://tiki.vn/ao-khoac-nam/c925?_lc=Vk4wMjUwMDMwMDU%3D", # khoác       
        # Quần nam
        "1-4-14":"https://tiki.vn/quan-jogger-nam/c5409?src=c.915.hamburger_menu_fly_out_banner&_lc=Vk4wMjUwMDMwMDU%3D", # jean
        "1-4-15":"https://tiki.vn/quan-jeans-nam/c920?src=c.915.hamburger_menu_fly_out_banner&_lc=Vk4wMjUwMDMwMDU%3D", # jogger
        "1-4-16":"https://tiki.vn/thoi-trang-nam-quan-kaki/c921?src=c.915.hamburger_menu_fly_out_banner&_lc=Vk4wMjUwMDMwMDU%3D", # kaki
        "1-4-17":"https://tiki.vn/thoi-trang-nam-quan-sooc/c923?src=c.915.hamburger_menu_fly_out_banner&_lc=Vk4wMjUwMDMwMDU%3D", # shorts
        "1-4-18":"https://tiki.vn/quan-tay-nam/c922?src=c.915.hamburger_menu_fly_out_banner&_lc=Vk4wMjUwMDMwMDU%3D", # tây
        # Áo nữ
        "2-5-19":"https://tiki.vn/ao-thun-nu/c933?_lc=Vk4wMjUwMDMwMDU%3D", # thun
        "2-5-20":"https://tiki.vn/ao-so-mi-nu/c934?_lc=Vk4wMjUwMDMwMDU%3D", # sơ mi
        "2-5-21":"https://tiki.vn/ao-khoac-nu/c936?_lc=Vk4wMjUwMDMwMDU%3D", # khoác
        # Quần nữ
        "2-6-22":"https://tiki.vn/quan-jean-nu/c1701?_lc=Vk4wMjUwMDMwMDU%3D", # jean
        "2-6-23":"https://tiki.vn/quan-kaki-nu/c8385?_lc=Vk4wMjUwMDMwMDU%3D", # kaki
        "2-6-24":"https://tiki.vn/quan-legging/c1716?_lc=Vk4wMjUwMDMwMDU%3D", # legging
        "2-6-25":"https://tiki.vn/quan-sooc/c939?_lc=Vk4wMjUwMDMwMDU%3D", # shorts
        "2-6-26":"https://tiki.vn/thoi-trang-nu-quan-dai/c938?_lc=Vk4wMjUwMDMwMDU%3D", # tay
        # Chân váy
        "2-2-8":"https://tiki.vn/chan-vay-nu/c5404?_lc=Vk4wMjUwMDMwMDU%3D", # chân váy
        # Đầm nữ
        "2-8-27":"https://tiki.vn/dam-suong/c27584?_lc=Vk4wMjUwMDMwMDU%3D", # suông
        "2-8-28":"https://tiki.vn/dam-xoe/c27582?_lc=Vk4wMjUwMDMwMDU%3D", # xòe
        "2-8-29":"https://tiki.vn/dam-om/c27580?_lc=Vk4wMjUwMDMwMDU%3D", # ôm
        }


categoryID = 9
data = []

for key in urls:
    url = urls[key]
    reps = requests.get(url = url)
    tree = html.fromstring(html=reps.text)

    root = tree.xpath("//*[@class='product-box-list']/*")

    i = 0
    count = 0


    for e in root:
        
        try:
            urlE = "https://tiki.vn" + e.xpath(".//a/@href")[0]
            repsLoop = requests.get(url = urlE)
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
                f = open("fundamentals/images/image-" + key + "-" + str(count) + "-(0)" + ".jpg", 'wb')
                f.write(requests.get(image).content)
                image = "image-" + key + "-" + str(count) + "-(0)" + ".jpg"

                quantity = random.randrange(100)
                
                price = treeLoop.xpath("//*[@class='summary']/*/*/p[1]/text()")[0]
                #remove dấu chấm
                price = price.replace('.','')
                #convert qua int
                price = int(price)

                category_id = categoryID

                rate_avg = random.randrange(5)

                i = i + 1
                count = count + 1
                # add vào cây json
                product = {
                    'name': name,
                    'description': description,
                    'image': image,
                    'quantity': quantity,
                    'price': price,
                    'category_id': category_id,
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
        except Exception:
            pass
    categoryID = categoryID + 1
    
write_to_json("data.json", data)