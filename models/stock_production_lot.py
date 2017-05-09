# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    stock_move_lots_ids = fields.One2many(
        'stock.move.lots', 'lot_id', 'Stock Moves', readonly=True)
    available_for_product_in_workorder = fields.Boolean(
        compute='_compute_available_for_product_in_workorder',
        search='_search_available_for_product_in_workorder'
    )

    @api.depends('stock_move_lots_ids')
    def _compute_available_for_product_in_workorder(self):
        for record in self:
            record.available_for_product_in_workorder = False
            if not record.stock_move_lots_ids:
                record.available_for_product_in_workorder = True
            else:
                if len(record.stock_move_lots_ids) == 1:
                    if not record.stock_move_lots_ids[0].lot_produced_id:
                        record.available_for_product_in_workorder = True
                if len(record.stock_move_lots_ids) == 2:
                    record.available_for_product_in_workorder = not bool(
                        [stock_move_lot.id for stock_move_lot in
                        record.stock_move_lots_ids
                        if stock_move_lot.done_wo == False]
                        )

    def _search_available_for_product_in_workorder(self, operator, value):
        product_id = self.env.context['default_product_id']
        production_id = self.env.context['production_id']
        stock_production_lot_ids = self.search(
            ['|',
            '&',
            ('product_id', '=', product_id),
            '|',
            ('stock_move_lots_ids', '=', False),
            '&',
            ('stock_move_lots_ids.production_id', '=', production_id),
            ('stock_move_lots_ids.lot_produced_id', '=', False),
            '&',
            ('product_id', '=', product_id),
            '&',
            ('stock_move_lots_ids.production_id', '!=', production_id),
            ('stock_move_lots_ids.lot_produced_id', '=', False),
            ])

        lots_ids_available_for_product_in_workorder = []
        for stock_production_lot in stock_production_lot_ids:
            if stock_production_lot.stock_move_lots_ids:
                stock_move_lots_done_wo = True
                stock_move_lots_quantity_done = 0.0
                stock_move_lots_produced_id = False
                for stock_move_lot in stock_production_lot.stock_move_lots_ids:
                    if not stock_move_lot.done_wo:
                        stock_move_lots_done_wo = False
                    if stock_move_lot.quantity_done > 0:
                        stock_move_lots_quantity_done = 1
                    if stock_move_lot.lot_produced_id:
                        stock_move_lots_produced_id = True
                if not stock_move_lots_produced_id and \
                    stock_move_lots_quantity_done == 0.0:
                    lots_ids_available_for_product_in_workorder.append(
                        stock_production_lot.id)
                elif not stock_move_lots_produced_id and \
                    stock_move_lots_done_wo:
                    lots_ids_available_for_product_in_workorder.append(
                        stock_production_lot.id)
            else:
                lots_ids_available_for_product_in_workorder.append(
                    stock_production_lot.id)

        return [('id', 'in', sorted(lots_ids_available_for_product_in_workorder))]
