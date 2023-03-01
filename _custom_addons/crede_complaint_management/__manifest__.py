# -*- coding: utf-8 -*-
#############################################################################
#
#    Crede Technologies.
#
#    Copyright (C) 2023-TODAY Crede Technologies(<https://www.credetechnologies.com>)
#    Author: Anura
#
#############################################################################
{
    "name": "Crede Complaint Management",

    "author": "Crede Technologies",
    
    "license": "",

    "website": "https://www.credetechnologies.com",

    "version": "15.0.1",

    "category": "",

    "summary": "Manage Complaints Module, Handle Worker Complaint, Complaint Management App, Employee Complaint Management, Manage Complaints With Types, Maintain Complaints",

    "description": """"Complaint Management" helps to evaluate complaints systematically. You can manage, handle & solve employees complaints. This module is useful to track  complaint records easily. Admin has to create a complaint category accordingly to the organization and allocate the responsible person & department. Employees can create and post their complaints with categories. After that posted complaints go to responsible persons and they can resolve, refuse, or close. Responsible persons get an email for complaints and the employee gets an email for complaints resolved, refused, or closed. They can give ratings and comment about the decision. You can print the complaint report.Complaint Management System, Manage Complains Module, Complain Management, Employee Complaint Management, Manage Complaints With Types, Maintain Complaints,Manage Complains Module, Complaint Management App, Employee Complaint Management, Manage Complains With Types, Maintain Complaints""",

    "depends": [
            'hr',
            "crede_complainer_registration"
    ],

    "data": [
        'security/crede_complaint_security.xml',
        'security/ir.model.access.csv',
        'data/crede_complaint_sequence.xml',
        'data/new_complaint_mail.xml',
        'views/crede_complaint.xml',
        'wizard/crede_complaint_resolve_wizard.xml',
        'wizard/crede_complaint_refuse_wizard.xml',
        'views/crede_effect.xml',
        'views/crede_complaint_mode.xml',
        'views/crede_complaint_categories.xml',
        'report/complaint_report.xml',


    ],
    "images": ["static/description/background.png", ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "price": "25",
    "currency": "EUR"
}
