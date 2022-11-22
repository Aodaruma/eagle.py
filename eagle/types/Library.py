from datetime import datetime
from typing import Dict, List

from ..base_class import EagleAPI

from .folder import Folder
from .smart_folder import SmartFolder
from .tags import TagGroups


class Library(object):
    """
    docstring
    """
    pass

    def __init__(self, api: EagleAPI, folders: List[Folder], smartFolders: List[SmartFolder], quickAccess: Dict[Folder, SmartFolder], tagGroups: List[TagGroups], modificationTime: datetime, applicationVersion: str):
        """
        docstring
        """
        self._api = api
        self._folders: List[Folder] = folders
        self._smart_folders: List[SmartFolder] = smartFolders
        self._quick_access: Dict[Folder, SmartFolder] = quickAccess
        self._tag_groups: List[TagGroups] = tagGroups
        self._modification_time: datetime = modificationTime
        self._application_version: str = applicationVersion

    @property
    def folders(self) -> List[Folder]:
        """
        return Library's folders
        """
        return self._folders

    @property
    def smart_folders(self) -> List[SmartFolder]:
        """
        return Library's smart folders
        """
        return self._smart_folders

    @property
    def quick_access(self) -> Dict[Folder, SmartFolder]:
        """
        return Library's quick access
        """
        return self._quick_access

    @property
    def tag_groups(self) -> List[TagGroups]:
        """
        return Library's tag_groups
        """
        return self._tag_groups

    @property
    def modification_time(self) -> datetime:
        """
        return Library's modification time
        """
        return self._modification_time

    @property
    def application_version(self) -> str:
        """
        return Library's application version
        """
        return self._application_version
