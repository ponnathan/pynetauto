from netmiko import ConnectHandler
import yaml

with open("my_devices.yml") as yaml_file:
    devices = yaml.safe_load(yaml_file)

for device in devices:
    connection = ConnectHandler(
        device_type="arista_eos",
        host=device["host"],
        username=device["username"],
        password=device["password"]
    )
    
    print(f"Connected to {device['device_name']} at {device['host']}")
    

    output = connection.send_command("show version")
    print(output)

    connection.disconnect()
