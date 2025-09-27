import bs4
from bs4 import BeautifulSoup

from file_workers.file_action import FileAction


class OpenHTMLWithBSFileAction(FileAction):

    __DEFAULT_PARSER: str = 'html.parser'

    def __init__(self, parser: str | None = None):

        """

        :param parser: str | None, the type of parser used,  if None - default to `html.parser`
        """

        super().__init__()

        self._parser_type: str = parser if parser is not None else self.__DEFAULT_PARSER


    def perform_action_on_file(self, path_to_file: str) -> bs4.BeautifulSoup:

        """
        :param path_to_file: str, (valid) abs path to a local file
        :return: bs4.BeautifulSoup representation of the local HTML file opened
        """

        with open(path_to_file, encoding='utf-8') as fl_in:
            soup: bs4.BeautifulSoup = BeautifulSoup(fl_in, self._parser_type)

        return soup
