from odoo import api, fields, models, _, tools


class HospitalPatient(models.Model):
    _name = "remedy.patient"
    _description = "Remedy Patient"

    name = fields.Char(string='Name')
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
