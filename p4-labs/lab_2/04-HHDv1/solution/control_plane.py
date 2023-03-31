#!/usr/bin/env python3

from p4utils.utils.helper import load_topo
from p4utils.utils.sswitch_p4runtime_API import SimpleSwitchP4RuntimeAPI


topo = load_topo('topology.json')
controllers = {}

for switch, data in topo.get_p4rtswitches().items():
    controllers[switch] = SimpleSwitchP4RuntimeAPI(data['device_id'], data['grpc_port'],
                                                  p4rt_path=data['p4rt_path'],
                                                  json_path=data['json_path'])

controller = controllers['s1']                        

controller.table_clear('hhd_threshold')

controller.table_add('hhd_threshold', 'set_hhd_threshold', ['10.0.0.1/32'], ['100'])
controller.table_add('hhd_threshold', 'set_hhd_threshold', ['10.0.0.2/32'], ['1000'])
controller.table_add('hhd_threshold', 'set_hhd_threshold', ['10.0.0.3/32'], ['300'])