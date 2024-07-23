{
    'name': 'Remove Background',
    'version': '1.0',
    'summary': 'The Remove Background Module for Odoo offers a powerful solution to automatically remove backgrounds from images, streamlining your image editing process. Designed for ease of use, this module ensures high-quality results with minimal manual intervention.',
    'description': """
        <p>This module provides an advanced solution for removing backgrounds from images within Odoo. It's designed to streamline your image editing process by automatically detecting and removing the background</p>
    """,
    'author': 'Vidhema Technologies',
    'website': 'https://www.vidhema.com',
    'depends': ['base'],
    'data': [
        'security/record_rules.xml',
        'views/views.xml',
        'views/menu.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
    ],
    "images":[
        'static/description/cover_image.jpg'
    ],
    'installable': True,
    'auto_install': True,
    'assets': {
    'web.assets_backend': [
        'custom_bg_remove/static/src/css/views.css',
    ],
},

}
