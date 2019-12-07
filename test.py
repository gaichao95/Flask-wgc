from database_client.postgres import local_pg_cli
username = 'wgc'
user_info = list(local_pg_cli.execute("SELECT * FROM www"))
print(user_info)
