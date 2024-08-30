# -*- coding: utf-8 -*-

from odoo import models, fields


class Author(models.Model):
    _name = 'bookstore.author'
    _description = 'Author'

    name = fields.Char(string='Name', required=True)
    biography = fields.Text(string='Biography')
    book_ids = fields.One2many('product.template', 'author_id', string='Books')
