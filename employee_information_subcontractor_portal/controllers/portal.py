# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
class EmployeeInformationPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        employee_user = request.env.user
        if 'employee_count_custom' in counters:
            values['employee_count_custom'] = request.env['hr.employee.public'].sudo().search_count([('user_id','=',employee_user.id)],limit=1)
        return values

    @http.route(['/my/employee/information'], type='http', auth="user", website=True)
    def portal_my_employee_information_form_custom(self,access_token=None, **kw):
        employee_user = request.env.user
        employee_id = request.env['hr.employee.public'].sudo().search([('user_id','=',employee_user.id)],limit=1)
        if employee_user.id != employee_id.user_id.id:
            return request.redirect("/my")
        values = {'employee_info': employee_id}
        return request.render("employee_information_subcontractor_portal.portal_my_employee_information_form_custom",values)