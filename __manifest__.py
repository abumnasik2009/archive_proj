# -*- coding: utf-8 -*-
{
    'name': 'archive_project',
    'version': '1.2',
    'category': '',
    'sequence': -100,
    'summary': 'archive_project',
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends': ['mail'],
    'data': [
        'views/menu.xml',
        'views/courts_view.xml',
        'views/operation_type_view.xml',
        'views/department_view.xml',
        'views/occupation.xml',
        'views/case_archive.process_view.xml',
            ],
}
