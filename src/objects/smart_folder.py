
from datetime import datetime
from typing import List


class SmartFolder(object):
    """
    docstring
    """

    def __init__(self, id: str, icon: str, name: str, description: str, modificationTime: datetime, conditions):
        """
        docstring
        """
        self._id: str = id
        self._icon: str = icon
        self._name: str = name
        self._description: str = description
        self._modification_time: datetime = modificationTime
        self._conditions = conditions

    @property
    def id(self) -> str:
        """
        return folder's id
        """
        return self._id

    @property
    def icon(self) -> str:
        """
        return folder's icon
        """
        return self._icon

    @property
    def name(self) -> str:
        """
        return folder's name
        """
        return self._name

    @property
    def description(self) -> str:
        """
        return folder's description
        """
        return self._description

    @property
    def modification_time(self) -> datetime:
        """
        return folder's modification_time
        """
        return self._modification_time
