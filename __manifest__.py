# -*- coding: utf-8 -*-
{
    'name': "website_prectice_v18",
    'version': '18.0',
    'category': 'Website',
    'summary': """
        this module is use for website practice purposes only""",
    'description': """
        this module is use for website practice purposes only for version 18
    """,
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/academy_view.xml',
        'views/template.xml'
    ],
    "assets": {
        "web.assets_frontend": [
            "website_v18/static/src/js/owlcomp.js",
            "website_v18/static/src/xml/owlcomps.xml",
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}