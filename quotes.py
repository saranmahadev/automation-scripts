import requests
from plyer import notification
def get_quote():
    """ Gets Quote From the Site """
    url = "https://zenquotes.io/api/random"
    resp = requests.get(url)
    quote = resp.json()[0]["q"]
    author = resp.json()[0]["a"]
    return quote,author

def send_quote():
    """ Sends Quote to the Desktop"""
    quote = get_quote()   
    notification.notify(title = quote[1] , message = quote[0], app_name = "Quote of the Day" )

if __name__ == '__main__':
    send_quote()
