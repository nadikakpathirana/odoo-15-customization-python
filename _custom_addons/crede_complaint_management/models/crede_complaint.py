# -*- coding: utf-8 -*-
#############################################################################
#
#    Crede Technologies.
#
#    Copyright (C) 2023-TODAY Crede Technologies(<https://www.credetechnologies.com>)
#    Author: Anura
#
#############################################################################
from odoo import api, fields, models

# complaint object


class CredeComplaint(models.Model):
    _name = 'crede.complaint'
    _description = 'Complaint'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Complaint Sequence', readonly=True,
                       required=True, copy=False, default='New')
    subject = fields.Char(string="Subject")
    complaint_category = fields.Many2one(
        'crede.complaint.categories', string="Complaint Category")
    create_date = fields.Datetime(required=True, default=lambda self: self._context.get(
        'Created On', fields.Date.context_today(self, timestamp=None)))
    # write_date = fields.Datetime("Last Updated On", index=True)
    # now = datetime.strftime(fields.Datetime.context_timestamp(self, datetime.now()), "%Y-%m-%d %H:%M:%S")
    # fields.Date.context_today(record, timestamp=None)
    created_by = fields.Many2one(
        'res.users', default=lambda self: self.env.uid, string="Created By")
    complainter_complaint = fields.Many2one(
        'res.partner', string="Complainer Name", required=True)
    # resp_person = fields.Many2many(
    #    'res.users', string="Responsible Person", compute="_compute_responsible_per", store=True)

    resp_persons = fields.Many2one(
        'res.users', string="Responsible Person", store=True, required=True)
    assigned_person = fields.Many2one(
        'res.users', string="Assigned To", store=True, required=True)
    has_effect_on = fields.Many2many('crede.effect.model', string="Has Effect On")
    has_mode_on = fields.Many2many('crede.complaint.mode.model', string="Mode of  Complaint")
    description = fields.Text('Description')
    state = fields.Selection([
        ('new', 'New'),
        ('waiting', 'Waiting For Approval'),
        ('resolve', 'Resolved'),
        ('refused', 'Refused'),
        ('closed', 'Closed')], string='State', readonly=True, index=True, copy=False, default='new',)
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.company)
    is_resolve = fields.Boolean(compute="_compute_resolve_buttont_check")
    resolved_by = fields.Many2one('res.users', string="Responsible Person ")
    refused_by = fields.Many2one('res.users', string="Responsible Person")
    refused_comment = fields.Text(string="Refused Comment")
    resolved_comment = fields.Text(string="Resolved Comment")
    rating = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ], string="Rating")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'crede.complaint') or 'New'
            # result = super(CredeComplaint, self).create(vals)
        return super(CredeComplaint, self).create(vals)

    @api.depends('complaint_category')
    def _compute_responsible_per(self):
        for rec in self:
            rec.resp_persons = False
            if rec.complaint_category:
                rec.resp_persons = [
                    (6, 0, rec.complaint_category.responsible_persons.ids)]

    @api.depends('created_by')
    def _compute_resolve_buttont_check(self):
        self.is_resolve = False
        if self.created_by.id == self.env.user.id:
            self.is_resolve = True

    # complaint form button actions
    def new_complaint_button(self):
        self.write({'state': 'waiting'})
        template = self.env.ref(
            'crede_complaint_management.send_new_complaint_notification_responsible_user')

        partner_to = ''
        total_receipients = len(self.resp_persons)
        count = 1
        if self.resp_persons:
            for resp in self.resp_persons:
                partner_to += str(resp.partner_id.id)
                if count < total_receipients:
                    partner_to += ','
                count += 1

        template.partner_to = partner_to
        template.send_mail(self.id, force_send=True,
                           notif_layout='mail.mail_notification_light')

    def resolve_button(self):
        self.write({'state': 'resolve'})
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'crede.complaint.resolve.wizard',
            'target': 'new',
            'type': 'ir.actions.act_window',
            'context': {'current_id': self.id}
        }

    def refuse_button(self):
        self.write({'state': 'refused'})
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'crede.complaint.refuse.wizard',
            'target': 'new',
            'type': 'ir.actions.act_window',
            'context': {'current_id': self.id}
        }

    def close_button(self):
        self.write({'state': 'closed'})
        return {}

    def reset_to_draft_button(self):
        self.write({'state': 'new',
                    'refused_comment': '',
                    'refused_by': False,
                    'resolved_comment': '',
                    'resolved_by': False,
                    'rating': '0',
                    })
        return {}
