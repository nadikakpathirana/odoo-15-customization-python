# -*- coding: utf-8 -*-
#############################################################################
#
#    Crede Technologies.
#
#    Copyright (C) 2023-TODAY Crede Technologies(<https://www.credetechnologies.com>)
#    Author: Anura
#
#############################################################################
from odoo import models, fields, api
from datetime import date, timedelta


class Complainer(models.Model):
    _inherit = 'res.partner'

    name = fields.Char(string="Name")
    partner_type = fields.Char(String="complainer", readonly=True)

    dob = fields.Date(string="Date of Birth", required=True)
    status = fields.Selection([('married', 'Married'),
                               ('unmarried', 'Unmarried')],
                              string="Marital Status", required=True)
    gender = fields.Selection([('female', 'Female'),
                               ('male', 'Male'),
                               ('others', 'Other')],
                              string="Gender", required=True)
    complainer_seq = fields.Char(string='Complainer No.', required=True,
                              copy=False,
                              readonly=True,
                              index=True,
                              default=lambda self: 'New')
    notes = fields.Html('Note', sanitize_style=True)
    complainer_profession = fields.Char(string="Profession", help="Profession of the complainer")
    complainer_age = fields.Integer(string="Age", compute='_compute_age')

    # doctor_id = fields.Many2one('hr.employee', string="Family Doctor",
    #                            domain="[('is_doctor','=','doctor')]")

    notes = fields.Text("Notes")

    @api.depends("dob")
    def _compute_age(self):
        """age calculation of complainer"""
        for rec in self:
            rec.complainer_age = False
            if rec.dob:
                rec.complainer_age = (date.today() - rec.dob) // timedelta(days=365.2425)

    def name_get(self):
        res = []
        for name in self:
            res.append((name.id, ("%s (%s)") % (name.name, name.complainer_seq)))
        return res

    @api.model
    def create(self, vals):
        if vals.get('complainer_seq', 'New') == 'New':
            vals['complainer_seq'] = self.env['ir.sequence'].next_by_code('complainer.sequence') or 'New'
        result = super(Complainer, self).create(vals)
        return result
