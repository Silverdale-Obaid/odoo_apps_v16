
{
    'name': "SilverA",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/templates.xml',
        'views/res_partner.xml'
    ],
    # only loaded in demonstration mode
    'installable':True
}
