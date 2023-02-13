# Basic CRUD

The user REST API allows System Administrators to do the following

* Get all user details
* Get user details
* Create users
* Update users
* Delete users

## How to start server

```bash
python app.py
```

### Before of start server

Edit config.py file add the SQLALCHEMY_DATABASE_URI to postgres, Mysql and so forth.

## CRUD Api for Users

### Get ping message

The server is alive .... ping message

```bash
curl  http://localhost:5000     
```

### Get all user details

All user details can be retrieved

```bash
curl  http://localhost:5000/users 
```

### Get user details

A user's details can be retrieved

```bash
curl  http://localhost:5000/users/1
```

### Create a user

A user can be created

```bash
curl -X POST -H 'Content-Type: application/json' 'http://localhost:5000/users' -d '{"username": "japeto","email": "japeto@japeto.com"}'
```

### Update a user

A user can be updated

```bash
curl -X PUT -H 'Content-Type: application/json' 'http://localhost:5000/users/2' -d '{"username": "prueba","email": "prueba@japeto.com"}'
```


### Delete users

A user can be deleted by making an HTTP DELETE request to

```bash
curl -X DELETE 'http://localhost:5000/users/2
```