# -*- coding: utf-8 -*-

from odoo import models, fields, api


class myacademy_tutor(models.Model):
    _name = 'myacademy.tutor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Tutor'

    name = fields.Char(string='Name', required=True,tracking=True)
    contact_details = fields.Char(string='Contact Details',tracking=True)
    qualification = fields.Char(string='Qualification',tracking=True)
    experience = fields.Integer(string='Experience (in years)',tracking=True)

    course_ids = fields.Many2many('myacademy.course', string='Courses Taught')
    image_medium = fields.Binary('Medium-Sized Image', attachment=True)
    salary = fields.Float(string='Salary', compute='_compute_salary',store=True)
    course_count = fields.Integer(compute='_compute_course_count', string='Number of Courses Taught')
    student_count = fields.Integer(compute='_compute_student_count', string='Number of Students in Course')


# Calculate Total courses a tutor teches
    @api.depends('course_ids')
    def _compute_course_count(self):
        for tutor in self:
            tutor.course_count = len(tutor.course_ids)

# Calculate Total Students for each course
    @api.depends('course_ids')
    def _compute_student_count(self):
        for tutor in self:
            tutor.student_count = len(tutor.course_ids.student_ids)



# Calculate Number of students for each course

# Calculate Salary of Tutor
    @api.depends('course_count','student_count')
    def _compute_salary(self):
        for rec in self:
            r = 0
            for tutor in self.course_ids:
                t = (tutor.fees * .25)
                r+=t
                print(r)
                print(rec.student_count)
            rec.salary=r

        # print(tutor.course_count)
        # print(tutor.student_count)
