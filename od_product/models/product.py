from odoo import models, fields

class productTemplate(models.Model):
    _inherit='product.template'
    processor=fields.Char(string="Computer Processor")


