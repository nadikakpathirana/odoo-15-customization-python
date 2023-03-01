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

# crede_complaint refuse Wizard


class CredeComplaintRefuseWizard(models.Model):
    _name = 'crede.complaint.refuse.wizard'
    _description = 'Crede Complaint Refuse Wizard'

    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'Minimum'),
        ('3', 'High'),
        ('4', 'Maximum'),
        ('5', 'Max'),
    ], string="Rating")
    ref_comment = fields.Text('Enter your Comment')

    def ref_action_ok(self):

        context = dict(self._context or {})
        active_id = context.get('active_id', False)
        if active_id:
            complaint = self.env['crede.complaint'].browse(active_id)
            complaint.write({
                'refused_comment': self.ref_comment,
                'rating': self.priority,
                'refused_by': self.env.user.id,
            })

        template = self.env.ref(
            'crede_complaint_management.send_complaint_refused_notification_created_user')
        template.send_mail(active_id, force_send=True,
                           notif_layout='mail.mail_notification_light')
