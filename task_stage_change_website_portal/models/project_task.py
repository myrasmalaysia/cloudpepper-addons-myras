# -*- coding: utf-8 -*-

from odoo import models,fields

class Task(models.Model):
    _inherit = 'project.task'

    def get_task_stages_website_custom(self):
        self.ensure_one()
        stage_list = []
        domain = [('project_ids','in',self.project_id.id),('is_customer_allow_change','=', True),('id','!=',self.stage_id.id)]
        stage_ids = self.env['project.task.type'].search(domain)
        if stage_ids:
            for stage in stage_ids:
                stage_list.append(stage)
            return stage_list