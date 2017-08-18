# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    available_for_product_in_workorder = fields.Boolean(
        compute='_compute_available_for_product_in_workorder',
        search='_search_available_for_product_in_workorder'
    )
    available_for_final_lot_in_workorder = fields.Boolean(
        compute='_compute_available_for_product_in_workorder',
        search='_search_available_for_final_lot_in_workorder'
    )

    def _compute_available_for_product_in_workorder(self):
        for record in self:
            record.available_for_product_in_workorder = True
            record.available_for_final_lot_in_workorder = True

    def _search_available_for_product_in_workorder(self, operator, value):
        """Function of searching for computed field
        available_for_product_in_workorder."""

        product_id = self.env.context['default_product_id']
        production_id = self.env.context['production_id']
        StockMove = self.env['stock.move']
        product_moves = StockMove \
            .search([
                ('product_id', '=', product_id),
                ('raw_material_production_id', '!=', False),
                ('raw_material_production_id', '!=', production_id),
                ])
        all_lots_reserved_ids = product_moves.mapped('lot_ids.id')

        product_lots_available_tmp = self.search([
            ('product_id', '=', product_id),
            ('id', 'not in', all_lots_reserved_ids)
        ])

        StockMoveLots = self.env['stock.move.lots']
        active_move_lots = StockMoveLots.search([
            ('lot_id', 'in', product_lots_available_tmp.mapped('id')),
            ('done_wo', '=', False),
        ]).mapped('lot_id')

        product_lots_available = product_lots_available_tmp - \
            active_move_lots

        product_lots_available_ids = list()
        for lot in product_lots_available:
            lot_used = StockMoveLots.search([
                ('lot_id', '=', lot.id),
                ('done_wo', '=', True),
                ('lot_produced_id', '!=', False),
                ('quantity_done', '>', 0),
            ])

            if not lot_used:
                product_lots_available_ids.append(lot.id)

            elif len(lot_used) == 1:
                MrpProduction = self.env['mrp.production']
                lot_used_in_same_product = MrpProduction.search([
                    ('product_id', '=', product_id),
                    ('move_finished_ids.active_move_lot_ids', 'in', lot_used.id),
                ])

                if lot_used_in_same_product:
                    product_lots_available_ids.append(lot.id)

        return [('id', 'in', product_lots_available_ids)]

    def _search_available_for_final_lot_in_workorder(self, operator, value):
        """Function of searching for computed field
        available_for_final_lot_in_workorder."""

        product_id = self.env.context['default_product_id']
        production_id = self.env.context['production_id']
        StockMove = self.env['stock.move']
        product_moves = StockMove \
            .search([
                ('product_id', '=', product_id),
                ('production_id', '!=', False),
                ('production_id', '!=', production_id),
                ])
        all_lots_reserved_ids = product_moves.mapped('lot_ids.id')

        product_lots_available_ids = self.search([
            ('product_id', '=', product_id),
            ('id', 'not in', all_lots_reserved_ids)
        ]).mapped('id')

        return [('id', 'in', product_lots_available_ids)]
