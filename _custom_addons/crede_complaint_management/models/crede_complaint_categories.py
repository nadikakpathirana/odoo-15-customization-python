# -*- coding: utf-8 -*-
#############################################################################
#
#    Crede Technologies.
#
#    Copyright (C) 2023-TODAY Crede Technologies(<https://www.credetechnologies.com>)
#    Author: Anura
#
#############################################################################
from odoo import fields, models

# crede_complaint.categories object


class ShComplainCategories(models.Model):
    _name = 'crede.complaint.categories'
    _description = 'Crede Complaint Categories'

    name = fields.Char(string='Complaint Categories', required=True)
    # department = fields.Many2many('hr.department', string="Department")
    # responsible_persons = fields.Many2many(
    #     'res.users', string="Responsible Persons")
