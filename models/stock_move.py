# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockMoveLots(models.Model):
    _inherit = 'stock.move.lots'

    lot_id = fields.Many2one(
        'stock.production.lot', 'Lot',
        domain="[('product_id', '!=', product_id)]")
