import notify2
import Rates


def notify():

    icon_path = "/home/dushyant/Desktop/Github/Crypto-Notifier/logo.jpg"

    cryptocurrencies = ["bitcoin",
                        "ethereum",
                        "litecoin",
                        "monero",
                        "ripple",
                        "dash"]
    
    result = ""
    
    for coin in cryptocurrencies:
        rate = Rates.fetch_coin(coin)
        result += "{} - {}\n".format(rate[0], rate[2].encode('utf-8'))

    print result

    notify2.init("Cryptocurrency rates notifier")
    n = notify2.Notification("Crypto Notifier", icon=icon_path)
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(1000)
    n.update("Current Rates", result)
    n.show()


if __name__ == "__main__":
    notify()
