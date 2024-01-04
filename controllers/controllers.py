# -*- coding: utf-8 -*-
from odoo import http

# class StockMoveWithQuant(http.Controller):
#     @http.route('/stock_move_with_quant/stock_move_with_quant/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_move_with_quant/stock_move_with_quant/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_move_with_quant.listing', {
#             'root': '/stock_move_with_quant/stock_move_with_quant',
#             'objects': http.request.env['stock_move_with_quant.stock_move_with_quant'].search([]),
#         })

#     @http.route('/stock_move_with_quant/stock_move_with_quant/objects/<model("stock_move_with_quant.stock_move_with_quant"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_move_with_quant.object', {
#             'object': obj
#         })