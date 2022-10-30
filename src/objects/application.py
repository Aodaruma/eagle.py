
from typing import Optional


class Application(object):
    """
    docstring
    """

    def __init__(self, version: str, buildVersion: str, execPath: str, platform: str, prereleaseVersion: Optional[str] = None):
        """
        docstring
        """
        self._version: str = version
        self._build_version: str = buildVersion
        self._exec_path: str = execPath
        self._platform: str = platform
        self._prerelease_version: Optional[str] = prereleaseVersion

    @property
    def version(self) -> str:
        """
        return application's version
        """
        return self._version

    @property
    def build_version(self) -> str:
        """
        return application's build version
        """
        return self._build_version

    @property
    def exec_path(self) -> str:
        """
        return application's exec_path
        """
        return self._exec_path

    @property
    def platform(self) -> str:
        """
        return application's platform
        """
        return self._platform

    @property
    def prerelease_version(self) -> Optional[str]:
        """
        return application's prerelease version
        """
        return self._prerelease_version
