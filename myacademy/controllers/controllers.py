# -*- coding: utf-8 -*-
# from odoo import http


# class Myacademy(http.Controller):
#     @http.route('/myacademy/myacademy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myacademy/myacademy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('myacademy.listing', {
#             'root': '/myacademy/myacademy',
#             'objects': http.request.env['myacademy.myacademy'].search([]),
#         })

#     @http.route('/myacademy/myacademy/objects/<model("myacademy.myacademy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myacademy.object', {
#             'object': obj
#         })
