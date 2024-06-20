# -*- coding: utf-8 -*-
from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    level_id = fields.Many2one("employee.level", readonly=True, tracking=True)
    salary = fields.Float(string="salary", related="level_id.salary")
    max_level = fields.Boolean(compute="is_check_or_not")

    @api.depends('level_id')
    def is_check_or_not(self):
        level_list = self.level_id.search([]).ids
        max_lev = max(level_list)
        print("max level", max_lev)
        print("level_id", self.level_id.id)

        if self.level_id.id == max_lev:
            self.max_level = True
        else:
            self.max_level = False

    def action_promote(self):
        for rec in self:
            if not rec.max_level:
                print("incrmnt")
                rec.level_id = rec.level_id.id + 1
            else:
                print("max level reached")
            
