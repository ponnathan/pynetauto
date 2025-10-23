from netmiko import ConnectHandler
import yaml

with open("/home/ponnathan/.netmiko.yml") as yaml_file:
    devices = yaml.safe_load(yaml_file)

device = devices["cisco4"]
dev_con = ConnectHandler(**device)

str_responses = [
    "Protocol",
    "Target IP address",
    "Repeat count",
    "Datagram size",
    "Timeout in seconds",
    "Extended commands",
    "Sweep range of sizes",
    "cisco4#"
]

inputs = [
    "ping\n",   
    "\n",       
    "8.8.8.8\n",
    "\n",   
    "\n",   
    "\n",
    "\n",
    "\n"
]

output = ""
for expect_str, answer in zip(str_responses, inputs):
    output += dev_con.send_command(answer, expect_string=expect_str, strip_prompt=False, strip_command=False)

dev_con.disconnect()

print(output)
