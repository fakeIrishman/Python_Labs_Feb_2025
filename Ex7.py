#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description:  Ex7
"""
   Docstring:
"""

import re


all_ports = set(range(1,201))
used_ports = set()

file_name = r"C:\Windows\System32\drivers\etc\services"

with open(file_name, mode = "rt") as fh_in:
    for service_line in fh_in:
        if service_line.isspace() or service_line.startswith("#"): continue

        used_port_line = re.search(r" (\d+)/(tcp|udp)", service_line)

        if used_port_line:
            used_port = int(used_port_line.group(1))
            if used_port < 200:
                used_ports.add(int(used_port))

free_ports = set()
free_ports = all_ports - used_ports

print(free_ports)



