import sys

sys.path.insert(0, "/Volumes/SSD/Repos/TikTok-Content-Scraper")

from TT_Content_Scraper import TT_Content_Scraper

scraper = TT_Content_Scraper(
    wait_time=0.5,
    output_files_fp="mistyway_data/",
    progress_file_fn="mistyway_data/progress.db",
    clear_console=False,
)

# MistyWay TikTok accounts
accounts = [
    "user3480772213181",
    "user3142033133840",
    "john.brown.161",
    "johnbmepwq2",
    "user9818735618885",
    "karder.grand",
]

# Add users for scraping
scraper.add_objects(ids=accounts, title="mistyway_accounts", type="user")

# Scrape metadata only (no video files)
scraper.scrape_pending(scrape_files=False)
