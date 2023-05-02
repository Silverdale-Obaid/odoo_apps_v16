# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class myacademy_student(models.Model):
    _name = 'myacademy.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Student'

    name = fields.Char(string='Name', required=True, tracking=True)
    contact_details = fields.Char(string='Contact Details')
    enrollment_status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')],
                                         string='Enrollment Status', default='active')
    dob = fields.Date(string='Date of Birth')
    address = fields.Html(string='Address')
    class_name = fields.Selection([('9th', 'Ninth'), ('10th', 'Tenth'), ('11th', 'Eleventh'), ('12th', 'Twelveth')],
                                  string='Class', default='9th',tracking=True,copy=False)
    course_ids = fields.Many2many('myacademy.course', string='Courses Enrolled',domain="[('class_name','=',class_name)]")
    invoice_ids = fields.One2many('myacademy.invoice','invoice_number', string='Invoices Issued')
    image_medium = fields.Binary('Medium-Sized Image', attachment=True)



# IF we duplcate student copy text will be added with name
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _("%s (copy)") % (self.name)
        return super(myacademy_student, self).copy(default)
