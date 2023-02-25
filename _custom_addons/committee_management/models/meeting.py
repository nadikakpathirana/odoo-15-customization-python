from odoo import models, fields, api


class CommitteeMeeting(models.Model):
    _name = 'committee.meeting'
    _description = 'Committee Meeting'

    name = fields.Char(string='Meeting Name', required=True)
    members = fields.Many2many('res.partner', 'members_res_partner', string='Committee Members')
    date = fields.Datetime(string='Date and Time', required=True)
    location = fields.Char(string='Location')
    agenda = fields.Text(string='Agenda')
    minutes = fields.Text(string='Minutes')
    attendees = fields.Many2many('res.partner', 'attendees_res_partner', string='Attendees')
    state = fields.Selection([
        ('pending', 'Pending'),
        ('scheduled', 'Scheduled'),
        ('held', 'Held'),
        ('cancelled', 'Cancelled')
    ], string='Meeting Status', default='pending')

    # @api.multi
    def action_hold_meeting(self):
        for rec in self:
            rec.state = 'held'
            return {
                'type': 'ir.actions.client',
                'tag': 'reload',
            }

    # @api.multi
    def action_schedule_meeting(self):
        return {
            'name': 'Schedule Meeting',
            'view_mode': 'form',
            'res_model': 'committee.meeting',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {'default_date': fields.Datetime.now()},
        }

    # @api.multi
    def action_cancel_meeting(self):
        for rec in self:
            rec.state = 'cancelled'
            return {
                'type': 'ir.actions.client',
                'tag': 'reload',
            }
