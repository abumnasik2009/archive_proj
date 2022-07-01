# -*- coding: utf-8 -*-
from odoo import api, fields, models

class archivecourts(models.Model):
    _name = "archive.courts"
    _description = "اسماء المحاكم لفترات متعددة"

    #inherit = ['mail.thread', 'mail.activity.mixin']
    court_name =fields.Selection([('المجكمة الجزيية1901-1948', 'المجكمة الجزيية1901-1948'), ('استئناف المحكمة الجزئية 1948-1973', 'استئناف المحكمة الجزئية 1948=1973'), ('المجكمة القومية العليل 1944-Now', 'المجكمة القومية العليل 1944-Now')], string="المجكمة", tracking=True)
    _sql_constraints = [('court_name', 'unique (court_name)', 'المجكمة مدخلة من قبل!')]


#age = fields.Integer(string="Age", tracking=True)
# ref = fields.Char(string="Reference", default='odoo mates')
#gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True, default='male')
#address = fields.Char(string='Address')
#active = fields.Boolean(string='Active', default=True)
