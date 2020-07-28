# fastlife.version
# Maintains version and package information for deployment.
#
# Author:   Benjamin Bengfort
# Created:  Sun Jul 26 08:44:11 2020 -0400
#
# Copyright (C) 2020 Bengfort.com
# For license information, see LICENSE
#
# ID: version.py [] benjamin@bengfort.com $

"""
Maintains version and package information for deployment.
"""

##########################################################################
## Module Info
##########################################################################

__version_info__ = {
    "major": 0,
    "minor": 2,
    "micro": 0,
    "releaselevel": "final",
    "post": 0,
    "serial": 2,
}

##########################################################################
## Helper Functions
##########################################################################


def get_version(short=False):
    """
    Prints the version.
    """
    assert __version_info__["releaselevel"] in ("alpha", "beta", "final")
    vers = ["{major}.{minor}".format(**__version_info__)]

    if __version_info__["micro"]:
        vers.append(".{micro}".format(**__version_info__))

    if __version_info__["releaselevel"] != "final" and not short:
        vers.append(
            "{}{}".format(
                __version_info__["releaselevel"][0],
                __version_info__["serial"],
            )
        )

    if __version_info__["post"]:
        vers.append(".post{}".format(__version_info__["post"]))

    return "".join(vers)
