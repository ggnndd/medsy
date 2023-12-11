import requests
from bs4 import BeautifulSoup

a = 1

for i in range (53):

    urlnumber = 'https://medsi.ru/articles/p/' + str(a)

    print(urlnumber)
    def get_number():
        response = requests.get(urlnumber)
        response = response.content
        html = BeautifulSoup(response, 'html.parser')
        number = html.find(class_='med-pagination-current')
        print('страница', number.text)
    get_number()

    def get_title():
        response = requests.get(urlnumber)
        response = response.content
        html = BeautifulSoup(response, 'html.parser')
        title = html.find(class_='med-articles-page__articles__wrapper')

        print(title.text)
    get_title()

    a = a + 1
