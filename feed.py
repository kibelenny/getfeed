from bs4 import BeautifulSoup
import requests

class Feed:

    def __init__(self, link) -> None:
        self.headers = {
            'User-Agent': 'Chrome/97.0.4692.71'
        }
        try:
            self.request = requests.get(link, self.headers)
        except Exception as e:
            print('Error fetching the URL: ', link)
            print(e)
        try:
            self.soup = BeautifulSoup(self.request.text, 'html.parser')
        except Exception as e:
            print('Could not parse the xml: ', self.url)
            print(e)
            
    def get_rss(self):
        rss_get = self.soup.find('link', type='application/rss+xml')
        if rss_get:
            rss_get = rss_get.get('href')
            return rss_get
        else: return None

    def get_atom(self):
        atom_get = self.soup.find('link', type='application/atom+xml')
        if atom_get:
            atom_get = atom_get.get('href')
            return atom_get
        else: return None
    def get_feed(self):
        rss = self.get_rss()
        atom = self.get_atom()
        return rss, atom
