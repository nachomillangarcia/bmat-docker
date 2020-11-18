# Accounts App

Accounts App es una API sencilla con Flask y base de datos PostgreSQL. Almacena nombres de usuario en la base de datos.

### Instalación

Debes tener el comando `pg_config` instalado. En Debian puedes ejecutar `sudo apt install -y libpq-dev`.

`pip install -r requirements.txt`


### Ejecución

```
cd src
export SQLALCHEMY_DATABASE_URI=postgresql://user:pass@hostname:5432/dbname
flask db upgrade
python app.py
```

### Rutas

`GET /` Muestra un Hello World
`POST /accounts` Acepta un JSON del tipo `{"name": "Nacho"}` y almacena ese nombre en la tabla `accounts` en la base de datos