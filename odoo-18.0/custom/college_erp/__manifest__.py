{
    'name': "College ERP",
    'author': 'Shaza',
    'version': '18.0.1.1',
    'license': "LGPL-3",
    'depends': ['base', 'website'],
    'summary': """ An erp for college education""",
    'description': """ From students adminstration to exam, this covers all aspects of college administration  """,
    'category': "Education",
    # 'website': "www.cybrosys.com",
    'maintainer': "Cybrosys Technologies Pvt Ltd <info@cybrosys.com>",
    'sequence': 4,
    # 'auto install': True,
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/menu.xml',
        'views/report_templates.xml',
        'views/student_search_template.xml',
        'views/sequence.xml',
    ],
'controllers': ['controllers/report.py'],
'assets': {
    'web.report_assets_common': [
        'college_erp/static/img/default_profile.png',
    ],
},

}