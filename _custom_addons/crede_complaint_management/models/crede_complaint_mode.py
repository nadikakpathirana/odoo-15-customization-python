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


# crede.complaint.mode'


class credeComplaintMode(models.Model):
    _name = 'crede.complaint.mode.model'
    _description = 'Crede complaint mode'

    name = fields.Char(string='Name', required=True, default='Online over here')
