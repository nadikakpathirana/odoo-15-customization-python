from odoo import api, fields, models, _, tools


class CommitteeCommittee(models.Model):
    _name = "committee.committee"
    _description = "Committee model"

    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    location = fields.Char(string='Location')
    type = fields.Selection([('religious', 'Religious'), ('social', 'Social'), ('cultural', 'Cultural')], string='Type')
    state = fields.Selection([('new', 'New'), ('approved', 'Approved'), ('banned', 'Banned')],
                              string='Status', default='new')

    def action_new(self):
        for rec in self:
            rec.state = 'new'

    def action_approved(self):
        for rec in self:
            rec.state = 'approved'

    def action_banned(self):
        for rec in self:
            rec.state = 'banned'
