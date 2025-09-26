import os
from typing import Any

from file_workers.file_action import FileAction


class BaseFileTraverser:

    """
    Base class for traversing local files

    """

    def __init__(self, abs_path_to_dir: str, file_action: FileAction):

        """

        :param abs_path_to_dir: str, (valid) abs path to the desired local directory for traversal
        :param file_action: concrete child of FileActions with the desired functionality implemented
        """

        self._abs_path_to_dir: str = abs_path_to_dir
        self._file_action: FileAction = file_action

    def traverse_files_and_perform_action(self) -> list[Any]:

        """Derive all the paths to files in the desired directory.

        Traverse them and call `perform_action_on_file` method of the FileAction instance
        on each one of them

        If there is any result different from None - append it to return list

        :return: list, containing the return values (if such exist) of perform_action_on_file from each file
        """

        repo_of_results: list = []

        all_fl_names_in_dir: list[str] = os.listdir(self._abs_path_to_dir)

        fl_name_current: str  # File extension is included in the return value of os.listdir
        for fl_name_current in all_fl_names_in_dir:

            path_current: str = rf"{self._abs_path_to_dir}/{fl_name_current}"

            res_from_action: Any | None = self._file_action.perform_action_on_file(
                path_to_file=path_current
            )

            if res_from_action is not None:  # Append the result only if it is not None
                repo_of_results.append(res_from_action)

        return repo_of_results
