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
street = ["Bạch Đằng", "Võ Văn Kiệt", "Trưng Nữ Vương", "Duy Tân", "Hùng Vương", "Phan Châu Trinh", "Hoàng Diệu", "Hàm Nghi", "Điện Biên Phủ",
        "Trần Phú", "Triệu Nữ Vương", "Trần Cao Vân", "Tiểu La", "Núi Thành", "Vũ Hữu", "Nguyễn Hữu Dật", "Nguyễn Xuân Ôn", "30 Tháng 4",
        "Huỳnh Tấn Phát", "Ngô Tất Tố", "Hàn Thuyên", "2 Tháng 9", "Tố Hữu", "Đào Cam Mộc", "Xô Viết Nghệ Tĩnh", "Huy Cận", "Nguyễn Dữ"]
city = ["TP Đà Nẵng", "TP Hồ Chí Minh", "TP Hà Nội"]

for i in range(1,61):
    
    name = "user" + str(i)
    
    email = name + "@gmail.com"
    
    avatar = ""

    phone = "0"
    phone += str(1 + random.randrange(9))
    for j in range(1,9):
        phone += str(random.randrange(10))
    
    address = "Số " + str(1 + random.randrange(60)) + " đường " + street[random.randrange(27)] + " " + city[random.randrange(3)]
    
    password_digest = "123456"
    
    role = "USER"
    if i < 10:
        role = "ADMIN"
    
    user = {
        'name': name,
        'email': email,
        'avatar': avatar,
        'phone': phone,
        'address': address,
        'password_digest': password_digest,
        'role': role
    }
    
    data.append(user)
        # print
    
    print(user)
    
    print("---------------------------------------------")
    
write_to_json("user.json", data)