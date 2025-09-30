from pprint import pprint
import textfsm

template_file = "show_inter_status_ex2.template"
template = open(template_file)

with open("show_inter_status.txt") as f:
    raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

table_keys = re_table.header
final_list = []
for fsm_list in data:
    fsm_dict = dict(zip(table_keys, fsm_list))
    final_list.append(fsm_dict)

print()
print(final_list)
print()
