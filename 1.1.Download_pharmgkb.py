""""
Download PharmGKB data files.
"""
import logging

#Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PharmGKB_arthiritis_downloader:
    def __init__(self):
        self.base_url = "https://api.pharmgkb.org/"


    def make_request(self):
        
        
