import ncs
import pydevd

def get_IP(device_name, int_type, int_id):
    pydevd.settrace("127.0.0.1", port=12345, stdoutToServer=True, stderrToServer=True)
    with ncs.maapi.Maapi() as m:
        with ncs.maapi.Session(m, 'admin', 'python'):
            with m.start_write_trans() as t:
                node = ncs.maagic.get_node(t, '/ncs:devices/device{'+device_name+'}')
    return node.config.interface.GigabitEthernet[int_id].ip.address.primary.address