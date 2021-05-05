# -*- coding: utf-8 -*-
from odm.naturalresources.content.mining_concession import \
    IMiningConcession  # NOQA E501
from odm.naturalresources.testing import \
    ODM_NATURALRESOURCES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject, queryUtility

import unittest


class MiningConcessionIntegrationTest(unittest.TestCase):

    layer = ODM_NATURALRESOURCES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_mining_concession_schema(self):
        fti = queryUtility(IDexterityFTI, name='Mining Concession')
        schema = fti.lookupSchema()
        self.assertEqual(IMiningConcession, schema)

    def test_ct_mining_concession_fti(self):
        fti = queryUtility(IDexterityFTI, name='Mining Concession')
        self.assertTrue(fti)

    def test_ct_mining_concession_factory(self):
        fti = queryUtility(IDexterityFTI, name='Mining Concession')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IMiningConcession.providedBy(obj),
            u'IMiningConcession not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_mining_concession_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Mining Concession',
            id='mining_concession',
        )

        self.assertTrue(
            IMiningConcession.providedBy(obj),
            u'IMiningConcession not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('mining_concession', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('mining_concession', parent.objectIds())

    def test_ct_mining_concession_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Mining Concession')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_mining_concession_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Mining Concession')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'mining_concession_id',
            title='Mining Concession container',
         )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
