# -*- coding: utf-8 -*-
##############################################################################
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2017 Marlon Falcón Hernández
#    (<http://www.falconsolutions.cl>).
##############################################################################
{
    'name': 'Gestion_Redes',
    'version': '10.0.0.1.0',
    'author': "Erick Leonardo Ruiz Sanchez",
    'maintainer': 'Erick Leonardo Ruiz Sanchez',
    'website': 'https://erickleonardoruizsanchez.wordpress.com/',
# En caso de tener problemas con la Licencia. Cambiela por 'AGPL-3', 'GPL-3' o 'LGPL-3' FUNCIONA EN AGPL-3    
    'license': 'OPL-1',
    'category': 'account.payment',
    'summary': 'GESTOR DE REDES',
# Atributos de precio para la App Store de Odoo 
    'price': 5.00,
    'currency': 'EUR',
    'depends': ['account','account_accountant'],
    'description': """ MODULO GESTOR DE REDES ===================================================== Este modulo permite gestionar diferentes dispositivos de redes en un almacen """,
    'demo': [],
    'test': [],
    'data': ['views/Gestion_Redes_view.xml'],
    'installable': True,
    'auto_install': False,
}
