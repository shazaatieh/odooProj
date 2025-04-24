{
    'name': "Sections",
    'author': 'Shaza',
    'version': '18.0.1.1',
    'depends': ['base', 'website'],
    'summary': "A module for learning sections",
    'description': "Building a model to learn how to do sections dynamically",
    'category': "Website",
    'sequence': 1,
    'application': True,
    'installable': True,
    'data': [
        'views/website_section_views.xml',
        'views/website_templates.xml',
        'views/demo_data.xml',
        'views/website_homepage_inherit.xml',
        'views/website_section_actions.xml',
        'views/website_section_menus.xml',
        'security/ir.model.access.csv',

    ],
    'qweb': [
        'views/website_templates.xml'
    ],
    'controllers': ['controllers/main.py'],
    'depends': ['base', 'website'],

}
