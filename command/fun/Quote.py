import json
import random
import urllib.request
from threading import Timer

from util.Util import try_send


class Quote:
    refresh_time = 3600
    def __init__(self, logging):
        self.logging = logging
        with open('quotes.json') as json_file:
            self.quotes = json.load(json_file)
        Timer(self.refresh_time, self.refresh_quotes, ()).start()

    def refresh_quotes(self):
        self.logging.info("refreshing quotes")
        with urllib.request.urlopen("https://raw.githubusercontent.com/nugroho-s/jahyadi/master/quotes.json") as url:
            self.quotes = json.loads(url.read().decode())
            self.logging.info(self.quotes)
        Timer(self.refresh_time, self.refresh_quotes, ()).start()

    async def do_response(self, message, args):
        await try_send(message.channel, random.choice(self.quotes))
