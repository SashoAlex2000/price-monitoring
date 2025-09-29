import bs4


class QuotesListingParser:

    """
    Class for parsing the Quotes listing pages
    """

    def parse_quotes_listing_soup(self, quotes_soup: bs4.BeautifulSoup) -> list[dict]:

        """

        :param quotes_soup: bs4.BeautifulSoup object representing a quotes HTML
        :return: list of dicts, where each dict contains the parsed information for quote
        """

        extracted_results: list[dict] = []

        div_holders: list[bs4.Tag] = quotes_soup.find_all("div", class_="quote")

        single_div: bs4.Tag
        for single_div in div_holders:

            text_of_quote: bs4.Tag = single_div.find(
                "span",
                attrs={"class": "text"}
            )
            author_name: bs4.Tag = single_div.find(
                'small',
                attrs={'class': 'author'}
            )

            info_dict_current: dict[str, str] = {
                'quote': text_of_quote.text,
                'author': author_name.text
            }
            extracted_results.append(info_dict_current)

        return extracted_results
