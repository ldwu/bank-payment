# -*- coding: utf-8 -*-
# © 2016 Akretion (<http://www.akretion.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Payment Mode',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'author': "Akretion,Odoo Community Association (OCA)",
    'website': 'https://github.com/OCA/bank-payment',
    'category': 'Banking addons',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_payment_method.xml',
        'views/account_payment_mode.xml',
        'views/res_partner_bank.xml',
        'views/res_partner.xml',
    ],
    'demo': ['demo/payment_demo.xml'],
    'installable': True,
}
