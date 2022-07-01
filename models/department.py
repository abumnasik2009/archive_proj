# -*- coding: utf-8 -*-
from odoo import api, fields, models

class archivedepartment(models.Model):
    _name = "archive.department"
    _description = "اسماء تخصصات المحاكم شرعي مدني جنائي"

  #inherit = ['mail.thread', 'mail.activity.mixin']
    depart_name = fields.Char(string='اسم التخصص', required=True, tracking=True)
    #age = fields.Integer(string="Age", tracking=True)
   # ref = fields.Char(string="Reference", default='odoo mates')
    #gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True, default='male')
    #address = fields.Char(string='Address')
    #active = fields.Boolean(string='Active', default=True)
