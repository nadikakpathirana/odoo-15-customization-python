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

# Crede. Effect  object


class CredeEffect(models.Model):
    _name = 'crede.effect.model'
    _description = 'Crede Effect'

    name = fields.Char(string='Name', required=True)
