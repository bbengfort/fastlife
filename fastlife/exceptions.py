# fastlife.exceptions
# Exception and warnings hierarchy for use with fastlife.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sun Jul 26 11:38:51 2020 -0400
#
# Copyright (C) 2020 Bengfort.com
# For license information, see LICENSE
#
# ID: exceptions.py [] benjamin@bengfort.com $

"""
Exception and warnings hierarchy for use with fastlife.
"""

##########################################################################
## Exception Hierarchy
##########################################################################

class FastlifeError(Exception):
    pass


class FastlifeTypeError(FastlifeError, TypeError):
    pass


class FastlifeValueError(FastlifeError, ValueError):
    pass


class ConsoleError(FastlifeError):
    pass



##########################################################################
## Warnings Hierarchy
##########################################################################

class FastlifeWarning(UserWarning):
    pass