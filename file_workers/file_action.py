from abc import ABC, abstractmethod
from typing import Any


class FileAction(ABC):

    """
    Abstract Base Class, providing a reliable blueprint method for working with files
    """

    def __init__(self):
        pass

    @abstractmethod
    def perform_action_on_file(self, path_to_file: str,) -> Any | None:

        """
        :param path_to_file: str, (valid) abs path to a local file
        :return: Any or None -> up to the concrete implementation of a concrete child class
        """

        pass
