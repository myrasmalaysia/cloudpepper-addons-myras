# -*- coding: utf-8 -*-
# Part of Probuse Consulting Service Pvt. Ltd. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Employee Information to Contract-based Employee on Portal',
    'version' : '2.1.1',
    'price': 9.0,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'summary': 'Employee Information on Portal for External Employee / Contract-based Employees / Subcontractor Employees / Workers / Employee Agents',
    'description': """
This app allows your employee information to show on the account portal of your
website to your contract-based employee who is not an internal user of the system
    """,
    'category': 'Human Resources/Employees',
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website':  'http://www.probuse.com',
    'support': 'contact@probuse.com',
    'images': ['static/description/image.png'],
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/employee_information_subcontractor_portal/1300',
    'depends' : ['hr', 'website','portal'
    ],
    'data': [
        'views/template.xml'
    ],
    'installable': True,
    'application': False,   
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
