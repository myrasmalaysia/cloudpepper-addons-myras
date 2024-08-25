# -*- coding: utf-8 -*-

from odoo import models,fields

class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    is_customer_allow_change = fields.Boolean(
        'Allow Customer to Change Stage'
    )