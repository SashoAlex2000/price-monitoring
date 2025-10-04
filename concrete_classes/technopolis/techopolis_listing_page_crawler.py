import random
import time

import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from concrete_classes.technopolis.techopolis_item_category import TechnopolisSubItemCategory
from selenium_classes.base_selenium_webdriver_setuper import BaseSeleniumWebdriverSetuper
from selenium_classes.page_saver_selenium import PageSaverSelenium


class TechnopolisListingPageCrawler:

    """
    Class for crawling the Technopolis listing pages for a specific subcategory
    """

    __MAIN_URL_FRAGMENT: str = "https://www.technopolis.bg/bg/"

    def __init__(self, path_to_save_dir: str, technopolis_sub_category: TechnopolisSubItemCategory):

        """

        :param path_to_save_dir: str, (valid) abs path to the local file save dir
        :param technopolis_sub_category: instance of TechnopolisSubItemCategory, used to specify the exact crawl
        """

        self._subcategory: TechnopolisSubItemCategory = technopolis_sub_category
        self._path_to_save_dir: str = path_to_save_dir

        self._base_selenium_webdriver_setuper: BaseSeleniumWebdriverSetuper = BaseSeleniumWebdriverSetuper()
        self._page_saver: PageSaverSelenium = PageSaverSelenium()

        self._main_driver: selenium.webdriver.Chrome = self._base_selenium_webdriver_setuper.get_base_pycharm_chrome_driver()

    def crawl_pages_till_last(self) -> None:

        """Crawl the instance's subcategory listing pages until the last page is reached.
        Save the HTMLs in the instance's directory
        """

        current_page: int = 0  # the first page when the URLs are build like that is actually 0
        while True:

            url_current: str = self.__generate_url(page_number=current_page)
            self._main_driver.get(url_current)
            time.sleep(random.uniform(5, 9))
            print(f"-- Current page is: {current_page}")

            if current_page == 0:
                self._accept_cookies()
                time.sleep(random.uniform(3, 5))
                print(f"-- Cookies accepted!")

            fl_save_name_current: str = self._get_file_save_name(current_page=current_page)
            abs_path: str = rf"{self._path_to_save_dir}/{fl_save_name_current}.html"
            self._page_saver.save_page_source_as_html(
                page_source=self._main_driver.page_source,
                abs_path_for_file_saving=abs_path,
            )

            is_there_next_page: bool = self._is_next_page_button_present()

            if not is_there_next_page:
                break

            current_page += 1

        print(f"{self.__class__.__name__} finished crawling - quitting driver!")
        self._main_driver.quit()

    def _accept_cookies(self) -> None:

        """Get the `Accept All Cookies` button by ID and click it.
        """

        accept_all_cookies_button = self._main_driver.find_element(
            By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"
        )
        accept_all_cookies_button.click()

    def _is_next_page_button_present(self) -> bool:

        """Check if there is a clickable next page button, to determine whether to continue the crawl
        """

        try:
            next_page_button = self._main_driver.find_element(By.CLASS_NAME, "next")

            if "disabled" in next_page_button.get_attribute("class"):
                # In bigger categories, in the last page, the button is disabled. Check it in the class name
                print("Next Page Button is Disabled!!!")
                return False

            print("Next page button found!")
            return True
        except NoSuchElementException:  # If there is just one page for a smaller category - button does not exist
            print("There is no next page button! Stopping the crawl!")
            return False

    def _get_file_save_name(self, current_page: int) -> str:

        """
        """

        fl_save_name: str = f"techonopolis-listing-page-{self._subcategory.category_name}-page-{str(current_page)}"
        return fl_save_name

    def __generate_url(self, page_number: int) -> str:

        """Get the listing URL for the current sub-category depending on the given page
        """

        url: str = (f"{self.__MAIN_URL_FRAGMENT}"
                    f"{self._subcategory.parent.category_name}/"
                    f"{self._subcategory.category_name}"
                    f"/c/"
                    f"{self._subcategory.category_number}"
                    f"?pageSize=90"  # In order to craw less pages, use the provided max number of items per page
                    f"&currentPage={str(page_number)}")
        return url
        