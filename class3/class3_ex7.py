from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse("bgp_config.txt", ignore_blank_lines=False)

neighbors = parse.find_objects(r"^ neighbor")


bgp_peers = []

for neighbor in neighbors:
    neighbor_ip = neighbor.text.split()[1]
    

    remote_as_line = neighbor.re_search_children(r"^\s+remote-as")[0]
    remote_as = remote_as_line.text.split()[1]
    
    bgp_peers.append((neighbor_ip, remote_as))

print("BGP Peers:")
print(bgp_peers)
