from bs4 import BeautifulSoup
import requests


def fetch_coin(coin):
    url = "https://www.coingecko.com/en/price_charts/"+coin+"/inr"
    headers = {'User-Agent': 'Mozilla/5.0'}
    crypto_file = requests.get(url)
    soup = BeautifulSoup(crypto_file.text, "html.parser")

    crypto_li = []

    for table in soup.find_all("table", attrs={"class" : "table"}):
        for td in table.find_all("td"):
            crypto_li.append(td.text)

    del crypto_li[3:]
    crypto_li = map(lambda s : s.strip(), crypto_li)

    print crypto_li

    return crypto_li
