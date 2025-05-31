""""
Download PharmGKB data files.
"""
import logging

#Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PGX_DBDownloader:
    def __init__(self, data_dir):
        
