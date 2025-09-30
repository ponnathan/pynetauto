import json

with open("arista_arp.json", "r") as file:
    arp_data = json.load(file)

ip_mac_dict = {}

for entry in arp_data.get("ipV4Neighbors", []):
    ip_address = entry["address"]
    mac_address = entry["hwAddress"]
    ip_mac_dict[ip_address] = mac_address

print("IP to MAC Mapping:")
print(ip_mac_dict)
