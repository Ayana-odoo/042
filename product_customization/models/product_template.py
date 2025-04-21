# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    x_is_domestic = fields.Boolean(
        string="Domestic Product",
        help="Indicates if the product is sourced domestically, based on import data."
    )
