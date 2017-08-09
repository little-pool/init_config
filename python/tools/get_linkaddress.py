from IPy import IP
'''
input the netblock address which is in type IPy.IP and generate every link's end IPs as a tuple
'''
def get_linkaddress(netblockIP):
    switch = 0
    for i in netblockIP:
        if switch%4 == 0:
            yield IP(i.int()+1), IP(i.int()+2)
        switch += 1