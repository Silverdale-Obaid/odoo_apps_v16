# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class myacademy_course(models.Model):
    _name = 'myacademy.course'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Course'

    @api.depends('start_date', 'end_date')
    def _compute_duration1(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                rec.duration = (rec.end_date - rec.start_date).days / 7
            else:
                rec.duration=0


    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Html(string='Description', tracking=True)
    duration = fields.Integer(string='Duration (in weeks)',compute='_compute_duration1')
    fees = fields.Float(string='Fees')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    student_ids = fields.Many2many('myacademy.student', string='Students Enrolled',
                                   domain="[('class_name','=',class_name)]")
    tutors_ids = fields.Many2many('myacademy.tutor', string='Tutors')
    invoice_ids = fields.Many2many('myacademy.invoice')
    class_name = fields.Selection([('9th', 'Ninth'), ('10th', 'Tenth'), ('11th', 'Eleventh'), ('12th', 'Twelveth')],
                                  string='Class', default='9th')
    color = fields.Integer(string="Color")


    @api.constrains('name')
    def _check(self):
        for rec in self:
            if rec.name and rec.name == rec.name:
                raise ValidationError(_("This Course is already created"))

