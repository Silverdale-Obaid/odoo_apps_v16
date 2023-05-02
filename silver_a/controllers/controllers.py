# -*- coding: utf-8 -*-
# from odoo import http


# class SilverA(http.Controller):
#     @http.route('/silver_a/silver_a', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/silver_a/silver_a/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('silver_a.listing', {
#             'root': '/silver_a/silver_a',
#             'objects': http.request.env['silver_a.silver_a'].search([]),
#         })

#     @http.route('/silver_a/silver_a/objects/<model("silver_a.silver_a"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('silver_a.object', {
#             'object': obj
#         })
