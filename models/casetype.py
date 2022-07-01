# -*- coding: utf-8 -*-
from odoo import api, fields, models

class operationtype(models.Model):
    _name = "operation.type"
    _description = "تفاصيل انواع الإجراءات فحص طعن "

    #inherit = ['mail.thread', 'mail.activity.mixin']
    casename = fields.Char(string='Name', required=True, tracking=True)

# ref = fields.Char(string="Reference", default='odoo mates')
#gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True, default='male')
#address = fields.Char(string='Address')
#active = fields.Boolean(string='Active', default=True)
