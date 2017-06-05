# -*- coding: utf-8 -*-
{
    'name': "Make Invoice Group By Account",

    'summary': "",

    'description': "",

    'author': "Mick",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'sale',
        'account'
    ],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [],
}