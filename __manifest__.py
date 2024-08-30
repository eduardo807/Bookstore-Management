# -*- coding: utf-8 -*-

{
    'name': 'Bookstore Management',
    'version': '1.0',
    'summary': 'Manage books, authors, and customers for a bookstore',
    'description': """
        A module to manage a bookstore with functionalities for inventory management, 
        CRM, and sales tracking.
    """,
    'author': 'Ing. Eduardo Morillo',
    'category': 'Sales',
    'depends': ['base', 'purchase', 'sale_management', 'stock'],
    'data': [
        'security/bookstore_security.xml',
        'security/ir.model.access.csv',
        'views/author_view.xml',
        'views/product_template.xml',
        'views/res_partner.xml',
        'views/bookstore_dashboard.xml',
        'views/bookstore_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
