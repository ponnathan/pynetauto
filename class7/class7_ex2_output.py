(py3_venv) [ponnathan@pylab36b class7]$ python class7_ex2.py 



Print the new variable and its type
--------------------
OrderedDict([('zones-information',
              OrderedDict([('zones-security',
                            [OrderedDict([('zones-security-zonename', 'trust'),
                                          ('zones-security-send-reset', 'Off'),
                                          ('zones-security-policy-configurable',
                                           'Yes'),
                                          ('zones-security-interfaces-bound',
                                           '1'),
                                          ('zones-security-interfaces',
                                           OrderedDict([('zones-security-interface-name',
                                                         'vlan.0')]))]),
                             OrderedDict([('zones-security-zonename',
                                           'untrust'),
                                          ('zones-security-send-reset', 'Off'),
                                          ('zones-security-policy-configurable',
                                           'Yes'),
                                          ('zones-security-screen',
                                           'untrust-screen'),
                                          ('zones-security-interfaces-bound',
                                           '2'),
                                          ('zones-security-interfaces',
                                           OrderedDict([('zones-security-interface-name',
                                                         ['fe-0/0/0.0',
                                                          'pt-1/0/0.0'])]))]),
                             OrderedDict([('zones-security-zonename',
                                           'junos-host'),
                                          ('zones-security-send-reset', 'Off'),
                                          ('zones-security-policy-configurable',
                                           'Yes'),
                                          ('zones-security-interfaces-bound',
                                           '0'),
                                          ('zones-security-interfaces',
                                           None)])])]))])
<class 'collections.OrderedDict'>



Print out index and name of the security zones
--------------------
Security Zone #1: trust
Security Zone #2: untrust
Security Zone #3: junos-host




