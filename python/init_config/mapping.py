import ncs
def interface_mapping(service, link, ip_peer):
    variables = ncs.template.Variables()
    template = ncs.template.Template(service)

    s_node = link.s_node
    s_interface = s_node.interface
    d_node = link.d_node
    d_interface = d_node.interface

    #s_node part
    variables.add("DEVICE", s_node.device)
    variables.add("INT_TYPE", s_interface.int_type)
    variables.add("INT_ID", s_interface.int_id)
    variables.add("IPADDRESS", ip_peer[0].strNormal())
    variables.add("NETMASK", "255.255.255.252")
    template.apply('interface', variables)

    #d_node part
    variables.add("DEVICE", d_node.device)
    variables.add("INT_TYPE", d_interface.int_type)
    variables.add("INT_ID", d_interface.int_id)
    variables.add("IPADDRESS", ip_peer[1].strNormal())
    variables.add("NETMASK", "255.255.255.252")
    template.apply('interface', variables)


