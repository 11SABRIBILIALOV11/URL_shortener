import hashlib

class URLShortener:
    def __init__(self):
        # Dictionaries to store the mappings
        self.long_to_short = {}
        self.short_to_long = {}
        self.base_url = "short.ly/"

    def shorten(self, long_url: str) -> str:
        # Check if the URL has already been shortened
        if long_url in self.long_to_short:
            return self.long_to_short[long_url]

        # Generate a unique short URL by hashing the long URL
        # Use a hash function to generate a deterministic but unique key
        short_hash = hashlib.md5(long_url.encode()).hexdigest()[:6]
        short_url = self.base_url + short_hash

        # Ensure the generated short URL is unique
        while short_url in self.short_to_long:
            short_hash = hashlib.md5((long_url + short_hash).encode()).hexdigest()[:6]
            short_url = self.base_url + short_hash

        # Store the mapping in both directions
        self.long_to_short[long_url] = short_url
        self.short_to_long[short_url] = long_url

        return short_url

    def redirect(self, short_url: str) -> str:
        # Check if the short URL exists in our mapping
        if short_url in self.short_to_long:
            return self.short_to_long[short_url]
        else:
            return "Error: Short URL not found."

# Example Usage
url_shortener = URLShortener()

# Shorten URLs
short1 = url_shortener.shorten("https://www.example.com/some/long/url")
print(short1)  # Outputs: short.ly/<some_hash>

short2 = url_shortener.shorten("https://www.another-example.com/different/url")
print(short2)  # Outputs: short.ly/<another_hash>

# Redirect URLs
long1 = url_shortener.redirect(short1)
print(long1)  # Outputs: https://www.example.com/some/long/url

long2 = url_shortener.redirect(short2)
print(long2)  # Outputs: https://www.another-example.com/different/url
