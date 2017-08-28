# -*- coding: utf-8 -*-
{
    'name': "mrp_product_unique_serial",
    'summary': """
        Extension of addon mrp for avoid asociate an product serial number to
        more than one manufacturing order.""",
    'description': """
        Extension of addon mrp for avoid asociate an product serial number to
        more than one manufacturing order.
    """,
    'author': "Humanytek",
    'website': "http://www.humanytek.com",
    'category': 'Manufacturing',
    'version': '0.4.0',
    'depends': ['mrp'],
    'data': [
        'views/mrp_workorder_views.xml',
    ],
    'demo': [
    ],
}
