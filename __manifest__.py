# -*- coding: utf-8 -*-
{
    'name': "Website Sale Variant Doc.",
    'version': '18.0',
    'category': 'Website',
    'sequence': -1,
    'summary': """
        this module is use for web sale variant document
    """,
    'description': """
        this module is use for website sale variant document
    """,
    'depends': ['website','website_sale','sale_management'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'data': [
        'views/template.xml',
        'views/product_product_inherited.xml',
    ],
    'assets':{
        "web.assets_frontend": [
            "website_sale_variant_document/static/src/js/product_docs.js"
        ]
    },
}