
from bs4 import BeautifulSoup
import requests


url = "https://coinmarketcap.com/"

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'html.parser')

div = soup.find_all('div', attrs={'class':'cmc-table__table-wrapper-outer'})

table = div[2].find('table')

table_body = table.find('tbody')

rows = table_body.find_all('tr')

top_capitalization_list = []

for row in rows:
    cells = row.find_all('td')
    rank = cells[0].find(text=True)
    name = cells[1].find(text=True)
    market_cap = cells[2].find(text=True)
    price = cells[3].find(text=True)
    volume = cells[4].find(text=True)
    
    top_capitalization_position = { 'rank':rank , 'name': name, 'market_cap': market_cap, 'price': price, 'volume': volume}
    
    top_capitalization_list.append(top_capitalization_position)


def get_all_list():
    return top_capitalization_list

def get_rank_name_list(list_position=100):
    name_rank_list = []
    for rank_list in top_capitalization_list:
        rank_name = {"rank":rank_list["rank"],"name":rank_list["name"]}
        name_rank_list.append(rank_name)

    return name_rank_list[0:list_position]

def get_rank_list(list_position=100):
    rank_list = []
    for top_single_list in top_capitalization_list:
        rank = {top_single_list["rank"]:top_single_list["name"]}
        rank_list.append(rank)

    return rank_list[0:list_position]

# print(get_rank_name_list(10))
        

        
        

