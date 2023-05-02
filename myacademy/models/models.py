# -*- coding: utf-8 -*-

from odoo import models, fields, api



class myacademy_courseInvoice(models.Model):
    _name = 'myacademy.courseinvoice'
    _description = 'Course Invoice'

    # course_id = fields.Many2one('myacademy.course', string='Course', required=True)
    # invoice_id = fields.Many2one('myacademy.invoice', string='Invoice', required=True)
    amount = fields.Float(string='Amount', required=True)