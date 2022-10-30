
from datetime import datetime
from typing import List, Optional

from ..base_class import EagleAPI


class Folder(object):
    """
    docstring
    """

    def __init__(self, api: EagleAPI, id: str, name: str, description: str, modificationTime: datetime, imageCount: int,  tags: List[str] = [], pinyin: Optional[str] = None, extendTags: List[str] = [], children: List["Folder"] = []):
        """
        docstring
        """
        self._api = api
        self._id: str = id
        self._name: str = name
        self._description: str = description
        self._modification_time: datetime = modificationTime
        self._image_count: int = imageCount
        self._pinyin: Optional[str] = pinyin
        self._tags: List[str] = tags
        self._extend_tags: List[str] = extendTags
        self._children: List["Folder"] = children

    @property
    def id(self) -> str:
        """
        return folder's id
        """
        return self._id

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

    @property
    def image_count(self) -> int:
        """
        return folder's image_count
        """
        return self._image_count

    @property
    def pinyin(self) -> Optional[str]:
        """
        return folder's pinyin
        """
        return self._pinyin

    @property
    def tags(self) -> List[str]:
        """
        return folder's tags
        """
        return self._tags

    @property
    def extend_tags(self) -> List[str]:
        """
        return folder's extend_tags
        """
        return self._extend_tags

    @property
    def children(self) -> List["Folder"]:
        """
        return folder's children
        """
        return self._children
