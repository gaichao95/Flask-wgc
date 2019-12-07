from .postgres import local_pg_cli


def db_init():
    local_pg_cli.execute("CREATE TABLE if not exists www("
                   "username TEXT UNIQUE NOT NULL,"
                   "password TEXT NOT NULL,"
                   "email TEXT,"
                   "area TEXT)"
                   )

