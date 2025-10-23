from netmiko import ConnectHandler
import yaml

with open("/home/ponnathan/.netmiko.yml") as yaml_file:
    devices = yaml.safe_load(yaml_file)

nxos_devices = ["nxos1", "nxos2"]

for name in nxos_devices:
    device = devices[name]
    dev_conn = ConnectHandler(**device)
    print("Device prompt:", dev_conn.find_prompt())
    print(f" device prompt verified for {name}")
    dev_conn.disconnect()
    print("Connection closed")

