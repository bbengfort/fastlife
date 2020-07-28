# tests
# Tests for the fastlife module
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sun Jul 26 09:12:08 2020 -0400
#
# Copyright (C) 2020 Bengfort.com
# For license information, see LICENSE
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Tests for the fastlife module
"""

##########################################################################
## Test Constants
##########################################################################

EXPECTED_VERSION = "0.2"


##########################################################################
## Initialization Tests
##########################################################################


class TestInitialization(object):
    def test_sanity(self):
        """
        Test that tests work by confirming 7**3 = 343
        """
        assert 7 ** 3 == 343, "The world went wrong!!"

    def test_import(self):
        """
        Assert that the yellowbrick package can be imported.
        """
        try:
            import fastlife
        except ImportError:
            self.fail("Could not import the fastlife library!")

    def test_version(self):
        """
        Assert that the test version matches the library version.
        """
        try:
            import fastlife as fl

            assert fl.__version__ == EXPECTED_VERSION
        except ImportError:
            self.fail("Could not import the fastlife library!")
