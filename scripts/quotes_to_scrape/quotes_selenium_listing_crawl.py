# ------------- Imports

from concrete_classes.quotes_to_scrape.quotes_selenium_listing_crawler import QuotesToScrapeSeleniumCrawler

# ------------- DOCS
"""
Test the functionality for crawling the Quotes Website 
"""

# ------------- Setup

# This is relative for now, until a class for doing abs paths is created TODO
_PATH_TO_SAVE_DIR: str = '../../output/quotes_to_scrape_output'

quotes_selenium_crawler: QuotesToScrapeSeleniumCrawler = QuotesToScrapeSeleniumCrawler(
    abs_path_to_dir_for_saving=_PATH_TO_SAVE_DIR,
)

quotes_selenium_crawler.craw_pages_in_range(
    end_page=10,
)
