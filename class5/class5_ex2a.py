from jinja2 import Environment, FileSystemLoader


devices = [
    {
        "device_name": "nxos1",
        "interface": "Ethernet1/1",
        "ip_address": "10.1.100.1",
        "netmask": 24
    },
    {
        "device_name": "nxos2",
        "interface": "Ethernet1/1",
        "ip_address": "10.1.100.2",
        "netmask": 24
    }
]

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('ex2a_template.j2')

for device in devices:
    config = template.render(
        device_name=device["device_name"],
        interface=device["interface"],
        ip_address=device["ip_address"],
        netmask=device["netmask"]
    )
    
    print(config)
    print("-" * 30)
