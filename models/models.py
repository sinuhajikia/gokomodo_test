from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # field business model(field required)
    business_model = fields.Selection([
        ('RT', 'retail'),
        ('CORP', 'corp'),
        ('SUB', 'subscription'),
    ], string="Business Model", required=True)


    # change the Sale Order display name to include short name of the business model
    def name_get(self):
        result = []
        for order in self:
            name = "[%s]-%s" % (order.business_model, order.name)
            result.append((order.id, name))
        return read_group_result