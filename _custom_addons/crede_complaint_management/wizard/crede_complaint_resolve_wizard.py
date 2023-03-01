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

# crede_complaint resolve Wizard


class CredeComplaintResolveWizard(models.Model):
    _name = 'crede.complaint.resolve.wizard'
    _description = 'Crede Complaint Resolve Wizard'

    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'Minimum'),
        ('3', 'High'),
        ('4', 'Maximum'),
        ('5', 'Max'),
    ], string="Rating")
    res_comment = fields.Text('Enter your Comment')

    def action_ok(self):

        context = dict(self._context or {})
        active_id = context.get('active_id', False)
        if active_id:
            complaint = self.env['crede.complaint'].browse(active_id)
            complaint.write({
                'resolved_comment': self.res_comment,
                'rating': self.priority,
                'resolved_by': self.env.user.id,
            })

        template = self.env.ref(
            'crede_complaint_management.send_complaint_resolved_notification_created_user')
        template.send_mail(active_id, force_send=True,
                           notif_layout='mail.mail_notification_light')
