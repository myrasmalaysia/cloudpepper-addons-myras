# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class CustomChangeTaskStage(CustomerPortal):  

    @http.route(['/project_task_stage/change/portal'], type='json', auth="user", website=True)
    def custom_change_task_stage(self, **kwargs):
        custom_task_id = kwargs.get('task_id')
        custom_task = request.env['project.task'].sudo().browse(int(custom_task_id))
        new_stage_id = kwargs.get('new_stage_id')
        if new_stage_id:
            custom_task.stage_id = int(new_stage_id)
        return True