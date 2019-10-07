def clean(recipe):
    return [
        'rm *.pyc',
        'rm *~',
        'rm __pycache__'
    ]
