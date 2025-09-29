# ------------- Imports

import bs4
import pandas as pd

from concrete_classes.quotes_to_scrape.quotes_listing_parser import QuotesListingParser
from file_workers.base_file_traverser import BaseFileTraverser
from file_workers.open_html_with_bs_file_action import OpenHTMLWithBSFileAction

# ------------- Docs
"""
Script for testing the classes for parsing of local HTML files
"""

# ------------- Constants
_PATH_TO_QUOTES_DIR: str = '../../output/quotes_to_scrape_output'
_PATH_TO_DIR: str = '../../output/quotes_to_scrape_output'
_PARSED_FL_SAVE_NAME: str = 'parsed_quotes'

# > Main
open_selenium_file_action: OpenHTMLWithBSFileAction = OpenHTMLWithBSFileAction()

base_file_traverser: BaseFileTraverser = BaseFileTraverser(
    abs_path_to_dir=_PATH_TO_QUOTES_DIR,
    file_action=open_selenium_file_action,
)

listing_file_soups: list[bs4.BeautifulSoup] = base_file_traverser.traverse_files_and_perform_action()

quotes_listing_parser: QuotesListingParser = QuotesListingParser()

parsed_listings: list[dict] = []

soup_listing: bs4.BeautifulSoup
for soup_listing in listing_file_soups:

    current_res: list[dict] = quotes_listing_parser.parse_quotes_listing_soup(
        quotes_soup=soup_listing,
    )

    parsed_listings.extend(current_res)


df_parsed_listings: pd.DataFrame = pd.DataFrame(
    data=parsed_listings
)

print(df_parsed_listings)

df_parsed_listings.to_csv(
    path_or_buf=rf"{_PATH_TO_DIR}/{_PARSED_FL_SAVE_NAME}.csv",
    encoding='utf-8',
    sep=',',
    index=False,
)
