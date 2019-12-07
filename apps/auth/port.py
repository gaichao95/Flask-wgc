from apps.base_handler import BaseHandler
from database_client.postgres import pg_cli


class PortHandler(BaseHandler):
    def get(self):
        db_list = list(
            pg_cli.execute("select generate_series('2019-12-05 15:00'::timestamp, '2019-12-05 17:00', '1 hours')  "
                           "as hour, port, type, sum(bit_count), sum(packet_count), sum(error_count) from port_flow "
                           "group by hour, port, type"))
        port_dict = {}
        for row in db_list:
            time_str = row[0].strftime('%Y-%m-%d %H:%M:%S')
            # print(time_str)
            port = row[1]
            port_dict.setdefault(port, {})
            port_dict[port].setdefault(time_str, {
                'in': 0,
                'out': 0
            })
            if row[2] == 'in':
                port_dict[port][time_str]['in'] += int(row[3])
            else:
                port_dict[port][time_str]['out'] += int(row[3])
        write_data = {}
        for port in port_dict:
            tmp_dict = {
                'in': [],
                'out': [],
                'time': []
            }
            # print(port_dict[port])
            tmp_time_list = sorted(port_dict[port].keys())
            # print(tmp_time_list)
            write_data['time'] = tmp_time_list
            for time_str in tmp_time_list:
                tmp_dict['time'].append(time_str)
                tmp_dict['in'].append(port_dict[port][time_str]['in'])
                tmp_dict['out'].append(port_dict[port][time_str]['out'])
            write_data['port{}_in'.format(port)] = tmp_dict['in']
            write_data['port{}_out'.format(port)] = tmp_dict['out']
        return self.write_response(data=write_data)
