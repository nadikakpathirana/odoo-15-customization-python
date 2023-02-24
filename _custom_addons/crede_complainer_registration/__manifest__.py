# -*- coding: utf-8 -*-
#############################################################################
#
#    Crede Technologies.
#
#    Copyright (C) 2023-TODAY Crede Technologies(<https://www.credetechnologies.com>)
#    Author: Anura
#
#############################################################################
{
    'name': "Crede Complainer Registration",
    'description': """
     Crede Complainer Registration  module which is used to mange the complainer registration
    """,
    'summary': """
     Crede Complainer Registration  module which is used to mange the complainer registration
    """,
    'author': "Anura",
    'company': "Crede Technologies",
    'maintainer': 'Crede Technologies',
    'website': "https://www.credetechnologies.com",
    "license": "AGPL-3",
    'category': '',
    'version': '15.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/complainer_seq.xml',
        'views/complainer_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,

}
