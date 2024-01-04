# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockMoveWithQuant(models.Model) : 
    _inherit = "stock.move"

    quant_ids = fields.One2many(
        'stock.quant', 
        'product_id', 
        compute='_compute_quant_ids',
        string='Stock Quant')
    
    @api.depends('product_id', 'product_id.stock_quant_ids')
    def _compute_quant_ids(self):
        for move in self:
            move.quant_ids = move.product_id.stock_quant_ids.filtered(lambda quant: quant.location_id.usage == 'internal')