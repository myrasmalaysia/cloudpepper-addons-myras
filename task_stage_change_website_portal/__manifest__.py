# -*- coding: utf-8 -*-
# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Task Stage Change Portal Customer',
    'version' : '2.2.2',
    'price': 29.0,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'summary': 'Project Task Change by Customer from Website',
    'description': """
       This app allows customers to change the project task stage from the task page on the website portal.
    """,
    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': "http://www.probuse.com",
    'support': 'contact@probuse.com',
    'category': 'Services/Project',
    'images': ['static/description/ch_image.png'],
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/task_stage_change_website_portal/1335',
    'depends' : [
        'portal', 
        'project' 
    ],
    'data': [
        'views/portal_view.xml',
        'views/task_type_view.xml',
        'views/project_view.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'task_stage_change_website_portal/static/src/js/change_stage.js',
        ],
    },
   
    'installable': True,
    'application': False,
    'auto_install': False,
    
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
