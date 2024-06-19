import socket
import time
import json

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cli_sock.settimeout(1.0)

def build_json(rule_id, event_type, event_descr, ethertype, timestamp_sec, timestamp_usec):
    data = {}
    data['rule_id'] = rule_id
    data['event_type'] = event_type
    data['event_descr'] = event_descr
    data['ethertype'] = ethertype
    data['timestamp_sec'] = timestamp_sec
    data['timestamp_usec'] = timestamp_usec

    return json.dumps(data)

for i in range(100):
    json_data = build_json(i, "Deny", "IPv4 Denied", 0x0101 + i, 0x01010101 + i, 0x01010102 + i)
    addr = ("127.0.0.1", 2125)
    cli_sock.sendto(json_data.encode(), addr)
    time.sleep(2)
