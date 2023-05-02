
{
    'name': "Product Extension",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['product','sale','mail'],

    # always loaded
    'data': [
        'views/product.xml',
    ],
    # only loaded in demonstration mode
    'installable':True
}
