# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging

from odoo import exceptions

_logger = logging.getLogger(__name__)

class sale_me(models.Model):
    _inherit = 'sale.order'

    type_sale = fields.Selection([('new', 'New Sell'), ('re', 'Re-Sell'),], string = 'Sale Type', default = 'new')
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

    @api.model
    def create(self, vals):
        result = None

        if vals.get('client_order_ref') is not False:
            s = self.env['sale.order'].search([])
            tf = False
            for x in s:
                if vals.get('client_order_ref') == x.client_order_ref:
                    tf = True
            if tf is False:
                s = self.env['sale.order'].search([('partner_id','=', vals.get('partner_id')), ('confirmation_date', '!=', None)], order = 'confirmation_date desc')

                if s:
                    latest = s[0].confirmation_date
                    max_date = latest[0:5] + str(int(latest[5:7]) + 3) + latest[7:]

                    if max_date > vals.get('date_order'):
                        vals['type_sale'] = 're'
                result = super(sale_me, self).create(vals)
        else:
            raise exceptions.ValidationError('Did not enter Client Reference or Client Reference was not unique')


        return result

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        for line in self:
            eligible_list = ['Employee', 'Manufacturer', 'Distributor']
            s = line.order_id.partner_id.category_id
            line.discount = 0.0
            no_discount = True
            for x in s:
                for eligible in eligible_list:
                    if x.display_name == eligible:
                        no_discount = False
            if not no_discount:
                line.discount = 15.0
            super(sale_me, self)._compute_amount()

