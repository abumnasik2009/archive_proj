# -*- coding: utf-8 -*-
from odoo import api, fields, models

class archivoccupation(models.Model):
    _name = "archive.occupation"
    _description = " تخصصات المحاكم شرعي مدني جنائي"

  #inherit = ['mail.thread', 'mail.activity.mixin']
    occupation_name = fields.Char(string='اسم التخصص', required=True, tracking=True)
    #age = fields.Integer(string="Age", tracking=True)
   # ref = fields.Char(string="Reference", default='odoo mates')
    #gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True, default='male')
    #address = fields.Char(string='Address')
    #active = fields.Boolean(string='Active', default=True)
