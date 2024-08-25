# -*- coding: utf-8 -*-

from odoo import models,fields

class Project(models.Model):
    _inherit = "project.project"

    is_customer_allow_change_stage = fields.Boolean(
        'Allow Customer to Change Task Stage'
    )