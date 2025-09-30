import json

with open("nxos_interfaces.json", "r") as f:
    nxos_data = json.load(f)

ipv4_list = []
ipv6_list = []

for interface, ip_addr in nxos_data.items():
    if "ipv4" in ip_addr:
        for ip, preflen in ip_addr["ipv4"].items():
            prefix = preflen["prefix_length"]
            ipv4_list.append(f"{ip}/{prefix}")
    if "ipv6" in ip_addr:
        for ip, details in ip_addr["ipv6"].items():
            prefix = preflen["prefix_length"]
            ipv6_list.append(f"{ip}/{prefix}")

print("IPv4 Addresses with Prefixes:")
print(ipv4_list)
print("\nIPv6 Addresses with Prefixes:")
print(ipv6_list)
