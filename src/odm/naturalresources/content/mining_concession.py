# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from collective import dexteritytextindexer
from odm.naturalresources import _
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.interface import implementer


class IMiningConcession(model.Schema):
    """ Marker interface and Dexterity Python Schema for MiningConcession
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('mining_concession.xml')

    start_date = schema.Date(
        title=_(u'Start Date'),
        description=_(u'Date which this concession began'),
        required=False,)

    end_date = schema.Date(
        title=_('End Date'),
        description=_(u'Date which this concession ended'),
        required=False,)

    # Licensed To
    directives.widget('licensed_to',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      },
                      )
    licensed_to = RelationChoice(
        title=_(u'Licensed To'),
        description=_(u'The organization licensed was issued to.'),
        source=CatalogSource(portal_type='Organization'),
        required=False,
    )


@implementer(IMiningConcession)
class MiningConcession(Container):
    """
    """
