import asyncio
from typing import Any, Dict, List, Optional, Union
import json
import requests


class APIconnection(object):
    """
    This class is the link between Eagle's API and eagle.py.
    All functions in this class have a one-to-one correspondence with the API.
    """
    # might be good if the port of API doesn't change tho
    SERVER_URL = "http://localhost:41595/api"

    def __init__(self):
        """
        init
        """
        pass

    @property
    def loop(self):
        """
        get event loop from asyncio
        """
        return asyncio.get_event_loop()

    async def __get(self, url: str, allow_redirects: bool = True):
        """
        async get
        """
        r = await self.loop.run_in_executor(None, requests.get, url)
        r.raise_for_status()
        j = r.json()
        rstatus: str = j["status"]
        rdata = j["data"] if "data" in j else None
        return (rstatus, rdata)

    async def __post(self, url: str, data: Dict[str, Any], header: Optional[dict] = None, allow_redirects: bool = True):
        """
        async post
        """
        jdata = json.dumps(data)
        r = await self.loop.run_in_executor(None, requests.post, url, jdata, header)
        r.raise_for_status()
        j = r.json()
        rstatus: str = j["status"]
        rdata = j["data"] if "data" in j else None
        return (rstatus, rdata)

    def __url_converter(self, path: str, queries: Dict[str, Any] = {}):
        """
        convert url to Eagle API
        """
        for k, v in queries:
            if isinstance(v, list):
                v = ",".join(v)
                queries[k] = v
        query = "&".join([f"{k}={v}" for k, v in queries.items()]) if len(
            queries) > 0 else None
        return f"{self.SERVER_URL}/{path}?{query if query else ''}"

    # -------------------- application
    async def application_info(self):
        url = self.__url_converter("/application/info")
        s, d = await self.__get(url)
        return d

    # -------------------- folder
    async def folder_create(self, folderName: str, parent: Optional[str] = None):
        url = self.__url_converter("/folder/create")
        data = {
            "folderName": folderName,
            "parent": parent,
        }
        s, d = await self.__post(url, data)
        return d

    async def folder_rename(self, folderId: str, folderName: str):
        url = self.__url_converter("/folder/rename")
        data = {
            "folderId": folderId,
            "folderName": folderName,
        }
        s, d = await self.__post(url, data)
        return d

    async def folder_update(self, folderId: str, newName: str, newDescription: str, newColor: str):
        url = self.__url_converter("/folder/update")
        data = {
            "folderId": folderId,
            "newName": newName,
            "newDescription": newDescription,
            "newColor": newColor,
        }
        s, d = await self.__post(url, data)
        return d

    async def folder_list(self):
        url = self.__url_converter("/folder/list")
        s, d = await self.__get(url)
        return d

    async def folder_listRecent(self):
        url = self.__url_converter("/folder/listRecent")
        s, d = await self.__get(url)
        return d

    # -------------------- item
    async def item_addFromURL(self, url: str, name: str, website: Optional[str], tags: List[str] = [], annotation: Optional[str] = None, modificationTime: Optional[int] = None, folderId: Optional[str] = None, headers: Optional[Dict[str, Any]] = None):
        data = {
            "url": url,
            "name": name,
            "website": website,
            "tags": tags,
            "annotation": annotation,
            "modificationTime": modificationTime,
            "folderId": folderId,
            "headers": headers,
        }
        _url = self.__url_converter("/item/addFromURL")
        s, d = await self.__post(_url, data)
        return s == "success"

    async def item_addFromURLs(self, items: Dict[str, Union[str, List[str], Dict[str, Any], int, None]], folderId: Optional[str] = None):
        url = self.__url_converter("/item/addFromURLs")
        data = {
            "items": items,
            "folderId": folderId
        }
        s, d = await self.__post(url, data)
        return s == "success"

    async def item_addFromPath(self, path: str, name: str, website: Optional[str], tags: List[str] = [], annotation: Optional[str] = None, folderId: Optional[str] = None):
        url = self.__url_converter("/item/addFromPath")
        data = {
            "path": path,
            "name": name,
            "website": website,
            "tags": tags,
            "annotation": annotation,
            "folderId": folderId,
        }
        s, d = await self.__post(url, data)
        return s == "success"

    async def item_addFromPaths(self, items: Dict[str, Union[str, List[str], None]], folderId: Optional[str] = None):
        url = self.__url_converter("/item/addFromPaths")
        data = {
            "items": items,
            "folderId": folderId
        }
        s, d = await self.__post(url, data)
        return s == "success"

    async def item_addBookmark(self, url: str, name: str, base64: str, tags: List[str] = [], modificationTime: Optional[int] = None, folderId: Optional[str] = None):
        data = {
            "url": url,
            "name": name,
            "base64": base64,
            "tags": tags,
            "modificationTime": modificationTime,
            "folderId": folderId,
        }
        _url = self.__url_converter("/item/addBookmark")
        s, d = await self.__post(_url, data)
        return s == "success"

    async def item_info(self, id: str):
        queries = {"id": id}
        url = self.__url_converter("/item/info", queries=queries)
        s, d = await self.__get(url)
        return d

    async def item_thumbnail(self, id: str):
        queries = {"id": id}
        url = self.__url_converter("/item/thumbnail", queries=queries)
        s, d = await self.__get(url)
        return d

    async def item_list(self, limit: int = 200, orderBy: Optional[str] = None, keyword: Optional[str] = None, ext: Optional[str] = None, tags: List[str] = [], folders: List[str] = []):
        queries = {
            "limit": limit,
            "orderBy": orderBy,
            "keyowrd": keyword,
            "ext": ext,
            "tags": tags,
            "folders": folders

        }
        url = self.__url_converter("/item/list", queries=queries)
        s, d = await self.__get(url)
        return d

    async def item_moveToTrash(self, itemIds: List[str]):
        data = {
            "itemIds": itemIds
        }
        url = self.__url_converter("/item/moveToTrash")
        s, d = await self.__post(url, data)
        return s == "success"

    async def item_refreshPalette(self, id: str):
        data = {
            "id": id
        }
        url = self.__url_converter("/item/refreshPalette")
        s, d = await self.__post(url, data)
        return s == "success"

    async def item_refreshThumbnail(self, id: str):
        data = {
            "id": id
        }
        url = self.__url_converter("/item/refreshThumbnail")
        s, d = await self.__post(url, data)
        return s == "success"

    async def item_update(self, id: str, tags: Optional[List[str]] = None, annotation: Optional[str] = None, url: Optional[str] = None, star: Optional[int] = None):
        data = {
            "id": id,
            "tags": tags,
            "annotation": annotation,
            "url": url,
            "star": star,
        }
        _url = self.__url_converter("/item/update")
        s, d = await self.__post(_url, data)
        return s == "success"
