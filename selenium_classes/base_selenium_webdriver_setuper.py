import selenium
from selenium import webdriver


class BaseSeleniumWebdriverSetuper():

    """
        Class for abstracting the creation of selenium drivers
    """

    def get_base_pycharm_chrome_driver(self) -> selenium.webdriver.Chrome:

        """The raw Chrome driver does not seem to work with Pycharm. It closes automatically after fetching the page.
        This may not be the desired behaviour at all cases.

        The driver returned is visible (i.e. not headless) and maximized.

        The driver has to manually be closed to not clog the RAM with `.quit()`

        :return: Chrome webdriver which works in Pycharm.
        """

        options = webdriver.ChromeOptions()

        options.add_argument('--start-maximized')
        # remove the `Select Default Browser` popup
        # https://stackoverflow.com/questions/78951935/selenium-chromedriver-asking-to-set-default-search-engine-on-startup
        options.add_argument('--disable-search-engine-choice-screen')

        # This is what makes the webdriver work in PyCharm
        options.add_experimental_option(
            name='detach',
            value=True,
        )

        chrome_webdriver: selenium.webdriver.Chrome = selenium.webdriver.Chrome(options=options)
        return chrome_webdriver
