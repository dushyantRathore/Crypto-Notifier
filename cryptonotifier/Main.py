import notify2
import Rates


def notify():

    icon_path = "/home/dushyant/Desktop/Github/Crypto-Notifier/logo.jpg"

    bitcoin = Rates.fetch_coin('bitcoin')
    ethereum = Rates.fetch_coin('ethereum')
    litecoin = Rates.fetch_coin('litecoin')
    monero = Rates.fetch_coin('monero')
    ripple = Rates.fetch_coin('ripple')
    dash = Rates.fetch_coin('dash')

    result = ""
    result = result + str(bitcoin[0]) + "  -  " + str(bitcoin[2].encode('utf-8')) + "\n"
    result = result + str(ethereum[0]) + "  -  " + str(ethereum[2].encode('utf-8')) + "\n"
    result = result + str(litecoin[0]) + "  -  " + str(litecoin[2].encode('utf-8')) + "\n"
    result = result + str(monero[0]) + "  -  " + str(monero[2].encode('utf-8')) + "\n"
    result = result + str(ripple[0]) + "  -  " + str(ripple[2].encode('utf-8')) + "\n"
    result = result + str(dash[0]) + "  -  " + str(dash[2].encode('utf-8')) + "\n"

    print result

    notify2.init("Cryptocurrency rates notifier")
    n = notify2.Notification("Crypto Notifier", icon=icon_path)
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(1000)
    n.update("Current Rates", result)
    n.show()


if __name__ == "__main__":
    notify()
