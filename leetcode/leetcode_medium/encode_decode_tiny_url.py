"""
Leetcode 535: Encode and Decode TinyURL

TinyURL is a URL shortening service where you enter a URL
such as https://leetcode.com/problems/design-tinyurl
and it returns a short URL such as http://tinyurl.com/4e9iAk.
Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL
can be decoded to the original URL.

Implement the Solution class:
- Solution() Initializes the object of the system.
- String encode(String longUrl) Returns a tiny URL for the given longUrl.
- String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
"""

import base64


class Codec:
    def __init__(self):
        self.url_to_id = {}
        self.id_to_url = {}
        self.next_id = 1

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.url_to_id:
            short_id = str(self.next_id)
            self.next_id += 1

            self.url_to_id[longUrl] = short_id
            self.id_to_url[short_id] = longUrl

        return "https://tinyurl.com/" + self.url_to_id[longUrl]

    def decode(self, shortUrl: str) -> str:
        short_id = shortUrl.rsplit("/", 1)[-1]
        return self.id_to_url[short_id]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
