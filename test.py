import requests
from bs4 import BeautifulSoup as bts

url = requests.get("https://olcha.uz/ru/category/s-ruki-olcha")

# print(url.status_code)
html_content = bts(url.content, 'html.parser')



for buyum in html_content.select("#splide__track splide__track--slide splide__track--ltr splide__track--draggable"):
    a = buyum.select(".product-card _big .product-card__content")[0].text
    print(a)









# class="row products-list"


# print(html_content.select('#main'))
# for havo in html_content.select('#main'):
#     min = havo.select('.day-link')
#     print(min)

