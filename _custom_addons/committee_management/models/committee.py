from odoo import api, fields, models, _, tools


class CommitteeCommittee(models.Model):
    _name = "committee.committee"
    _description = "Committee model"

    name = fields.Char(string='Name')
    title = fields.Char(string='Title')
    type = fields.Selection([('type1', 'Type 01'), ('type2', 'Type 02')], string='Type')
