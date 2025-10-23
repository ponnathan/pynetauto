from netmiko import ConnectHandler
import yaml

with open("/home/ponnathan/.netmiko.yml") as yaml_file:
    devices = yaml.safe_load(yaml_file)

for device_name in ["nxos1", "nxos2"]:
    print(f"\n{'#' * 30}\nConnecting to {device_name}...\n{'#' * 30}")
    device = devices[device_name]

    dev_con = ConnectHandler(**device)

    output = dev_con.send_config_from_file("vlans.txt")
    print(f"\nConfiguration output from {device_name}:\n{output}")

    save_output = dev_con.save_config()
    print(f"\nSaved configuration on {device_name}:\n{save_output}")

    dev_con.disconnect()
    print(f"Disconnected from {device_name}\n")
