import notify2
import requests
from bs4 import BeautifulSoup


def fetch_coin(coin, fiat):
    url = "https://www.coingecko.com/en/price_charts/"+coin+"/"+fiat
    headers = {'User-Agent': 'Mozilla/5.0'}
    crypto_file = requests.get(url)
    soup = BeautifulSoup(crypto_file.text, "html.parser")

    crypto_li = []

    for table in soup.find_all("table", attrs={"class" : "table"}):
        for td in table.find_all("td"):
            crypto_li.append(td.text)

    del crypto_li[3:]
    crypto_li = list(map(lambda s : s.strip(), crypto_li))

    # print crypto_li

    return crypto_li


def notify():

    icon_path = "/home/dushyant/Desktop/Github/Crypto-Notifier/logo.jpg"

    cryptocurrencies = ["bitcoin",
                        "ethereum",
                        "litecoin",
                        "monero",
                        "ripple",]
    
    result = ""
    
    for coin in cryptocurrencies:
        rate = fetch_coin(coin, "usd")
        result += "{} , {} - {}\n".format(coin, rate[1].encode('utf-8'), rate[2].encode('utf-8'))

    # print result

    notify2.init("Cryptocurrency rates notifier")
    n = notify2.Notification("Crypto Notifier", icon=icon_path)
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(1000)
    n.update("Current Rates", result)
    n.show()


if __name__ == "__main__":
    notify()
