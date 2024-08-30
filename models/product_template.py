# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Book'

    is_book = fields.Boolean(string='Is a Book', default=False)
    author_id = fields.Many2one('bookstore.author', string='Author')
    published_date = fields.Date(string='Published Date')
    isbn = fields.Char(string='ISBN')