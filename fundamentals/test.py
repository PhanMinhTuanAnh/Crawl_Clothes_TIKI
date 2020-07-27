import urllib.request


def dl_ipg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

url = "https://salt.tikicdn.com/cache/w390/ts/product/60/90/f4/9aff972f76a562f831efa964e943b461.jpg"
file_path = "fundamentals/images"
file_name = "test"

dl_ipg(url, file_path, file_name)

s = "192.123"
s = s.replace(".","")

print(int(s))