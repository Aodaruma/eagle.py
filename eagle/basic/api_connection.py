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
