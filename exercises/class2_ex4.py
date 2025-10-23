from netmiko import ConnectHandler
import yaml
from datetime import datetime

with open("/home/ponnathan/.netmiko.yml") as f:
    devices = yaml.safe_load(f)

device = devices["cisco3"]

commands = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]
dev_con = ConnectHandler(**device)
output = dev_con.send_config_set(commands)
print("#" * 30)
print()
print(output)
print()
print("#" * 30)
dev_con.disconnect

print("-" * 50)
print("\n====  With Fast_cli = False ===")
print()
print("-" * 50)
start_time1 = datetime.now()
device["fast_cli"] = False
dev_con = ConnectHandler(**device)
ping_result = dev_con.send_command("ping google.com")
if "!!" in ping_result:
    print("\nping_successful:\n{}\n".format(ping_result))
else:
    raise ValueError("\nPing Failed:\n{}\n".format(ping_result))
dev_con.disconnect()
end_time1 = datetime.now()
print("Excecution Time (Fast_cli=False):", end_time1 - start_time1)
print("-" * 50)

print("\n====  With Fast_cli = True ===")
print("-" * 50)
start_time2 = datetime.now()
device["fast_cli"] = True
dev_con = ConnectHandler(**device)
ping_result = dev_con.send_command("ping google.com")
if "!!" in ping_result:
    print("\nping_successful:\n{}\n".format(ping_result))
else:
    raise ValueError("\nPing Failed:\n{}\n".format(ping_result))
dev_con.disconnect()
end_time2 = datetime.now()
print("Excecution Time (Fast_cli=True):", end_time2 - start_time2)
print("-" * 50)
