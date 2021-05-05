# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import odm.naturalresources


class OdmNaturalresourcesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=odm.naturalresources)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'odm.naturalresources:default')


ODM_NATURALRESOURCES_FIXTURE = OdmNaturalresourcesLayer()


ODM_NATURALRESOURCES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ODM_NATURALRESOURCES_FIXTURE,),
    name='OdmNaturalresourcesLayer:IntegrationTesting',
)


ODM_NATURALRESOURCES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ODM_NATURALRESOURCES_FIXTURE,),
    name='OdmNaturalresourcesLayer:FunctionalTesting',
)


ODM_NATURALRESOURCES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ODM_NATURALRESOURCES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='OdmNaturalresourcesLayer:AcceptanceTesting',
)
