# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityItem
from plone.restapi.exceptions import DeserializationError
from plone.restapi.interfaces import IDeserializeFromJson
from plone.restapi.testing import PLONE_RESTAPI_DX_INTEGRATION_TESTING
from plone.restapi.tests.dxtypes import ITestAnnotationsBehavior
from plone.restapi.tests.mixin_ordering import OrderingMixin
from zExceptions import BadRequest
from zope.component import getMultiAdapter
from zope.component import provideHandler
from zope.lifecycleevent.interfaces import IObjectModifiedEvent

import json
import unittest


class TestDXContentDeserializer(unittest.TestCase, OrderingMixin):

    layer = PLONE_RESTAPI_DX_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']

        # ordering setup
        self.folder = self.portal

        for x in range(1, 10):
            self.folder.invokeFactory(
                'Document',
                id='doc' + str(x),
                title='Test doc ' + str(x)
            )

    def deserialize(self, body='{}', validate_all=False, context=None):
        context = context or self.portal
        self.request['BODY'] = body
        deserializer = getMultiAdapter((context, self.request),
                                       IDeserializeFromJson)
        return deserializer(validate_all=validate_all)

    def test_set_layout(self):
        current_layout = self.portal.getLayout()
        self.assertNotEquals(current_layout, "my_new_layout")
        self.deserialize(body='{"layout": "my_new_layout"}')
        self.assertEquals('my_new_layout', self.portal.getLayout())
