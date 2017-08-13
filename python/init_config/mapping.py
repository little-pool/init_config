import ncs
import pydevd
from tools.get_IP import get_IP

def interface_mapping(service, link, ip_peer):
    variables = ncs.template.Variables()
    template = ncs.template.Template(service)

    s_node = link.s_node
    s_interface = s_node.interface
    d_node = link.d_node
    d_interface = d_node.interface

    '''
    s_node part
    '''
    variables.add("DEVICE", s_node.device)
    variables.add("INT_TYPE", s_interface.int_type)
    variables.add("INT_ID", s_interface.int_id)
    variables.add("IPADDRESS", ip_peer[0].strNormal())
    variables.add("NETMASK", "255.255.255.252")
    template.apply('interface', variables)

    '''
    d_node part
    '''
    variables.add("DEVICE", d_node.device)
    variables.add("INT_TYPE", d_interface.int_type)
    variables.add("INT_ID", d_interface.int_id)
    variables.add("IPADDRESS", ip_peer[1].strNormal())
    variables.add("NETMASK", "255.255.255.252")
    template.apply('interface', variables)




def igp_mapping(service):
    variables = ncs.template.Variables()
    template = ncs.template.Template(service)

    '''
    redistribute part
    '''
    route_import = service.route_import
    route_type = route_import.route_type
    red_process_id = route_import.red_process_id
    metric_type = route_import.metric_type
    metric_value = route_import.metric_value
    if route_import is not None:
        variables.add("RED",'true')
        variables.add("RED_PROCESS_ID",red_process_id)
        variables.add("RED_TYPE",route_type)
        variables.add("METRIC_TYPE",metric_type)
        variables.add("METRIC_VALUE",metric_value)

    '''
    areas part
    '''
    def mapping_task(area, device, interface):
        variables.add("PROCESS_ID", process_id)
        variables.add("AREA_ID",area.area_id)
        variables.add("AREA_TYPE",area.area_type)
        variables.add("TOTALLY",area.totally)
        variables.add("ROUTER_ID",device.router_id)
        variables.add("INT_IP",get_IP(device.device_id, interface.int_type, interface.int_id))
        variables.add("WILD_CARD",'0.0.0.0')
        variables.add("TAR_AREA",area.area_id)
        variables.add("INT_ID",interface.int_id)
        variables.add("NET_TYPE",interface.network_type)


    process_id = service.process_id
    areas = service.areas.area
    for area in areas:
        area_id = area.area_id
        area_type = area.area_type
        totally = area.totally

        devices = area.devices.device
        for device in devices:
            device_id = device.device_id
            router_id = device.router_id

            interfaces = device.interfaces.interface
            for interface in interfaces:
                int_type = interface.int_type
                int_id = interface.int_id
                network_type = interface.network_type
                mapping_task(area, device, interface)

