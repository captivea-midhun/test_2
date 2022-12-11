# -*- coding: utf-8 -*-
{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage training""",
    
    'description': """
        Academy Module eto manage Training:
        - Courses
        - Sessions
        - Attendees
        """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [       # Odoo loads files in order, so make sure you specify the xml file first.
        'security/academy_security.xml',  
        'security/ir.model.access.csv
    ],
    
    'demo': [                       # How to link .xml files to the manifest
        'demo/academy_demo.xml'
    ],
    
}