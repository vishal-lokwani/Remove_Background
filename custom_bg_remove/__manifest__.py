{
    'name': 'Remove Background',
    'version': '1.0',
    'summary': 'Remove background of any image',
    'description': """
        <p>Remove background from any image</p>
        <p>you can remove it</p>
    """,
    'author': 'Pukhraj kumawat',
    'website': 'https://www.pk.com',
    'depends': ['base'],
    'data': [
        'security/record_rules.xml',
        'views/views.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': True,
    'assets': {
    'web.assets_backend': [
        'custom_bg_remove/static/src/css/views.css',
    ],
},

}
