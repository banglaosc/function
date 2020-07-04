
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta,date

today_date = date.today()

past_date_before_3_months = today_date - timedelta(days = 90) 

query_end_date = str(today_date).replace('-','')
query_start_date = str(past_date_before_3_months).replace('-','')

url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start={0}&end={1}".format(query_start_date,query_end_date)

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'html.parser')

div = soup.find_all('div', attrs={'class':'cmc-table__table-wrapper-outer'})

table = div[2].find('table')

table_body = table.find('tbody')

rows = table_body.find_all('tr')

historical_list = []

for row in rows:
    cells = row.find_all('td')
    date = cells[0].find(text=True)
    c_open = str(cells[1].find(text=True)).replace(',','')
    high = cells[2].find(text=True)
    low = cells[3].find(text=True)
    close = cells[4].find(text=True)
    volume = cells[5].find(text=True)
    market_cap = cells[6].find(text=True)
  
    
    historical_data = { 'date':date , 'price_open': c_open, 'high': high, 'low': low, 'close': close,'volume':volume,'market_cap':market_cap}
    
    historical_list.append(historical_data)
    
    
def get_3_month_bitcoin_historical_data():
    return historical_list[::-1];



    