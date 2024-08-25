import json
import base64

from odoo import http, _, SUPERUSER_ID
from odoo.tools import consteq

from odoo.exceptions import AccessError, MissingError, UserError
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request

class CreateTaskAttachmentController(http.Controller):

    def _task_document_check_access(self, model_name, document_id, access_token=None):
        document = request.env[model_name].browse([document_id])
        document_sudo = document.with_user(SUPERUSER_ID).exists()
        if not document_sudo:
            raise MissingError(_("This document does not exist."))
        try:
            document.check_access_rights('read')
            document.check_access_rule('read')
        except AccessError:
            if not access_token or not document_sudo.access_token or not consteq(document_sudo.access_token, access_token):
                raise
        return document_sudo
    
    @http.route('/portal/project/task_create', type='json', auth='public', methods=['POST'], website=True)
    def project_task_create(self, name, project_id, partner_id=None, user_ids=None, date_deadline=None, description=None, **kwargs):
        if name and project_id:
            projectTask = request.env['project.task'].sudo()
            task = projectTask.sudo().create({
                'name': name,
                'project_id': int(project_id),
                'partner_id': int(partner_id),
                'user_ids': user_ids,
                'date_deadline': date_deadline,
                'description': description,
            })
            return task.id
        return False
    
    @http.route('/portal/attachment/task_add', type='http', auth='public', methods=['POST'], website=True)
    def attachment_task_add(self, name, file, res_model, res_id, access_token=None, **kwargs):
        try:
            self._task_document_check_access(res_model, int(res_id), access_token=access_token)
        except (AccessError, MissingError) as e:
            raise UserError(_("The document does not exist or you do not have the rights to access it."))

        IrAttachment = request.env['ir.attachment']
        access_token = False

        if not request.env.user._is_internal():
            IrAttachment = IrAttachment.sudo().with_context(binary_field_real_user=IrAttachment.env.user)
            access_token = IrAttachment._generate_access_token()

        attachment = IrAttachment.create({
            'name': name,
            'datas': base64.b64encode(file.read()),
            'res_model': res_model,
            'res_id': res_id,
            'access_token': access_token,
        })
        return request.make_response(
            data=json.dumps(attachment.read(['id', 'name', 'mimetype', 'file_size', 'access_token'])[0]),
            headers=[('Content-Type', 'application/json')]
        )

class ProjectCustomerPortalCustom(CustomerPortal):

    @http.route(['/my/tasks/create_new'], type='http', auth="user", website=True)
    def create_new_task(self, access_token=None):
        if not request.session.uid:
            return {'error': 'anonymous_user'}
        
        projects = request.env['project.project'].sudo().search([])
        users = request.env['res.users'].sudo().search([('active', '=', True)])

        values = {
            'projects': projects,
            'users': users,
            'partner': request.env.user.partner_id.id,
            'page_name': 'create_new_task',
        }
        return request.render("portal_create_task.create_new_task", values)
