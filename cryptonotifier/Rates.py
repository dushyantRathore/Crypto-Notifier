from bs4 import BeautifulSoup
import requests


def fetch_coin(coin):
    url = "https://www.coingecko.com/en/price_charts/"+coin+"/inr"
    headers = {'User-Agent': 'Mozilla/5.0'}
    bitcoin_file = requests.get(url)
    soup = BeautifulSoup(bitcoin_file.text, "html.parser")

    bitcoin_li = []

    for table in soup.find_all("table", attrs={"class" : "table"}):
        for td in table.find_all("td"):
            bitcoin_li.append(td.text)

    del bitcoin_li[3:]
    bitcoin_li = map(lambda s : s.strip(), bitcoin_li)
    print bitcoin_li
    return bitcoin_li
