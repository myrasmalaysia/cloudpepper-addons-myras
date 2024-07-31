odoo.define('portal_template.portal_template_inherit2', function (require) {
'use strict';
    const ajax = require('web.ajax');
    var publicWidget = require('web.public.widget');
    publicWidget.registry.TimesheetPannel = publicWidget.Widget.extend({
        selector: '.new_button_class',
        events: {
            'click': 'callController',
        },
        callController: function (ev) {
            //Show Task Dynamically
            var selectedProjectId = $('#mySelectProject').val();
            $.ajax({
                url: "/show/task",
                data: {
                    selected_project_id: selectedProjectId
                },
                success: function(data) {
                    console.log("====calling====")
                    console.log(data)  // Getting Json Data from Python (List of Task)
                    $('#mySelect').empty();
                    var js_array = JSON.parse(data);
                    $('#mySelect').append('<option value=""></option>');
                    js_array.forEach(function(task) {
                        $('#mySelect').append('<option value="' + task + '">' + task + '</option>');
                    });
                    $('#mySelect').show();
                    // Handle success response if needed
                },
               });
               }

    });
});