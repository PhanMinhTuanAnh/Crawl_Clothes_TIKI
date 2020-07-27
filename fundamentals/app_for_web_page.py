from lxml import etree

# lấy cấu trúc của html ra
tree = etree.parse("fundamentals/src/web_page.html")

# LXML WITH ELEMENT OBJECT #

# print(etree.tostring(tree))
#---------------------------------------------------#
# tìm theo thẻ head -> thẻ title
title_element = tree.find("head/title")
# get text của element
print(title_element.text)
#----------------------------------------------------#
# tìm theo thẻ body -> thẻ p
p_element = tree.find("body/p")
# get text của element
print(p_element.text)
#----------------------------------------------------#
# get list_item thẻ li
list_item = tree.findall("body/ul/li")
print(list_item)
# get nội dung của từng element
for li in list_item:
    # kiểm tra xem trong thẻ li có a không nếu có thì in ra không thì thôi
    a = li.find("a")
    if a is not None:
        # nếu chỉ in ra cách này thì nó sẽ ra kết quả kiểu
        # Created by:
        #      Ahmed Rafik
        # vì trong thẻ nó bị tách ra bởi thẻ a nằm thụt vào trong
        # print(f"{li.text} {a.text}")
        # để remove cái này mình gọi text.strip()
        print(f"{li.text.strip()} {a.text}")
    else:
        print(li.text) 

print("--------------------end of element object -----------------------")

# LXML WITH XPATH #

# tìm theo thẻ head -> thẻ title
title_element = tree.xpath("//title")[0]
# get text của element
# nếu để nguyên là .text thì xảy ra lỗi vì xpath trả về một list
# nó hoạt động như ông findall để lấy title đầu tiên thì chỉ cần ghi như trên
print(title_element.text)

# một cách khác
title_element = tree.xpath("//title/text()")[0]
print(title_element)
#-----------------------------------------------------------#
p_element = tree.xpath("//p/text()")[0]
print(p_element)
#-----------------------------------------------------------#
list_item = tree.xpath("//li")
for li in list_item:
    #li.xpath("//text()") để ri không thì nó sẽ get text của 
    # tất cả các Element
    # sửa lại dấu chấm nó sẽ lấy tiếp mấy Element từ li vào phía trong
    # map(str.strip) để mỗi thằng phải cắt gọn phần tử trống,
    # nó get từng hàng, kể cả hàng trống có thẻ li
    # <li class='myClass'>Created by:
    #     <a href='https://twitter.com/AhmedRafik__'>Ahmed Rafik</a>
    # </li>
    # như khúc này thì có 3 đoạn: "Created by:", "Ahmed Rafik", ""
    text = map(str.strip, li.xpath(".//text()"))
    print(list(text))

    # join các phần tử trong map lại thành một chuỗi 
    text = ''.join(map(str.strip, li.xpath(".//text()")))
    print(text)
