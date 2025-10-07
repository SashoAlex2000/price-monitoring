import bs4


class TechnopolisListingParser:

    __URL_FRAGMENT: str = "https://www.technopolis.bg"

    """
    Class for parsing the downloaded listing pages of Technopolis
    """

    def parse_technopolis_listing_soup(self, listing_soup: bs4.BeautifulSoup) -> list[dict]:

        """

        :param listing_soup:bs4.BeautifulSoup representation of the listing page HTML
        :return: list of dicts, where each dict is a parsed item
        """

        extracted_results: list[dict] = []

        ul_grid_list_holder: bs4.Tag = listing_soup.find(
            "ul",
            attrs={
                "class": "products-grid-list"
            }
        )

        all_li_elements: list[bs4.Tag] = ul_grid_list_holder.find_all(
            "li",
            attrs={
                "class": "list-item"
            },
        )

        single_li_element: bs4.Tag
        for single_li_element in all_li_elements:

            parsed_info: dict = self._parse_single_li_item_info(li_element=single_li_element)
            extracted_results.append(parsed_info)

        return extracted_results

    def _parse_single_li_item_info(self, li_element: bs4.Tag) -> dict[str, str]:

        """
        """

        parsed_res: dict = {}

        # -- Top panel contains the picture

        # -- Middle panel
        middle_panel: bs4.Tag = li_element.find('div', attrs={'class': 'product-box__middle'})

        # This is an <a> tag inside <h3> tag - it holds the title as text, and the link to individual item
        name_anchor: bs4.Tag = middle_panel.find("a", attrs={'class': 'product-box__title-link'})
        url_bit: str = name_anchor.get('href')
        full_url: str = self._build_full_url(url_fragment=url_bit)
        parsed_res['product_url'] = full_url
        extracted_id: str = self._extract_item_id(url_fragment=url_bit)
        parsed_res['product_id'] = extracted_id

        parsed_res['product_title'] = name_anchor.text

        # Bottom Panel
        is_discounted: bool = False
        bottom_panel: bs4.Tag = li_element.find("div", attrs={"class": "product-box__bottom"})

        panel_price: bs4.Tag = bottom_panel.find('te-price')

        if panel_price is None:
            # If there is a discount - the name of the element is different
            panel_price = bottom_panel.find('te-save-price')
            is_discounted = True

        # In the regular items: There are 2 prices - one in BGN, the other in EUR - get both
        # In the discounted there are 3 prices - the first one is the discounted in BGN
        price_panels: list[bs4.Tag] = panel_price.find_all("span", attrs={'class': 'price'})
        if not is_discounted:
            regular_price_lv: str = ''
            lv_price: str = price_panels[0].text
            eur_price: str = price_panels[1].text
        else:
            regular_price_lv: str = price_panels[0].text
            lv_price: str = price_panels[1].text
            eur_price: str = price_panels[2].text

        parsed_res['is_discounted'] = 1 if is_discounted else 0

        parsed_res['lv_price'] = lv_price
        parsed_res['eur_price'] = eur_price
        parsed_res['regular_price_lv'] = regular_price_lv

        return parsed_res

    def _build_full_url(self, url_fragment: str) -> str:

        """Build the URL for the detailed page for a given item
        """

        full_url: str = f"{self.__URL_FRAGMENT}{url_fragment}"
        return full_url

    def _extract_item_id(self, url_fragment: str) -> str:

        """Extract the last bit of the URL fragment, which (seems that it) contains unique IDs of items
        """

        try:

            shred: list[str] = url_fragment.split('/')
            return shred[-1]

        except Exception as ex:
            print(f"{self.__class__.__name__} encountered an error extracting the product ID from: {url_fragment}")
            return ''
