# flask_web/app.py
import sys
import os
from flask import Flask

import config as cfg

app = Flask(__name__)

@app.route('/')
def hello_world():

    # Leer argumentos del CMD
    argument = ""
    if len(sys.argv) > 1:
        argument = sys.argv[1]

    # Leer variables de entorno
    foo = os.getenv('FOO', "BAR")

    # Leer archivo configuracion
    password = cfg.password

    return f'''Hey, we have Flask in a Docker container!!!! 
    <br> arg: {argument} 
    <br> envvar: {foo} 
    <br> password: {password}'''

app.run(debug=True, host='0.0.0.0')