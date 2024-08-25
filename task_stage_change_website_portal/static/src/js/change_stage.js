odoo.define('task_stage_change_website_portal.change_stage', function (require) {
'use strict';

require('web.dom_ready');
var ajax = require('web.ajax');

    $("#button_state_change_custom").on("click", function(ev){

        ajax.jsonRpc("/project_task_stage/change/portal", 'call', {

            'task_id' : $('#custom_project_task_id').val(),
            'new_stage_id' : $('input[name="stages"]:checked').val()

        }).then(function () {

            location.reload(true); 
            
        });   
    });
});