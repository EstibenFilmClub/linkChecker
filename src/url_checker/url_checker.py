#url_checker.py
import re

class URLChecker:
    def is_youtube_url(self, url):
        return re.match(r'https?://www\.youtube\.com/watch\?v=', url) is not None
    def is_netflix_url(self, url):
        return re.match(r'https?://media\.netflix\.com/', url) is not None