# -*- coding: utf-8 -*-
from odoo import models, fields, api


class EmployeeLevel(models.Model):
    _name = "employee.level"
    _description = "Employee Level"
    _rec_name = 'level'

    level = fields.Text(string="Level", ondelete='restrict')
    salary = fields.Float(string="Salary")



