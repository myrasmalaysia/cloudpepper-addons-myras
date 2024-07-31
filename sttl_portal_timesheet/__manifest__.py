{
    "name": "Portal Timesheet",
    "version": "16.0.1.0",
    "author": "Silver Touch Technologies Limited",
    "website": "https://www.silvertouch.com/",
    "category": "Timesheet",
    "sequence": 15,
    "license": "LGPL-3",
    "summary": "Effortless Timesheet Entry for Portal and Public Users.",
    "description": """
            Effortlessly manage timesheets with our Odoo module designed specifically for portal and public users. 
        """,
    "depends": ['base','project','hr_timesheet','website','portal','sale'],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/portal_template.xml",
    ],
   'assets': {
        'web.assets_frontend': [
            'sttl_portal_timesheet/static/src/js/custom.js',
        ],
   },
    
    "installable": True,
    "application": True,
    "auto_install": False,
    'images': ['static/description/banner.png'],
}
