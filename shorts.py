import hashlib


class URLShortener:

     def __init__(self):
         self.long_to_short = {}
         self.short_to_long = {}
         self.base_url = "short.ly/"


    def shorten_url(self, long_url: str)-> str:
        if long_url in self.long_to_short:
            return self.long_to_short[long_url]


    while short_url in self.short_to_long:
        short_hash = hashlib.md5((long_url + short_hash).encode()).hexdigest()[:6]
        short_url = self.base_url + short_hash


    self.long_to_short[long_url]=short_url
    self.short_to_long[short_url]=long_url


    return short_url
