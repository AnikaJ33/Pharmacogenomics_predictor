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
            'clinical annotations' : [],
            'variant annotations' : [],
            'drug labels' : [],
            'pathways' : [],
            'genes' : [],
            'variants' : []
        }

    def make_request(self,endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            print(f"Requesting: {url} with params: {params}")
            time.sleep(self.rate_limit_delay)

            response = requests.get(url, headers=self.headers, params=params, timeout=30)

            if response.status_code == 200:
                data = response.json()
                print(f"Success: Found data")
                return data
            elif response.status_code == 429:
                print("Rate limit hit, waiting 5 seconds")
                time.sleep(5)
                return self.make_request(endpoint, params)
            else:
                print(f"Failed : {response.status_code}")
                return None

        except Exception as e:
            print(f"Error: {str(e)}")
            return None

def main():
    extractor = PharmGKB_arthiritis_downloader()
    
if __name__ == "__main__":
    main()

