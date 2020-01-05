# -*- coding: utf-8 -*-
{
    'name': "Library Management",
    'description': """
        Manage library book catalogue and lending.
    """,

    'author': "codeNext",
    'website': "http://www.codenext.nl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    #'category': 'Uncategorized',
    #'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'views/views.xml',
        # 'views/templates.xml',
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'application': True,
}