import requests
import csv
from bs4 import BeautifulSoup
from bs4 import Tag, ResultSet

URL = 'https://www.kivano.kg/mobilnye-telefony'

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
print(type(headers))
response = requests.get(URL, headers=headers)


def get_html_card():       
    html = requests.get(URL)
    soup = BeautifulSoup(html.text, 'lxml')
    cards: ResultSet = soup.find_all('div', class_="item product_listbox oh")
    return cards
 

def parse_cards(cards):
    obj_list = []
    for i in cards:
        obj = {
            'title':i.find('div', class_='listbox_title oh').find('a').text,
            'price': str(i.find('div', class_= 'listbox_price text-center').text),
            'link_img': i.find('div', class_='listbox_img pull-left').find('img').get('src'),
        }
        obj_list.append(obj)
    with open('csvDB.csv', 'w') as file:
        fieldnames = obj_list[0].keys()
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(obj_list)

cards = get_html_card()
parse_cards(cards)

