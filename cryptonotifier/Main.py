import notify2
import Rates


def notify():

    icon_path = "/home/dushyant/Desktop/Github/Crypto-Notifier/logo.jpg"

    bitcoin = Rates.fetch_bitcoin()
    ethereum = Rates.fetch_ethereum()
    litecoin = Rates.fetch_litecoin()
    monero = Rates.fetch_monero()

    result = ""
    result = result + str(bitcoin[0]) + "  -  " + str(bitcoin[2].encode('utf-8')) + "\n"
    result = result + str(ethereum[0]) + "  -  " + str(ethereum[2].encode('utf-8')) + "\n"
    result = result + str(litecoin[0]) + "  -  " + str(litecoin[2].encode('utf-8')) + "\n"
    result = result + str(monero[0]) + "  -  " + str(monero[2].encode('utf-8')) + "\n"

    # Notification Tool

    # print result

    notify2.init("Cryptocurrency rates notifier")
    n = notify2.Notification("Crypto Notifier", icon=icon_path)
    n.update("Current Rates", result)
    n.show()


if __name__ == "__main__":
    notify()