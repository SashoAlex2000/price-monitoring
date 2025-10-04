from datetime import date
import sys
import os

from concrete_classes.technopolis.export_categories_for_crawl import export_categories_for_crawl
from concrete_classes.technopolis.techopolis_item_category import TechnopolisSubItemCategory
from concrete_classes.technopolis.techopolis_listing_page_crawler import TechnopolisListingPageCrawler

EXPORT_LIST: list[TechnopolisSubItemCategory] = export_categories_for_crawl()
_PATH_TO_SAVE_DIR: str = r"/home/aleksandarm/Desktop/price_monitoring/price-monitoring/output/technopolis/"

CURRENT_DATE: date = date.today()

_TODAY_SAVE_DIR: str = rf"{_PATH_TO_SAVE_DIR}/{str(CURRENT_DATE)}"

if not os.path.isdir(_TODAY_SAVE_DIR):
    print("-- Creating save dir!")
    os.makedirs(_TODAY_SAVE_DIR)
else:
    print("-- Save path already exists!")

category_to_crawl: TechnopolisSubItemCategory
for category_to_crawl in EXPORT_LIST:

    print(f"{category_to_crawl.category_name} "
          f"<> {category_to_crawl.category_number} "
          f"<> {category_to_crawl.parent.category_name}")

    current_crawler: TechnopolisListingPageCrawler = TechnopolisListingPageCrawler(
        path_to_save_dir=_TODAY_SAVE_DIR,
        technopolis_sub_category=category_to_crawl
    )

    current_crawler.crawl_pages_till_last()
