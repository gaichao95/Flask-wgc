from apps.base_handler import BaseHandler
from database_client.postgres import local_pg_cli


class FlowHandler(BaseHandler):
    def get(self, *args, **kwargs):
        ip = '192.168.1.1'

        ip_list = list(local_pg_cli.execute("SELECT * from flow where ip_src= '{}' or ip_dst='{}'".format(ip, ip)))
        ip_dict = {}
        print(ip_list)

        for row in ip_list:
            time_str = row[3]
            ip_dict.setdefault(time_str, {
                'in': 0,
                'out': 0
            })
            if row[1] == ip:
                ip_dict[time_str]['in'] += row[2]
            else:
                ip_dict[time_str]['out'] += row[2]

        time_list = sorted(ip_dict.keys())
        write_data = {
            'time': time_list,
            'in': [],
            'out': []
        }
        for time in time_list:
            write_data['in'].append(ip_dict[time]['in'])
            write_data['out'].append(ip_dict[time]['out'])
        return self.write_response(data=write_data)
