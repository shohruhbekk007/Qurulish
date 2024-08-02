


































# from eskiz_sms import EskizSMS

# # Создаем экземпляр класса EskizSMS
# sms_sender = EskizSMS(api_key='https://notify.eskiz.uz/api', api_secret='zeyu5tlOIttzoINCFEpPVXBe2n1KuWu5tXJnKa0q')

# # Номер телефона, на который отправляем SMS
# phone_number = '+998883601656'

# # Текст сообщения
# message = 'salom maktab'

# # Отправка SMS
# response = sms_sender.send_sms(to=phone_number, text=message)

# # Обработка ответа
# if response['status'] == 'success':
#     print('SMS успешно отправлено')
# else:
#     print(f'Ошибка при отправке SMS: {response["message"]}')


















# import requests
# from bs4 import BeautifulSoup as bts

# url = requests.get("https://olcha.uz/ru/category/s-ruki-olcha")

# # print(url.status_code)
# html_content = bts(url.content, 'html.parser')



# for buyum in html_content.select("#splide__track splide__track--slide splide__track--ltr splide__track--draggable"):
#     a = buyum.select(".product-card _big .product-card__content")[0].text
#     print(a)




# class="row products-list"


# print(html_content.select('#main'))
# for havo in html_content.select('#main'):
#     min = havo.select('.day-link')
#     print(min)
a = 10000000
print(f'{a:_}')
