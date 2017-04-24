# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    stock_move_lots_ids = fields.One2many(
        'stock.move.lots', 'lot_id', 'Stock Moves', readonly=True)
