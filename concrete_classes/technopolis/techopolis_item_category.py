

class TechnopolisMainItemCategory:

    """
    Class representing a main category in the Technopolis website, e.g. TV, Audio and Gaming
    """

    def __init__(self, category_name: str, category_number: str):

        self.__category_name: str = category_name
        self.__category_number = category_number

    @property
    def category_name(self) -> str:
        """
        :return: str, tne string name as it is in the website
        """
        return self.__category_name

    @property
    def category_number(self) -> str:
        """
        :return: str, the specific, associated string for the specific category as it is in the website for the
        """
        return self.__category_number


class TechnopolisSubItemCategory:

    """
    Class representing a Technopolis Subcategory, e.g. TVs
    """

    def __init__(self, category_name: str, category_number: str,
                 parent: TechnopolisMainItemCategory):

        self.__category_name: str = category_name
        self.__category_number = category_number
        self.__parent: TechnopolisMainItemCategory = parent

    @property
    def category_name(self) -> str:
        """
        :return: str, tne string name as it is in the website
        """
        return self.__category_name

    @property
    def category_number(self) -> str:
        """
        :return: str, the specific, associated string for the specific category as it is in the website for the
        """
        return self.__category_number

    @property
    def parent(self) -> TechnopolisMainItemCategory:
        """
        :return: instance of TechnopolisMainItemCategory representing the parent of the Subcategory
        """
        return self.__parent
