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

    test1 = fields.Char(string='test1')
    test2 = fields.Char(string='test2')
    test3 = fields.Char(string='test3')
    test4 = fields.Char(string='test4')
    test5 = fields.Char(string='test5')
    test6 = fields.Char(string='test6')

    def action_new(self):
        for rec in self:
            rec.state = 'new'

    def action_approved(self):
        for rec in self:
            rec.state = 'approved'

    def action_banned(self):
        for rec in self:
            rec.state = 'banned'
