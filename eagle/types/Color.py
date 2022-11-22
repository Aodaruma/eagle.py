from typing import Tuple

from ..base_class import EagleAPI


class EaglePallete(object):
    """
    docstring
    """

    def __init__(self, api: EagleAPI, color: Tuple[int, int, int], ratio: int, hashkey: str):
        """
        docstring
        """
        self._api = api
        self._color: Tuple[int, int, int] = color
        self._ratio: int = ratio
        self._hashkey: str = hashkey

    @property
    def color(self) -> Tuple[int, int, int]:
        """
        docs
        """
        return self._color

    @property
    def ratio(self) -> int:
        """
        docs
        """
        return self._ratio

    @property
    def hashkey(self) -> str:
        """
        docs
        """
        return self._hashkey


class Color(object):
    """
    docstring
    """
    pass
