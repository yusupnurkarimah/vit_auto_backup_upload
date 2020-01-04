# -*- coding: utf-8 -*-
{
    'name': "vit_auto_backup_upload",

    'summary': """
        Database Auto-Backup Upload
        """,

    'description': """
        Automatically Upload backup to Google Drive.
    """,

    'author': "yusup[vitraining.com]",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','google_drive'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/backup_view.xml',
        'views/templates/auto_backup_mail_templates.xml',
        'data/backup_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}