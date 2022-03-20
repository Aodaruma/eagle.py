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

    @cached_property
    def version(self):
        """
        returns the version of Eagle App

        Returns
        -------
        str
            the version of Eagle App
        """
        if not self._version:
            self._api.loop.run_until_complete(self.get_info())
        return self._version

    @cached_property
    def prerelease_version(self):
        """
        returns the prerelease version of Eagle App

        Returns
        -------
        str
            the prerelease version of Eagle App
        """
        if not self._prereleaseVersion:
            self._api.loop.run_until_complete(self.get_info())
        return self._prereleaseVersion

    @cached_property
    def build_version(self):
        """
        returns the build version of Eagle App

        Returns
        -------
        str
            the build version of Eagle App
        """
        if not self._buildVersion:
            self._api.loop.run_until_complete(self.get_info())
        return self._buildVersion

    @cached_property
    def exec_path(self):
        """
        returns the exec path of Eagle App

        Returns
        -------
        str
            the exec path of Eagle App
        """
        if not self._execPath:
            self._api.loop.run_until_complete(self.get_info())
        return self._execPath
