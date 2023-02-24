{
    'name': 'Committee Management',
    'version': '15.0.1',
    'author': 'Nadika K Pathirana',
    'category': 'Management',
    'sequence': -101,
    'summary': 'This module is for executives and committees to manage and track their meetings and their interactions in any complaint management operations.',
    'description': """ 
    The Committee Management Module manages the critical administrative processes such as setting up meetings for envelops opening, technical evaluations, advisory committees and board of counselors and any operations related to business. This module allows to establish committees, hold them with qualified members, create and schedule meetings and issue reports, minutes and decisions made. This module, with the help of steering committees assists to lead patient complaint management operations. 
    """,
    'depends': ['base', 'crede_complainer_registration', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/committee_view.xml',
        'views/complainer_view.xml',
        'views/disscuss_view.xml',
        'views/meeting_views.xml',
    ],  # use to import xml files
    'demo': [],  # use to import demo data into the system
    'application': True,  # so that module is the main domain(That is a application by itself)
    'auto_install': False,
    'license': 'LGPL-3',
}
