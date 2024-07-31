from odoo import http,_
from odoo.http import request, Response
import json
from datetime import datetime


class CreateTimesheetController(http.Controller):
    @http.route('/open/timesheet',auth='user',website=True,type='http',csrf=False)
    def timesheet_form(self, **kwargs):
        if len(kwargs)==0:
            proj_lst = []
            task = request.env['project.task'].sudo().search([('user_ids','in',request.env.user.id)])
            for line in task:
                proj_lst.append(line.project_id.name)
            uniq_proj=list(set(proj_lst))
            return http.request.render("sttl_portal_timesheet.open_timesheet_form1",{"project_records":uniq_proj,"tasks_records":task})  ###call template id
        else:
            dateTimeObj = datetime.strptime(kwargs.get('date'), "%Y-%m-%d")
            time_string = kwargs.get('hrs_spent')
            hours, minutes = map(int, time_string.split(':'))
            total_hours = hours + minutes / 60.0

            proj_id=request.env['project.project'].sudo().search([('name','=',kwargs.get('project_id'))])
            task_id = request.env['project.task'].sudo().search([('name', '=', kwargs.get('task')),('project_id','=',proj_id.id)])
            timesheet=request.env['account.analytic.line'].sudo().create({'date':dateTimeObj,'project_id':proj_id.id,'task_id':task_id.id,'name':kwargs.get('description'),'unit_amount':total_hours})

            return http.request.render("sttl_portal_timesheet.timesheet_notification_record",
                                       {"id":timesheet.id})

    # <!--Edit Button-->
    @http.route('/open/timesheet/<int:timesheet_id>', auth='user',website=True,type='http',csrf=False)
    def timesheet_open(self, timesheet_id,**kwargs):
        print("=====edit timesheet open====",timesheet_id)
        timesheet = request.env['account.analytic.line'].sudo().browse(timesheet_id)
        timesheet_id = request.env['account.analytic.line'].sudo().search([('id', '=', timesheet.id)])
        proj = request.env['project.project'].sudo().search([])
        task = request.env['project.task'].sudo().search([])
        print("=====timesheetdata======",timesheet_id,timesheet_id.date,timesheet_id.unit_amount)
        decimal_hours=timesheet_id.unit_amount
        hours = int(decimal_hours)
        minutes = int((decimal_hours - hours) * 60)
        time_string = f"{hours:02d}:{minutes:02d}"
        emp = request.env['hr.employee'].sudo().search([('user_id', '=', request.env.user.id)])
        # if request.env.user.name == timesheet_id.employee_id.name:
        if timesheet_id.employee_id.id==emp.id or request.env.user.name == timesheet_id.employee_id.name:
            return http.request.render("sttl_portal_timesheet.open_timesheet_edit_form",
            {"timesheet_id":timesheet_id.id,
             "date":timesheet_id.date,
             # "project_records": proj,
             # "tasks_records":task,
             "project":timesheet_id.project_id.name,
             "task":timesheet_id.task_id.name,
             "description":timesheet_id.name,
             "hrs":time_string})
        else:
            return http.request.render("sttl_portal_timesheet.restrict_project_edit_record",{})

    # <!--Update Button-->
    @http.route('/update/edit_timesheet', auth='user', website=True, type='http', csrf=False)
    def timesheet_update(self, **kwargs):
        print("============kwargs=================",kwargs)
        if kwargs.get('timesheet_id'):
            timesheet = request.env['account.analytic.line'].sudo().browse(int(kwargs['timesheet_id']))
            timesheet_id = request.env['account.analytic.line'].sudo().search([('id', '=', timesheet.id)])
            print("=======timesheet_id=============",timesheet_id)
            proj = request.env['project.project'].sudo().search([('name','=',kwargs['project'])])
            task = request.env['project.task'].sudo().search([('name','=',kwargs['task']),('project_id','=',proj.id)])
            dateTimeObj = datetime.strptime(kwargs.get('date'), "%Y-%m-%d")
            time_string = kwargs.get('hrs')
            hours, minutes = map(int, time_string.split(':'))
            total_hours = hours + minutes / 60.0
            timesheet_id.sudo().write({
                'date':dateTimeObj,
                'name':kwargs['description'],
                'unit_amount':total_hours,
                'project_id':proj.id,
                'task_id':task.id})

            return http.request.render("sttl_portal_timesheet.timesheet_notification_record",
                                       {"id": timesheet.id})

    # <!--Controllers Handled From js-->
    @http.route('/show/task', auth='public', website=True, type='http', csrf=False)
    def callController(self,**kwargs):
        task_lst=[]
        task = request.env['project.task'].sudo().search([('project_id.name','=',kwargs.get('selected_project_id')),('user_ids','in',request.env.user.id) ])
        for t in task:
            task_lst.append(t.name)
        print("======Task=========",task_lst)
        json_string = json.dumps(task_lst)
        return json_string