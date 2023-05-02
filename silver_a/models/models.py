from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name='silver_a.course'

    name=fields.Char(string='Name', required=True)
    description=fields.Text(string='Description')
    resposible_id=fields.Many2one('res.users', ondelete='set null')
    session_ids=fields.One2many('silver_a.session','course_id',string='Session')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('name_description_check',
         'check (name != description)',
         'The course name and description can not be same.'),

        ('course_name_unique',
         'unique(name)',
         'Course name should be unique'),
    ]


class Session(models.Model):
    _name="silver_a.session"
    _description="SilverA Session"

    name= fields.Char(required=True)
    start_date=fields.Date(string="Start Date",default=fields.Date.context_today)
    duration=fields.Float(digits=(6,2), help="Duration in Days")
    seats=fields.Integer(string="Number of seats")
    instructor_id=fields.Many2one('res.partner', string='Instructor')
    course_id=fields.Many2one('silver_a.course', string='course', required=True )
    attendee_ids = fields.Many2many('res.partner', 'session_ids')
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    active=fields.Boolean(default=True)

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise ValidationError("A session's instructor can't be an attendee")

    @api.onchange('seats', 'attendee_ids')
    def _onchange_seats_attendees(self):
        if self.seats<0:
            return {
            'warning': {
                'title': "Something bad happened",
                'message': "You cannot add negitive values",
            }
        }
        if self.seats<len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Something bad happened",
                    'message': "You cannot add more attendees then number of seats",
                }
            }



    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for session in self:
            if not session.seats:
                session.taken_seats = 0.0
            else:
                session.taken_seats = 100.0 * len(session.attendee_ids) / session.seats




