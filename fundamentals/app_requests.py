import requests
from lxml import html


reps = requests.get(url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
# check responese
# print(reps.headers)

# check html
# print(reps.text)

# check html
# print(reps.content)

tree = html.fromstring(html=reps.text)
title = tree.xpath("//*[@class='col-sm-6 product_main']/h1/text()")[0]
desciption = tree.xpath("//article[@class='product_page']/p/text()")[0]
image = tree.xpath("//*[@class='item active']/img/@src")[0]
price = tree.xpath("//*[contains(@class, 'product_main')]/p/text()")[0]
quantity = tree.xpath("//*[contains(@class, 'product_main')]/p/text()")
text = map(str.strip, quantity)




print("TITLE: " + title)
print("DESCRIPTION: " + desciption)
print("IMAGE: " + image)
print("PRICE: " + price)
# print("QUANTITY: " + quantity)



