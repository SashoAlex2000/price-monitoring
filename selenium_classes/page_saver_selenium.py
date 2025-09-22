

class PageSaverSelenium:

    """
    Class providing reusable functionality for saving a webdriver page source as HTML locally.
    """

    def save_page_source_as_html(self, page_source: str,
                                 abs_path_for_file_saving: str) -> None:

        """
        :param page_source: str, the result of calling driver.page_source on a selenium driver
        :param abs_path_for_file_saving: str, (valid) abs path for saving the file, `.html` file extension included
        :return: None
        """

        with open(
            abs_path_for_file_saving,
            "w",
            encoding='utf-8',
        ) as fl_out:
            fl_out.write(page_source)
