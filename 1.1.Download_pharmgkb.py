""""
Download PharmGKB data files.
"""
import logging
import time
import requests


class PharmGKB_arthiritis_downloader:
    def __init__(self):
        self.base_url = "https://api.pharmgkb.org/v1"
        self.headers = {
            'Accept' : 'application/json',
            'User-Agent' : 'PharmGKB-RA-Extractor/1.0'
        }
        self.disease_term = "rheumatoid arthiritis"
        self.rate_limit_delay = 0.6

        #Storage for results
        self.results = {
            'pathway':
        }

    def make_request(self):
        url = f"{self.base_url}"
        try:
            time.sleep(self.rate_limit_delay)
        except:
            requests.exceptions.RequestException as e:




