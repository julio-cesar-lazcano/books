# -*- coding: utf-8 -*-
{
    'name': "mymodule",

    'summary': """
        Modulo creado para llenar las descriciones de los libros""",

    'description': """
        Modulo creado para llenar las descriciones de los libros, usa Controladores, WEB, Modelos y JS
    """,

    'author': "Julio Cesar Lazcano Cruz",
    'website': "http://julio-lazcano.azurewebsites.net",


    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['website'],

    'data': [
        'security/ir.model.access.csv',
        'views/website_assets.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/checkout_template.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}