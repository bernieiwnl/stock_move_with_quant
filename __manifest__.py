# -*- coding: utf-8 -*-
{
    "name": "Stock move with quant",
    "summary": """Get view of stock quant in delivery""",
    "description": """Get view of stock quant in delivery""",
    "author": "Agustian Suhartono",
    "website": "berniecxy@gmail.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Stock",
    "version": "0.1",
    "application": True,
    "installable": True,
    # any module necessary for this one to work correctly
    "depends": ["base", "stock"],
    # always loaded
    "data": [
        
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
