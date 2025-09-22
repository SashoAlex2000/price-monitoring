import random
import time

import selenium.webdriver
from selenium.webdriver.common.by import By

from selenium_classes.base_selenium_webdriver_setuper import BaseSeleniumWebdriverSetuper
from selenium_classes.page_saver_selenium import PageSaverSelenium


class QuotesToScrapeSeleniumCrawler:

    """
    Selenium Crawler for the `quotes to scrape` website.
    """

    # This is the start page for the Quotes website
    __QUOTES_STAR_URL: str = 'https://quotes.toscrape.com/page/1/'

    def __init__(self, abs_path_to_dir_for_saving: str):

        """
        :param abs_path_to_dir_for_saving: str, (valid) abs path to the directory for saving HTMLs
        """

        self._base_selenium_webdriver_setuper: BaseSeleniumWebdriverSetuper = BaseSeleniumWebdriverSetuper()
        self._page_saver: PageSaverSelenium = PageSaverSelenium()
        self._abs_path_to_dir_for_saving: str = abs_path_to_dir_for_saving

        self._main_driver: selenium.webdriver.Chrome = self._base_selenium_webdriver_setuper.get_base_pycharm_chrome_driver()

        # -- Setup
        self.__goto_start_url()

    def craw_pages_in_range(self, end_page: int, start_page: int | None = 1) -> None:

        """

        :param end_page: int, final page for the crawl
        :param start_page: int or None, start page of the crawl; if None - defaults to 1
        :return: None
        """

        current_page: int
        for current_page in range(start_page, end_page):

            print(f"-- {self.__class__.__name__} is downloading for {current_page} / {end_page}")
            fl_save_name_current: str = self._get_fl_save_name_for_current_page(current_page=current_page)

            abs_path_for_saving: str = rf"{self._abs_path_to_dir_for_saving}/{fl_save_name_current}.html"

            self._page_saver.save_page_source_as_html(
                page_source=self._main_driver.page_source,
                abs_path_for_file_saving=abs_path_for_saving,
            )

            time.sleep(random.uniform(0.1, 0.3))
            self._click_next_page_button(current_page=current_page)
            time.sleep(random.uniform(1, 3))

        self._main_driver.quit()  # After finishing the crawl - quit the driver

    def _click_next_page_button(self, current_page: int) -> None:

        """
        Click the button which takes the driver to the next page
        """

        # Dynamically build the class in order to locate the anchor for the next page
        next_page_button = self._main_driver.find_element(
            By.XPATH,
            f"//a[contains(@href, '/page/{str(current_page+1)}')]"
        )

        next_page_button.click()

    def _get_fl_save_name_for_current_page(self, current_page: int) -> str:

        """Get the current file save name depending on the current page of the crawl
        """

        fl_save_name: str  = f"quotes_to_scrape_page_{str(current_page)}"
        return fl_save_name


    def __goto_start_url(self) -> None:

        """
        Fetch the beginning page of the website using the instance's driver
        """

        self._main_driver.get(self.__QUOTES_STAR_URL)
