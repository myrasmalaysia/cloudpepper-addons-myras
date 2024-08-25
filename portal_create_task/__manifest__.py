# -*- coding: utf-8 -*-
#################################################################################
# Author      : CFIS (<https://www.cfis.store/>)
# Copyright(c): 2017-Present CFIS.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://www.cfis.store/>
#################################################################################

{
    "name": "Create Task from Portal | Portal Project Task | Project Task Portal | Portal Tasks",
    "summary": """
        This app allows odoo portal users to create / submit 
        new task requests from the portal account and it will create a project task in the backend.""",
    "version": "16.0.1",
    "description": """
        This app allows odoo portal users to create / submit 
        new task requests from the portal account and it will create a project task in the backend.
        Create Task from Portal
        Portal Project Task
        Project Task Portal
        Portal Tasks
    """,    
    "author": "CFIS",
    "maintainer": "CFIS",
    "license" :  "Other proprietary",
    "website": "https://www.cfis.store",
    "images": ["images/portal_create_task.png"],
    "category": "Project",
    "depends": [
        "base",
        "project",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/project_portal_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "/portal_create_task/static/src/css/*.css",
            "/portal_create_task/static/src/js/*.js",
        ],
    },
    "installable": True,
    "application": True,
    "price"                 :  30,
    "currency"              :  "EUR",
    "pre_init_hook"         :  "pre_init_check",
}
