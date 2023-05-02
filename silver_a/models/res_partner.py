from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean("Instructor", default=False)
    session_ids = fields.Many2many('silver_a.session', string="Attendees Sessions", readonly=True)