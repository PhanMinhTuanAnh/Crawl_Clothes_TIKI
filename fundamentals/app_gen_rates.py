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

data = []

contentsPositive = ["Đồ ngon, đồ ngon.", "đẹp 10/10.", "ship nhanh - chất lượng và y hình.", "Đẹp lắm nhé mọi người kkkk.", 
                    "Tôi rất thick chất liệu vải tốt và đẹp.", "OK", "Rất ưng *dấu bé ba", "Hài lòng. Mặc rất dễ thương.",
                    "Hàng đẹp, đúng như mô tả, hài lòng!", "Chất rất thích , mình rất ưng luôn", "Hàng đúng hình giao hàng nhanh",
                    "sản phẩm vừa ý", "Form đẹp, vải ok, kiểu dáng dễ thương dễ mặc, giá cả phù hợp", 
                    "Hàng nhận được như ảnh, lên form đẹp, chất liệu ok. Hài lòng.", "Chất không được đẹp nhưng dáng may khá ổn. Màu sắc như hình."]
contentsNegative = ["quá tệ. mình mua về xong vứt luôn vì không thể mặc được.", "Lừaaaaaa ...", "Sao hình đẹp mà, hàng đến tay xấu vậy :(", 
                    "Sản phẩm bị lỗi lũng 1 lỗ đổi trả thể nào ạ", "Thất vọng ..."]

for i in range(1,101):
    
    value = 3 + random.randrange(3)

    product_id = 1 + random.randrange(352)

    content = ""
    if value == 3:
        content = contentsNegative[random.randrange(5)]
    else:
        content = contentsPositive[random.randrange(15)]
    
    user_id = 10 + random.randrange(50)
    
    rate = {
        'value': value,
        'product_id': product_id,
        'content': content,
        'user_id': user_id,
    }
    
    data.append(rate)
        # print
    
    print(rate)
    
    print("---------------------------------------------")
    
write_to_json("rate.json", data)