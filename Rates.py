from bs4 import BeautifulSoup
import urllib2
import requests


def fetch_bitcoin():
    url = "https://www.coingecko.com/en/price_charts/bitcoin/inr"
    headers = {'User-Agent': 'Mozilla/5.0'}
    bitcoin_file = requests.get(url)
    soup = BeautifulSoup(bitcoin_file.text, "html.parser")

    bitcoin_li = []

    for table in soup.find_all("table", attrs={"class" : "table"}):
        for td in table.find_all("td"):
            bitcoin_li.append(td.text)

    del bitcoin_li[3:]
    bitcoin_li = map(lambda s : s.strip(), bitcoin_li)
    return bitcoin_li


def fetch_ethereum():
    url = "https://www.coingecko.com/en/price_charts/ethereum/inr"
    headers = {'User-Agent': 'Mozilla/5.0'}
    ethereum_file = requests.get(url)
    soup = BeautifulSoup(ethereum_file.text, "html.parser")

    ethereum_li = []

    for table in soup.find_all("table", attrs={"class": "table"}):
        for td in table.find_all("td"):
            ethereum_li.append(td.text)

    del ethereum_li[3:]
    ethereum_li = map(lambda s : s.strip(), ethereum_li)
    return ethereum_li


def fetch_litecoin():
    url = "https://www.coingecko.com/en/price_charts/litecoin/inr"
    headers = {'User-Agent': 'Mozilla/5.0'}
    litecoin_file = requests.get(url)
    soup = BeautifulSoup(litecoin_file.text, "html.parser")

    litecoin_li = []

    for table in soup.find_all("table", attrs={"class": "table"}):
        for td in table.find_all("td"):
            litecoin_li.append(td.text)

    del litecoin_li[3:]
    litecoin_li = map(lambda s : s.strip(), litecoin_li)
    return litecoin_li


def fetch_monero():
    url = "https://www.coingecko.com/en/price_charts/monero/inr"
    headers = {'User-Agent': 'Mozilla/5.0'}
    monero_file = requests.get(url)
    soup = BeautifulSoup(monero_file.text, "html.parser")

    monero_li = []

    for table in soup.find_all("table", attrs={"class": "table"}):
        for td in table.find_all("td"):
            monero_li.append(td.text)

    del monero_li[3:]
    monero_li = map(lambda s : s.strip(), monero_li)
    return monero_li

fetch_bitcoin()