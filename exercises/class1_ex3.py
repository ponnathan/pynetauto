from netmiko import ConnectHandler
import yaml

with open("/home/ponnathan/.netmiko.yml") as yaml_file:
    devices = yaml.safe_load(yaml_file)

dev_name = "cisco3"
cisco_device = devices[dev_name]

dev_conn = ConnectHandler(**cisco_device)
output = dev_conn.send_command("show version")

with open ("cisco3_show_version.txt", "w") as f:
    f.write(output)

print("device version verified")

dev_conn.disconnect()

print("Connection closed")

