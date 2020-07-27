from lxml import etree

# .text là lấy nội dung giữa các thẻ
# lấy cấu trúc của html ra
tree = etree.parse("fundamentals/src/web.html")

# .../<tên thẻ>[@<tên thuộc tính>='...']/<tên thẻ>[...]
element = tree.xpath("//div[@class='outro']/p[@id='outside']")

for p in element:
    # này lấy nội dung giữa thẻ, value các thứ
    print(p.text)


# ...//a/@href
# lấy nội dung của thuộc tính
aa = tree.xpath("//a/@href")
# vì nội dung của thuộc tính nên k cần .text
for a in aa:
    print(a)


# ...//a[starts-with(@<attribute>, 'https')]
# lấy element có chứa phần đầu 'https' nội dung thuộc tính 'href'
aa = tree.xpath("//a[starts-with(@href, 'https')]")
for a in aa:
    print(a.text)

# ...//a[ends-with(@<attribute>, 'fr')]
# lấy element có chứa phần cuối 'fr' nội dung thuộc tính 'href'
aa = tree.xpath("//a[contains(@href, 'fr')]")
for a in aa:
    print(a.text)


# ...//a[contains(@<attribute>, 'google')]
# lấy element có chứa chuỗi 'google' bên trong nội dung thuộc tính
aa = tree.xpath("//a[contains(@href, 'google')]")
for a in aa:
    print(a.text)


# ...//a[contains(text(), 'google')]
# lấy element có chứa 'Google' bên trong nội dung giữa các thẻ a
aa = tree.xpath("//a[contains(text(),'Google')]")
for a in aa:
    print(a.text)  


# ...//ul[@id='items']/li[position() = 1 or position() = 4]
# ...//ul[@id='items']/li[position() = 1 or position() = last()]
# ...//ul[@id='items']/li[position() > 1]
aa = tree.xpath("//ul[@id='items']/li[position() = 1 or position() = last()]")
for a in aa:
    print(a.text)  

