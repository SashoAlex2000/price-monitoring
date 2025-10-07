# ------------- Imports
import os

import bs4
import pandas as pd
from datetime import date

from concrete_classes.technopolis.technopolis_listing_parser import TechnopolisListingParser
from file_workers.base_file_traverser import BaseFileTraverser
from file_workers.open_html_with_bs_file_action import OpenHTMLWithBSFileAction

# ------------- Docs
"""
Script for parsing the Technopolis listing files in a given directory
"""

# ------------- Setup

_PATH_TO_BASE_TECHO_DIR: str = '../../output/technopolis'

YEAR: int = 2025
MONTH: int = 10
DAY: int = 4

DATE_OBJECT: date = date(year=YEAR, month=MONTH, day=DAY)

_CURRENT_DAY_DIR: str = rf"{_PATH_TO_BASE_TECHO_DIR}/{DATE_OBJECT}"

_PARSED_LISTING_FL_NAME: str = f"technopolis_all_parsed_listings-{DATE_OBJECT}"
_ABS_PATH_TO_PARSED_FL: str = rf"{_CURRENT_DAY_DIR}/{_PARSED_LISTING_FL_NAME}.csv"

if not os.path.isdir(_CURRENT_DAY_DIR):
    print("-- Creating save dir!")
    os.makedirs(_CURRENT_DAY_DIR)
else:
    print("-- Save path already exists!")

if not os.path.isfile(_ABS_PATH_TO_PARSED_FL):

    print("Technopolis Listing file does not exist - parsing!")

    technopolis_parser: TechnopolisListingParser = TechnopolisListingParser()

    open_selenium_file_action: OpenHTMLWithBSFileAction = OpenHTMLWithBSFileAction()

    # > Main
    base_file_traverser: BaseFileTraverser = BaseFileTraverser(
        abs_path_to_dir=_CURRENT_DAY_DIR,
        file_action=open_selenium_file_action
    )

    soups: list[bs4.BeautifulSoup] = base_file_traverser.traverse_files_and_perform_action()

    all_parsed_listing: list[dict] = []

    soup_to_parse: bs4.BeautifulSoup
    for soup_to_parse in soups:

        current_parse_res: list[dict] = technopolis_parser.parse_technopolis_listing_soup(
            listing_soup=soup_to_parse,
        )
        all_parsed_listing.extend(current_parse_res)

    df_parsed_listing: pd.DataFrame = pd.DataFrame(
        data=all_parsed_listing
    )

    print(df_parsed_listing)

    df_parsed_listing.to_csv(
        path_or_buf=_ABS_PATH_TO_PARSED_FL,
        encoding='utf-8',
        sep=',',
        index=False,
    )

else:
    print(f"-- Technopolis parsed listing file already exists here: \n {_ABS_PATH_TO_PARSED_FL}")
