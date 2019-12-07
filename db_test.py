from database_client.postgres import local_pg_cli

tmp_list = [
    ('192.168.1.1', '192.168.1.2', 20, '08-01'),
    ('192.168.1.2', '192.168.1.1', 20, '08-01'),
    ('192.168.1.2', '192.168.1.1', 30, '08-02'),
    ('192.168.1.3', '192.168.1.1', 40, '08-03'),
    ('192.168.1.2', '192.168.1.1', 30, '08-04'),
    ('192.168.1.2', '192.168.1.1', 60, '08-05'),
    ('192.168.1.2', '192.168.1.1', 80, '08-06')
]

tmp_dict = {}

for row in tmp_list:
    time_str = row[3]
    tmp_dict.setdefault(time_str, {
        'in': 0,
        'out': 0
    })
    if row[1] == '192.168.1.1':
        tmp_dict[time_str]['in'] += row[2]
    elif row[0] == '192.168.1.1':
        tmp_dict[time_str]['out'] += row[2]


time_list = sorted(tmp_dict.keys())

data = {
    'time': time_list,
    'in': [],
    'out': []
}
for time in time_list:
    data['in'].append(tmp_dict[time]['in'])
    data['out'].append(tmp_dict[time]['out'])
print(data)

local_pg_cli.execute("CREATE TABLE if not exists flow("
               "ip_src TEXT NOT NULL,"
               "ip_dst TEXT NOT NULL,"
               "flowsize INT NOT NULL,"
               "create_time TEXT NOT NULL)"
               )

for row in tmp_list:
    local_pg_cli.execute(
        "INSERT INTO flow (ip_src, ip_dst, flowsize, create_time) "
        "VALUES ('{}', '{}', '{}', '{}')".format(row[0], row[1], row[2], row[3]))
