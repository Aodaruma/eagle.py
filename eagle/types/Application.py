from eagle.basic.api_connection import APIconnection
from eagle.basic.cached_property import cached_property
from eagle.types.Library import Library


class Application(object):
    """
    Application class of Eagle
    """

    def __init__(self, api_connection: APIconnection):
        """
        Constructor

        Parameters
        ----------
        api_connection : APIconnection
            the instance of APIconnection
        """
        self._api = api_connection
        self._version = None
        self._prereleaseVersion = None
        self._buildVersion = None
        self._execPath = None
        self._platform = None
        self._library = None

    async def get_info(self):
        """
        Get information of the application of Eagle
        """
        d = await self._api.application_info()
        self._version = d["version"]
        self._prereleaseVersion = d["prereleaseVersion"]
        self._buildVersion = d["buildVersion"]
        self._execPath = d["execPath"]
        self._platform = d["platform"]
