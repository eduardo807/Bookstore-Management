# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_bookstore_customer = fields.Boolean(string='Is a Bookstore Customer', default=False)
    customer_since = fields.Date(string='Customer Since', default=fields.Date.today)