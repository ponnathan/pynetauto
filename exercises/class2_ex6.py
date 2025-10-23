from netmiko import ConnectHandler
from getpass import getpass
import time

password = getpass("Enter the password: ")

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

dev_con = ConnectHandler(**device)

print("Current prompt:", dev_con.find_prompt())

dev_con.config_mode()
print("Config mode prompt:", dev_con.find_prompt())

dev_con.exit_config_mode()
print("After exit config mode:", dev_con.find_prompt())

dev_con.write_channel("disable\n")
time.sleep(2)
print("Output after disable:\n", dev_con.read_channel())

dev_con.enable()
print("After enable:", dev_con.find_prompt())

dev_con.disconnect()
print("\nSession log saved in 'my_output.txt'")
