from netmiko import ConnectHandler
import yaml
from datetime import datetime

with open("/home/ponnathan/.netmiko.yml") as yaml_file:
    devices = yaml.safe_load(yaml_file)

device = devices["nxos2"]

dev_con = ConnectHandler(**device, global_delay_factor=2, fast_cli=False)

start_time1 = datetime.now()
output1 = dev_con.send_command("show lldp neighbors detail")
end_time1 = datetime.now()
exec_time_1 = end_time1 - start_time1

print(output1)
print(f"\nExecution time: {exec_time_1}\n")

start_time2 = datetime.now()
output2 = dev_con.send_command("show lldp neighbors detail", delay_factor=8)
end_time2 = datetime.now()
exec_time_2 = end_time2 - start_time2

print(output2)
print(f"\nExecution time: {exec_time_2}\n")

dev_con.disconnect()
