

from main2 import app
from flask import request, current_app



with app.test_request_context('/products'):
    request.path
    request.method
    current_app.name


    

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
