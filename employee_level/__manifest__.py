# -*- coding: utf-8 -*-
{
    'name': "Employee Level",
    'summary': 'Manage Employee Level',
    'description': 'Manage Employee Level',
    'license': 'LGPL-3',
    'application': True,

    'depends': ['base','hr'],
    'data': ['security/ir.model.access.csv',

             'views/employee_level_view.xml',
             'views/hr_employee.view.xml',
             'views/employee_level_menu.xml',
             ]
}