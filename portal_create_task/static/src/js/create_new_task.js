odoo.define('portal_create_task.create_new_task', function (require) { 
    "use strict";
    
    var core = require('web.core');
    var publicWidget = require('web.public.widget');
    var ajax = require('web.ajax');
    var _t = core._t;
    
    publicWidget.registry.create_new_task = publicWidget.Widget.extend({
        selector: '#wrapwrap:has(.create_new_task_form)',    

        events: {
            'click .create_new_task_confirm': _.debounce(function (ev) {
                this._onCreateNewTask(ev);
            }, 200, true),
        },
        
        init: function (parent, options) {
            this._super.apply(this, arguments);
        },

        start: function () {
            var self = this;
            return self._super.apply(this, arguments);
        },

        _onCreateNewTask:function(ev){
            ev.preventDefault();
            ev.stopPropagation();

            var self = this;

            var $name = $('.create_new_task_form .task_name');
            var name = $name.val() || undefined
            if (!name) {    
                $name.addClass('alter_border');
                self.displayNotification({ message: _t("Please Enter Name") });
                return;
            }else{
                $name.removeClass('alter_border');
            }

            var $project = $('.create_new_task_form .task_project');
            var project = $project.val() || undefined
            if (!project) {    
                $project.addClass('alter_border');
                self.displayNotification({ message: _t("Please Project Name") });
                return;
            }else{
                $project.removeClass('alter_border');
            }

            self._createNewRequest($(ev.currentTarget))
        },

        _createNewRequest: function($btn){
            var self = this;

            $btn.prop('disabled', true);

            var $name = $('.create_new_task_form .task_name');
            var name = $name.val() || undefined

            var $project = $('.create_new_task_form .task_project');
            var project = $project.val() || undefined

            var $partner = $('.create_new_task_form .task_partner');
            var partner = $partner.val() || undefined

            var assigneeIds = []
            var $assignee = $('.create_new_task_form .task_assignee');
            if ($assignee.val()){
                assigneeIds.push(parseInt($assignee.val()));
            }

            var $date_deadline = $('.create_new_task_form .task_date_deadline');
            var date_deadline = $date_deadline.val() || undefined
            
            var $description = $('.create_new_task_form .task_description');
            var description = $description.val() || undefined

            var attahments = $('.create_new_task_form .task_attachments');
            var files = attahments[0].files;

            return ajax.jsonRpc('/portal/project/task_create', 'call', {
                'name': name,
                'project_id': parseInt(project),
                'partner_id': parseInt(partner),
                'user_ids': [([6, false, assigneeIds])],
                'date_deadline': date_deadline,
                'description': description,
            })
            .then(async function(response){
                if (response){
                    if (files.length > 0){
                        return Promise.all(_.map(files, function (file) {
                            return new Promise(function (resolve, reject) {
                                var data = {
                                    'name': file.name,
                                    'file': file,
                                    'res_id': parseInt(response),
                                    'res_model': 'project.task',
                                    'access_token': false,
                                };
                                ajax.post('/portal/attachment/task_add', data).then(function (attachment) {
                                    resolve();
                                    window.location = '/my/tasks'
                                }).guardedCatch(function (error) {
                                    self.displayNotification({
                                        message: _.str.sprintf(_t("Could not save file <strong>%s</strong>"),
                                            _.escape(file.name)),
                                        type: 'warning',
                                        sticky: true,
                                    });
                                    
                                    setTimeout(function(){
                                        $btn.prop('disabled', true);
                                        window.location = '/my/tasks'
                                    },2000);
                                    resolve();
                                });
                            });
                        }));
                    }else{
                        window.location = '/my/tasks'
                    }
                }else{
                    self.displayNotification({ message: _t("Something went wrong during your request updation.") });
                }  
            });
        },
    });
});