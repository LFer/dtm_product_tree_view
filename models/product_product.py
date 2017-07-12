# -*- coding: utf-8 -*-
from openerp import models, fields, _, api, exceptions
from openerp.tools.misc import DEFAULT_SERVER_DATE_FORMAT
import locale
import time
import logging
import ipdb as pdb
from openerp.exceptions import Warning

class product_product(models.Model):
    _inherit='product.product'
    _order = 'name,default_code'

    # @api.one
    # def compute_utilidad(self):
    #     return
    #
    # utilidad = fields.Float(string='Utilidad', compute='compute_utilidad')


class product_template(models.Model):
    _inherit='product.template'
    _order = 'name,default_code'