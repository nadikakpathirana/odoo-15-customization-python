{
    'name': 'Remedy Hospital',
    'version': '1.0.0',
    'category': 'test category',
    'sequence': -100,  # for listing top of the search result
    'summary': 'test summery',
    'description': """ test description """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml'
    ],  # use to import xml files
    'demo': [],  # use to import demo data into the system
    'application': True,  # so that module is the main domain(That is a application by itself)
    'auto_install': False,
    'license': 'LGPL-3',
}
