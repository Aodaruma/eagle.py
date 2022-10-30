from ctypes import Union
import json
from optparse import Option
from typing import Any, Dict, Optional, Tuple
import requests

from .objects.application import *
from .objects.folder import *
from .objects.item import *
from .objects.library import *
from .objects.pallete import *
from .objects.tags import *
from .objects.smart_folder import *


class EagleAPI(object):
    """
    docstring
    """
    pass

    request_url = "http://localhost"
    listening_port = 41195

    def __init__(self, request_url: str = "http://localhost", listening_port: int = 41195):
        """
        docstring
        """
        self.__req_url__: str = request_url
        self.__lis_port__: int = listening_port

    def _post(self, to_url: str, data: dict) -> Tuple[bool, Optional[Dict[str, Any]]]:
        """
        docstring
        """
        r = requests.post(url=self.__req_url__+to_url, data=json.dumps(data))
        r.raise_for_status()
        result = r.json()
        return True if result["status"] == "success" else False, result["data"] if "data" in result else None

    def _get(self, to_url: str) -> Tuple[bool, dict]:
        """
        docstring
        """
        r = requests.post(url=self.__req_url__+to_url)
        r.raise_for_status()
        result = r.json()
        return True if result["status"] == "success" else False, result["data"]

    # --------------------------------------------------

    def create_folder(self, folder_name: str) -> Optional[Folder]:
        """
        docstring
        """
        data = {
            "folderName": folder_name
        }
        s, d = self._post("/api/folder/create", data)
        if s:
            return Folder(
                api=self,
                id=d["id"],
                name=d["name"],
                description="",
                modificationTime=d["modificationTime"],
                imageCount=0,
                pinyin=d["name"],
                tags=d["tags"],
                children=d["children"]
            )

    def rename_folder(self, folder_id: str, folder_name: str) -> Optional[Folder]:
        """
        docstring
        """
        data = {
            "folderId": folder_id,
            "folderName": folder_name
        }

        s, d = self._post("/api/folder/rename", data)
        if s:
            return Folder(
                api=self,
                id=d["id"],
                name=d["name"],
                description=d["description"],
                modificationTime=d["modificationTime"],
                imageCount=0,
                tags=d["tags"],
                children=d["children"]
            )

    def update_folder(self, folder_id: str, folder_name: Optional[str] = None, folder_description: Optional[str] = None, folder_color: Optional[str] = None) -> Optional[Folder]:
        """
        docstring
        """
        data = {
            "folderId": folder_id,
        }

        if folder_name:
            data["newName"] = folder_name
        if folder_description:
            data["newDescription"] = folder_description
        if folder_color:
            data["newColor"] = folder_color

        s, d = self._post("/api/folder/update", data)
        if s:
            return Folder(
                api=self,
                id=d["id"],
                name=d["name"],
                description=d["description"],
                modificationTime=d["modificationTime"],
                imageCount=d["size"],
                pinyin=d["pinyin"],
                tags=d["tags"],
                children=d["children"]
            )

    def get_folder_list(self) -> Optional[List[Folder]]:
        """
        docstring
        """
        s, d = self._get("/api/folder/list")
        if s:
            folders = []
            for v in d:
                folders.append(Folder(
                    api=self,
                    id=v["id"],
                    name=v["name"],
                    description=v["description"],
                    modificationTime=v["modificationTime"],
                    imageCount=v["size"],
                    pinyin=v["pinyin"],
                    tags=v["tags"],
                    children=v["children"]
                ))
            return folders

    def get_recent_folder_list(self) -> Optional[List[Folder]]:
        """
        docstring
        """
        s, d = self._get("/api/folder/listRecent")
        if s:
            folders = []
            for v in d:
                folders.append(Folder(
                    api=self,
                    id=v["id"],
                    name=v["name"],
                    description=v["description"],
                    modificationTime=v["modificationTime"],
                    imageCount=v["size"],
                    pinyin=v["pinyin"],
                    tags=v["tags"],
                    children=v["children"]
                ))
            return folders

    # --------------------------------------------------

    def get_item(self, id: str):
        """
        docstring
        """
        data = {
            "id": id
        }
        s, d = self._post("/api/item/info", data)
        if s:
            return Item(
                api=self,
                id=d[""]
            )

    def add_item_from_url(self, url: str, name: str, website: Optional[str] = None, tags: List[str] = [], annotation: Optional[str] = None, modificationTime: datetime = datetime.now(), folderId: Optional[str] = None, headers: Optional[dict] = None) -> Optional[Folder]:
        """
        docstring
        """
        data = {
            "url": url,
            "name": name,
            "website": website,
            "tags": tags if len(tags) != 0 else None,
            "annotation": annotation,
            "modificationTime": int(modificationTime.timestamp()),
            "folderId": folderId,
        }
        s, d = self._post("/api/folder/addFromURL", data)
        if s:
            return Item(
                api=self,
                id=d[""]
            )
