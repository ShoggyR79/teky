# -*- coding: utf-8 -*-
from odoo import http

# class SaleMe(http.Controller):
#     @http.route('/sale_me/sale_me/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_me/sale_me/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_me.listing', {
#             'root': '/sale_me/sale_me',
#             'objects': http.request.env['sale_me.sale_me'].search([]),
#         })

#     @http.route('/sale_me/sale_me/objects/<model("sale_me.sale_me"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_me.object', {
#             'object': obj
#         })