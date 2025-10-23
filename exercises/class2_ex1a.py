from netmiko import ConnectHandler
import yaml

with open("/home/ponnathan/.netmiko.yml") as yaml_file:
    devices = yaml.safe_load(yaml_file)

dev_name =devices["cisco4"]

dev_con = ConnectHandler(**dev_name)
responses = ["\n",      
             "8.8.8.8\n"
             "\n",      
             "\n",      
             "\n",      
             "\n",      
             "\n",
             "\n"]
output = dev_con.send_command_timing("ping", strip_prompt=False, strip_command=False)
for response in responses:
    output += dev_con.send_command_timing(response, strip_prompt=False, strip_command=False)                 

dev_con.disconnect()

print(output)

