import pathlib
import sys


def get_appdata_folder():
    """
    Finds the path for application data based on the platform
    :return: Returns the path of the location application data is stored
    """
    home = pathlib.Path.home()
    if sys.platform == "win32":
        return home / "AppData/Roaming"
    elif sys.platform == "linux" or sys.platform == "linux2":
        return home / ".local/share"
    elif sys.platform == "darwin":
        return home / "Library/Application Support"
