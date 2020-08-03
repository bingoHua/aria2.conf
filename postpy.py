import requests
url = "https://api.telegram.org/bot1258672142:AAFToNJKap-vYcS1wt7iBEk0vmo86O2bdBs/sendMessage?chat_id=520800871&text="
def main(c1):
    res = requests.get(url+c1)
