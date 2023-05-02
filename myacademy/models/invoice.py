# -*- coding: utf-8 -*-

from odoo import models, fields, api


class myacademy_invoice(models.Model):
    _name = 'myacademy.invoice'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _description = 'Invoice'

    invoice_number = fields.Char(string='Invoice Number')
    date = fields.Date(string='Date', required=True)
    amount = fields.Float(string='Amount')
    payment_status = fields.Selection([('paid', 'Paid'), ('unpaid', 'Unpaid')],
                                      string='Payment Status', default='unpaid')
    due_date = fields.Date(string='Due Date')
    payment_method = fields.Selection([('cash', 'Cash'), ('check', 'Check'), ('online', 'Online')],
                                      string='Payment Method', default='cash')
    student_id = fields.Many2one('myacademy.student')
    course_ids = fields.Many2many('myacademy.course')
    fee_status = fields.Selection([('unpaid', 'Unpaid'), ('paid', 'Paid'),
                                   ('late', 'Late')], default='unpaid',
                                  string="Fee Status", tracking=True)
    sender_name = fields.Char(string="Sender Name")
    check_no = fields.Char(string="Check Number")

    def action_paid(self):
        self.fee_status = 'paid'

    def action_late(self):
        self.fee_status = 'late'

    # this will not allow you to create a new record
    ######################################################################
    # @api.onchange('due_date')
    # def state_change(self):
    #     if ((fields.date.today() - self.due_date).days) / 365 < 2:
    #         self.fee_status = 'late'

    @api.onchange('student_id')
    def onchange_student_id(self):
        self.course_ids = self.student_id.course_ids

    @api.onchange('course_ids', 'student_id')
    def _compute_fee(self):
        # print(self.course_ids)
        fee = 0
        for rec in self.course_ids:
            fee += rec.fees
        self.amount = fee

    #     first_record = self.env['myacademy.course'].search([], limit=1)
    #     fee=first_record.fees*count
    #     self.amount=fee

    # print(fee)

    # @api.onchange('course_ids', 'student_id')
    # def _compute_fee(self):
    #     count = len(self.course_ids)
    #
    #     # first_record = self.env['myacademy.course'].browse(2)
    #     f = self.student_id
    #     if f.class_name=='9th':
    #         fee = 1500 * count
    #         self.amount = fee
    #     elif f.class_name=='10th':
    #         fee = 1500 * count
    #         self.amount = fee
    #     else:
    #         fee = 2000 * count
    #         self.amount = fee

    def fee_payment(self):
        return
