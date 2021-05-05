# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from odm.naturalresources.testing import \
    ODM_NATURALRESOURCES_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that odm.naturalresources is properly installed."""

    layer = ODM_NATURALRESOURCES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if odm.naturalresources is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'odm.naturalresources'))

    def test_browserlayer(self):
        """Test that IOdmNaturalresourcesLayer is registered."""
        from odm.naturalresources.interfaces import (
            IOdmNaturalresourcesLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IOdmNaturalresourcesLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ODM_NATURALRESOURCES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['odm.naturalresources'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if odm.naturalresources is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'odm.naturalresources'))

    def test_browserlayer_removed(self):
        """Test that IOdmNaturalresourcesLayer is removed."""
        from odm.naturalresources.interfaces import \
            IOdmNaturalresourcesLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IOdmNaturalresourcesLayer,
            utils.registered_layers())
