from odoo import models, fields

class ProductPackaging(models.Model):
    _inherit = "product.packaging"

    packaging_weight = fields.Float(string="Packaging Weight")
