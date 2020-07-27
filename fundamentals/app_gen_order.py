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

Ho = ["Nguyễn", "Lê", "Trần", "Lý", "Phạm", "Hoàng", "Bùi", "Đỗ", "Phan", "Vũ", "Võ", "Đỗ", "Ngô", "Dương", "Đặng", "Hồ"]
TenLot = ["Nguyễn", "Lê", "Trần", "Lý", "Phạm", "Hoàng", "Bùi", "Đỗ", "Phan", "Vũ", "Võ", "Đỗ", "Ngô", "Dương", "Đặng", "Hồ", 
        "Anh", "Tuấn", "Thị", "Hữu", "Thanh", "Bảo", "Việt", "Minh"]
Ten = ["Anh", "Tuấn", "Thị", "Hữu", "Thanh", "Bảo", "Việt", "Minh", "Thư", "Huyền", "Tài", "Tiến", "Hào", "Duy", "Hạo", "Dương", "Đức", "Đào"
        "Quang", "Nhơn", "Nhi", "Lan", "Điệp", "Tú", "Chánh", "Hương", "Hóa", "Huy", "Hiếu", "Đang", "Bảo", "Vy", "Thủy", "Mạnh", "Cường", "Dũng"]


street = ["Bạch Đằng", "Võ Văn Kiệt", "Trưng Nữ Vương", "Duy Tân", "Hùng Vương", "Phan Châu Trinh", "Hoàng Diệu", "Hàm Nghi", "Điện Biên Phủ",
        "Trần Phú", "Triệu Nữ Vương", "Trần Cao Vân", "Tiểu La", "Núi Thành", "Vũ Hữu", "Nguyễn Hữu Dật", "Nguyễn Xuân Ôn", "30 Tháng 4",
        "Huỳnh Tấn Phát", "Ngô Tất Tố", "Hàn Thuyên", "2 Tháng 9", "Tố Hữu", "Đào Cam Mộc", "Xô Viết Nghệ Tĩnh", "Huy Cận", "Nguyễn Dữ"]
city = ["TP Đà Nẵng", "TP Hồ Chí Minh", "TP Hà Nội"]

for i in range(1,101):
    
    user_id = 10 + random.randrange(50)
    
    rand = random.randrange(2)
    if rand == 1:
        receiver_name = Ho[random.randrange(len(Ho))] + " " + TenLot[random.randrange(len(TenLot))] + " " + TenLot[random.randrange(len(TenLot))] + " " + Ten[random.randrange(len(Ten))] 
    else:
        receiver_name = Ho[random.randrange(len(Ho))] + " " + TenLot[random.randrange(len(TenLot))] + " " + Ten[random.randrange(len(Ten))] 

    receiver_phone = "0"
    receiver_phone += str(1 + random.randrange(9))
    for j in range(1,9):
        receiver_phone += str(random.randrange(10))
    
    receiver_address = "Số " + str(1 + random.randrange(60)) + " đường " + street[random.randrange(27)] + " " + city[random.randrange(3)]

    status = 1 + random.randrange(4)

    order = {
        'user_id': user_id,
        'receiver_name': receiver_name,
        'receiver_phone': receiver_phone,
        'receiver_address': receiver_address,
        'status' : status
    }
    
    data.append(order)
        # print
    
    print(order)
    
    print("---------------------------------------------")
    
write_to_json("order.json", data)