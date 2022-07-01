# -*- coding: utf-8 -*-
from odoo import api, fields, models

class process_archive(models.Model):
    _name = "archive.process"
    _description = "ارشفة الدعاوي"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    #inherit = ['mail.thread', 'mail.activity.mixin']
    case_no1 = fields.Integer(string='الرقم ', required=True, tracking=True)

    case_no2 = fields.Selection([('فحص جنائي', 'فحص جنائي'), ('طعن جنائي', 'طعن جنائي'),('فحص شرعي', 'فحص شرعي'),('طعن شرعي ', 'طعن شرعي'),('طعن اداري استئنافي', 'طعن اداري استئنافي'),('اعدام', 'اعدام'),('مؤبد', 'مؤبد'),('حدي', 'حدي'),('مراجعات كل الاقسام', 'مراجعات كل الاقسام'),('المحاكم العسكرية', 'المحاكم العسكرية'), ('مكافحة الارهاب', 'مكافحة الارهاب')], string="النوع", tracking=True, default='')
    #casename_id = fields.Many2one('operation.type', "الاجراء")
    case_no3 = fields.Integer(string='السنة', required=True, tracking=True)
    _sql_constraints = [('case_no1', 'unique (case_no1,case_no2,case_no3)', 'الدعوي مؤرشفة من قبل!')]
    case_owner=fields.Char(string='أطراف الدعوي ', required=True, tracking=True)
    court_members1=fields.Char(string='رئيس الدائرة ', required=True, tracking=True)
    court_members2 = fields.Char(string='صاحب الرأي الأول  ', required=True, tracking=True)
    court_members3 = fields.Char(string='صاحب الرأي الثاني ', required=True, tracking=True)
    case_date=fields.Date(string='تاريخ الارشفة ', required=True, tracking=True, default=fields.Date.context_today)
    active = fields.Boolean(string='Active', default=True)
    case_text_info=fields.Text(string='نص الجكم')
    #age = fields.Integer(string="Age", tracking=True)
   # ref = fields.Char(string="Reference", default='odoo mates')
    #gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True, default='male')
    #address = fields.Char(string='Address')
    #active = fields.Boolean(string='Active', default=True)
