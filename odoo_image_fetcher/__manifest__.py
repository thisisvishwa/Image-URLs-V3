{
    'name': 'Odoo Image Fetcher',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Fetch and display product images from external URLs',
    'sequence': 1,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
        'views/templates.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
Odoo Image Fetcher
==================
This module fetches and displays main product images and extra product media from external URLs on the Odoo 17 CE e-commerce website. It does not store these images in the Odoo database.
    """,
}