from getpass import getpass

password = getpass()
API_KEY = 'mypersonalkey'
rtr3 = {
    'device_type': 'cisco_ios',
    'host': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': password,
}

rtr4 = {
    'device_type': 'cisco_ios',
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': password,
}

