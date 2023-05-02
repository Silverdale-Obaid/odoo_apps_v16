{
    'name': "MyAcademy",
    'author': "Obaid Ahmed",
    'website': "https://www.yourcompany.com",
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/course.xml',
        'views/invoice.xml',
        'views/student.xml',
        'views/tutor.xml',
        'views/ninth_class_student.xml',
        'views/tenth_class_student.xml',
        'views/eleventh_class_student.xml',
        'views/twelveth_class student.xml',
    ],

    # only loaded in demonstration mode
    'installable': True,
    'assets': {
        'web.assets_backend': [
        'myacademy/static/src/css/academy.css',]
    }
}
