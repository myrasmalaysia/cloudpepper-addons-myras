# -*- encoding: utf-8 -*-
from odoo.exceptions import UserError
from odoo import api, fields, models, modules, tools, _


class Project(models.Model):
    _inherit = 'project.project'

    user_ids=fields.Many2many("res.users",string="Assignees")

class ProjectTask(models.Model):
    _inherit = 'project.task'

class HrEmployee(models.Model):
    _inherit = 'hr.employee'


class ResUsers(models.Model):
    _inherit = 'res.users'
