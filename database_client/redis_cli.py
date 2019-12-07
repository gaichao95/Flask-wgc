from redis import StrictRedis


def conn_redis(config):
    """
    redis 连接
    """
    cli = StrictRedis(host=config["host"],
                      port=config["port"],
                      db=config["database"],
                      password=config["password"],
                      socket_connect_timeout=2,
                      charset='utf-8')
    return cli


REDIS_CONFIG = {
    "host": "127.0.0.1",
    "port": 6379,
    "password": '',
    "database": 0
}

redis_cli = conn_redis(REDIS_CONFIG)
