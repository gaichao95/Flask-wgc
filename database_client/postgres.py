# coding: utf-8
import sys
sys.path.append('/home/wgc/PycharmProjects/Flask_V1')
from sqlalchemy import create_engine

from local_config import POSTGRESQL_CONFIG, POSTGRES_TIMEOUT,LOCAL_POSTGRES_CONFIG


def conn_postgres_db(db='controller'):
    url = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'.format(
        user=POSTGRESQL_CONFIG['username'],
        password=POSTGRESQL_CONFIG['password'],
        port=POSTGRESQL_CONFIG['port'],
        host=POSTGRESQL_CONFIG['host'],
        db=POSTGRESQL_CONFIG.get('db', db)
    )
    eng = create_engine(url, client_encoding='utf8',
                        connect_args=POSTGRES_TIMEOUT)
    return eng


def conn_local_postgres_db(db='flask'):
    url = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'.format(
        user=LOCAL_POSTGRES_CONFIG['username'],
        password=LOCAL_POSTGRES_CONFIG['password'],
        port=LOCAL_POSTGRES_CONFIG['port'],
        host=LOCAL_POSTGRES_CONFIG['host'],
        db=LOCAL_POSTGRES_CONFIG.get('db', db)
    )
    eng = create_engine(url, client_encoding='utf8',
                        connect_args=POSTGRES_TIMEOUT)
    return eng


pg_cli = conn_postgres_db()
local_pg_cli = conn_local_postgres_db()
