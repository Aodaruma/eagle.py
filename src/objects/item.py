from typing import Dict, List, Optional, Tuple
from datetime import datetime

from ..base_class import EagleAPI

from .pallete import EaglePallete


class Item(object):
    """
    docstring
    """

    def __init__(self, api: EagleAPI, id: str, name: str,  modificationTime: datetime, size: int, isDeleted: bool, width: int, height: int, noThumbnail: bool, lastModified: datetime, tags: List[str] = [], folders: List[str] = [], website: Optional[str] = None, annotation: Optional[str] = None, palletes: List[EaglePallete] = []):
        """
        docstring
        """
        self._api = api
        self._id: str = id
        self._name: str = name
        self._size: int = size
        self._modification_time: datetime = modificationTime
        self._is_deleted: bool = isDeleted
        self._width: int = width
        self._height: int = height
        self._no_thumbnail: bool = noThumbnail
        self._last_modified: datetime = lastModified
        self._folders: List[str] = folders
        self._tags: List[str] = tags
        self._website: Optional[str] = website
        self._annocation: Optional[str] = annotation
        self._palletes: List[EaglePallete] = palletes

    @property
    def id(self) -> str:
        """
        return item's id
        """
        return self._id

    @property
    def name(self) -> str:
        """
        return item's name
        """
        return self._name

    @property
    def size(self) -> int:
        """
        return item's size
        """
        return self._size

    @property
    def modification_time(self) -> datetime:
        """
        return item's modification time
        """
        return self._modification_time

    @property
    def is_deleted(self) -> bool:
        """
        return item's is_deleted
        """
        return self._is_deleted

    @property
    def shape(self) -> Tuple[int, int]:
        """
        return item's width and height
        """
        return (self._width, self._height)

    @property
    def no_thumbnail(self) -> bool:
        """
        return item's no_thumbnail
        """
        return self._no_thumbnail

    @property
    def last_modified(self) -> datetime:
        """
        return item's last_modified
        """
        return self._last_modified

    @property
    def folders(self) -> List[str]:
        """
        return item's folders
        """
        return self._folders

    @property
    def tags(self) -> List[str]:
        """
        return item's tags
        """
        return self._tags

    @property
    def website(self) -> Optional[str]:
        """
        return item's website
        """
        return self._website

    @property
    def annocation(self) -> Optional[str]:
        """
        return item's annocation
        """
        return self._annocation

    @property
    def palletes(self) -> List[EaglePallete]:
        """
        return item's pallete
        """
        return self._palletes
