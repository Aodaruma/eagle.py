import asyncio
from typing import Any, Dict, List, Optional, Tuple, Union
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

        Returns
        -------
        loop: asyncio.events.AbstractEventLoops
            event loop
        """
        return asyncio.get_event_loop()

    async def __get(self, url: str, allow_redirects: bool = True) -> Tuple[str, Any]:
        """
        async get

        Parameters
        ----------
        url : str
            url
        allow_redirects : bool, optional
            whether following redirects, by default True

        Returns
        -------
        Tuple[str, Any] :
            (status, data)
        """
        r = await self.loop.run_in_executor(None, requests.get, url)
        r.raise_for_status()
        j = r.json()
        rstatus: str = j["status"]
        rdata = j["data"] if "data" in j else None
        return (rstatus, rdata)

    async def __post(self, url: str, data: Dict[str, Any], header: Optional[dict] = None, allow_redirects: bool = True) -> Tuple[str, Any]:
        """
        async post

        Parameters
        ----------
        url : str
            url
        data : Dict[str, Any]
            data
        header : Optional[dict], optional
            header, by default None
        allow_redirects : bool, optional
            whether following redirects, by default True

        Returns
        -------
        Tuple[str, Any] : 
            (status, data)
        """
        jdata = json.dumps(data)
        r = await self.loop.run_in_executor(None, requests.post, url, jdata, header)
        r.raise_for_status()
        j = r.json()
        rstatus: str = j["status"]
        rdata = j["data"] if "data" in j else None
        return (rstatus, rdata)

    def __url_converter(self, path: str, queries: Dict[str, Any] = {}) -> str:
        """
        convert url to Eagle API

        Parameters
        ----------
        path : str
            path
        queries : Dict[str, Any], optional
            queries, by default {}

        Returns
        -------
        str : 
            url
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
        """
        Get detailed information on the Eagle App currently running.
        In most cases, this could be used to determine whether certain functions are available on the user's device.
        https://api.eagle.cool/application/info
        """
        url = self.__url_converter("/application/info")
        s, d = await self.__get(url)
        return d

    # -------------------- folder
    async def folder_create(self, folderName: str, parent: Optional[str] = None):
        """
        Create a folder.
        The created folder will be put at the bottom of the folder list of the current library.
        https://api.eagle.cool/folder/create
        ### Parameters
        `folderName`: The name of the Folder
        `parent`: ID of the parent folder
        """
        url = self.__url_converter("/folder/create")
        data = {
            "folderName": folderName,
            "parent": parent,
        }
        s, d = await self.__post(url, data)
        return d

    async def folder_rename(self, folderId: str, folderName: str):
        """
        Rename the specified folder.
        https://api.eagle.cool/folder/rename
        ### Parameters
        `folderId`: The folder's ID
        `folderName`: The new name of the folder
        """
        url = self.__url_converter("/folder/rename")
        data = {
            "folderId": folderId,
            "folderName": folderName,
        }
        s, d = await self.__post(url, data)
        return d

    async def folder_update(self, folderId: str, newName: str, newDescription: str, newColor: str):
        """
        Update the specified folder.
        https://api.eagle.cool/folder/update
        ### Parameters
        `folderId`: The folder's ID
        `newName`: The new name of the folder
        `newDescription`: The new description of the folder
        `newColor`:"red","orange","green","yellow","aqua","blue","purple","pink"
        """
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
        """
        Get the list of folders of the current library.
        https://api.eagle.cool/folder/list
        """
        url = self.__url_converter("/folder/list")
        s, d = await self.__get(url)
        return d

    async def folder_listRecent(self):
        """
        Get the list of folders recently used by the user.
        https://api.eagle.cool/folder/list-recent
        """
        url = self.__url_converter("/folder/listRecent")
        s, d = await self.__get(url)
        return d

    # -------------------- item
    async def item_addFromURL(self, url: str, name: str, website: Optional[str], tags: List[str] = [], annotation: Optional[str] = None, modificationTime: Optional[int] = None, folderId: Optional[str] = None, headers: Optional[Dict[str, Any]] = None):
        """
        Add an image from an address to Eagle App.
        If you intend to add multiple items in a row, we suggest you use `/api/item/addFromURLs`.
        https://api.eagle.cool/item/add-from-url
        ### Parameters
        `url`: Required, the URL of the image to be added. Supports `http`, `https`, `base64`
        `name`: Required，The name of the image to be added.
        `website`: The Address of the source of the image
        `tags`: Tags for the image.
        `annotation`: The annotation for the image.
        `modificationTime`: The creation date of the image. The parameter can be used to alter the image's sorting order in Eagle. 
        `folderId`: If this parameter is defined, the image will be added to the corresponding folder.
        `headers`: Optional, customize the HTTP headers properties, this could be used to circumvent the security of certain websites.
        """
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
        """
        Add multiple images from URLs to Eagle App.
        https://api.eagle.cool/item/add-from-urls
        ### Parameters
        `items`: The array object made up of multiple items (See the description below)
        `folderId`: If the parameter is defined, images will be added to the corresponding folder.
        #### Description of the Item parameter:
        `url`: Required, the URL of the image to be added. Supports `http`, `https`, `base64`
        `name`: Required，The name of the image to be added.
        `website`: The Address of the source of the image
        `tags`: Tags for the image.
        `annotation`: The annotation for the image.
        `modificationTime`: The creation date of the image. The parameter can be used to alter the image's sorting order in Eagle. 
        `headers`: Optional, customize the HTTP headers properties, this could be used to circumvent the security of certain websites.
        """
        url = self.__url_converter("/item/addFromURLs")
        data = {
            "items": items,
            "folderId": folderId
        }
        s, d = await self.__post(url, data)
        return s == "success"

    async def item_addFromPath(self, path: str, name: str, website: Optional[str], tags: List[str] = [], annotation: Optional[str] = None, folderId: Optional[str] = None):
        """
        Add a local file to Eagle App.
        If you intend to add multiple items in a row, we suggest you use `/api/item/addFromPaths` 
        https://api.eagle.cool/item/add-from-path
        ### Parameters
        `path`: Required, the path of the local file.
        `name`: Required, the name of the image to be added.
        `website`: The Address of the source of the image
        `annotation`: The annotation for the image.
        `tags`: Tags for the image.
        `folderId`: If this parameter is defined, the image will be added to the corresponding folder.
        """
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
        """
        Add multiple local files to Eagle App.
        https://api.eagle.cool/item/add-from-paths
        ### Parameters
        `items`: The array object made up of multiple items (See the description below)
        `folderId`: If the parameter is defined, images will be added to the corresponding folder.
        #### Description of the Item parameter:
        `path`: Required, the path of the local file.
        `name`: Required, the name of the image to be added.
        `website`: The Address of the source of the image
        `annotation`: The annotation for the image.
        `tags`: Tags for the image.
        """
        url = self.__url_converter("/item/addFromPaths")
        data = {
            "items": items,
            "folderId": folderId
        }
        s, d = await self.__post(url, data)
        return s == "success"

    async def item_addBookmark(self, url: str, name: str, base64: str, tags: List[str] = [], modificationTime: Optional[int] = None, folderId: Optional[str] = None):
        """
        Save the link in the URL form to Eagle App.
        https://api.eagle.cool/item/add-bookmark
        ### Parameters
        `url`: Required, the link of the image to be saved. Supports `http`, `https`, `base64` 
        `name`: Required, the name of the image to be added.
        `base64`: The thumbnail of the bookmark. Must be in base64 format.
        `tags`: Tags for the image
        `modificationTime`: The creation date of the images. The parameter can be used to alter the images' sorting order in Eagle. 
        `folderId`: If this parameter is defined, the image will be added to the corresponding folder.
        """
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
        """
        Get Properties of the specified file, including the file name, tags, categorizations, folders, dimensions, etc.
        https://api.eagle.cool/item/info
        ### Parameters
        `id`: ID of the file
        """
        queries = {"id": id}
        url = self.__url_converter("/item/info", queries=queries)
        s, d = await self.__get(url)
        return d

    async def item_thumbnail(self, id: str):
        """
        Get the path of the thumbnail of the file specified.
        If you would like to get a batch of thumbnail paths, the combination of `Library path` + `Object ID` is recommended.
        https://api.eagle.cool/item/thumbnail
        ### Parameters
        `id`: ID of the file
        """
        queries = {"id": id}
        url = self.__url_converter("/item/thumbnail", queries=queries)
        s, d = await self.__get(url)
        return d

    async def item_list(self, limit: int = 200, orderBy: Optional[str] = None, keyword: Optional[str] = None, ext: Optional[str] = None, tags: List[str] = [], folders: List[str] = []):
        """
        Get items that match the filter condition.
        https://api.eagle.cool/item/list
        ### Parameters
        `limit`: The number of items to be displayed. the default number is `200`
        `orderBy`: The sorting order. `CREATEDATE`, `FILESIZE`, `NAME`, `RESOLUTION`, add a minus sign for descending order: `-FILESIZE`
        `keyowrd`: Filter by the keyword
        `ext`: Filter by the extension type, e.g.: `jpg`, `png`
        `tags`: Filter by tags. Use `,` to divide different tags. E.g.: `Design,Poster`
        `folders`: Filter by Folders.  Use `,` to divide folder IDs. E.g.: `KAY6NTU6UYI5Q,KBJ8Z60O88VMG` 
        """
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
        """
        Move items to trash.
        https://api.eagle.cool/item/api-item-movetotrash
        ### Parameters
        `itemIds`: Required
        """
        data = {
            "itemIds": itemIds
        }
        url = self.__url_converter("/item/moveToTrash")
        s, d = await self.__post(url, data)
        return s == "success"

    async def item_refreshPalette(self, id: str):
        """
        Re-analysis the color of the file.
        When changes to the original file were made, you can call this function to refresh the Color Analysis. 
        https://api.eagle.cool/item/refresh-palette
        ### Parameters
        `id`: The item's ID
        """
        data = {
            "id": id
        }
        url = self.__url_converter("/item/refreshPalette")
        s, d = await self.__post(url, data)
        return s == "success"

    async def item_refreshThumbnail(self, id: str):
        """
        Re-generate the thumbnail of the file used to display in the List.
        When changes to the original file were made, you can call this function to re-generate the thumbnail, the color analysis will also be made.
        https://api.eagle.cool/item/refresh-thumbnail
        ### Parameters
        `id`: The item's ID
        """
        data = {
            "id": id
        }
        url = self.__url_converter("/item/refreshThumbnail")
        s, d = await self.__post(url, data)
        return s == "success"

    async def item_update(self, id: str, tags: Optional[List[str]] = None, annotation: Optional[str] = None, url: Optional[str] = None, star: Optional[int] = None):
        """
        Modify data of specified fields of the item.
        #### What tasks can be done with this function?
        - Text output from the external OCR Tools can be added as tags, annotations to the image, and serve as search conditions for later use. 
        - The analysis result of the image generated by external Object Detection Tools can be added in the form of tags, and serve as a search condition.
        https://api.eagle.cool/item/update
        #### Fields that can be modified are listed as follows:
        `id`: Required, the ID of the item to be modified
        `tags`: Optional, tags
        `annotation`: Optional, annotations
        `url`: Optional, the source url
        `star`: Optional, ratings
        """
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

    # -------------------- library

    async def library_info(self):
        """
        Get detailed information of the library currently running.
        The function can be used to obtain details such as All `Folders`, All `Smart Folders`, All `Tag Groups`, `Quick Access` and etc.
        https://api.eagle.cool/library/info
        """
        url = self.__url_converter("/library/info")
        s, d = await self.__get(url)
        return d

    async def library_history(self):
        """
        Get the list of libraries recently opened by the Application. 
        https://api.eagle.cool/library/history
        """
        url = self.__url_converter("/library/history")
        s, d = await self.__get(url)
        return d

    async def library_switch(self, libraryPath: str):
        """
        Switch the library currently opened by Eagle.
        https://api.eagle.cool/library/switch
        ### Parameters
        `libraryPath`: The path of the library
        """
        data = {
            "libraryPath": libraryPath
        }
        url = self.__url_converter("/library/history")
        s, d = await self.__post(url, data)
        return s == "success"
