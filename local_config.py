# coding: utf-8

POSTGRESQL_CONFIG = {
    "host": '192.168.30.125',
    "port": 5432,
    "username": 'postgres',
    "password": 'postgres'
}


POSTGRES_TIMEOUT = {
    'connect_timeout': 5,
    "options": "-c statement_timeout=5s"
}

LOCAL_POSTGRES_CONFIG = {
    "host": '127.0.0.1',
    "port": 5432,
    "username": 'postgres',
    "password": 'postgres'
}
