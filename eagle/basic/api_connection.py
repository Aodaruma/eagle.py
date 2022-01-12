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
