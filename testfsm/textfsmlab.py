from netmiko import ConnectHandler
import os

device = {
    "device_type": "cisco_ios",
    "host": "172.31.Y.4",
    "username": "admin",
    "password": "cisco",
}

net_textfsm_path = os.getenv("NET_TEXTFSM")

with ConnectHandler(**device) as conn:
    output = conn.send_command("show cdp neighbors", use_textfsm=True)
    for entry in output:
        print(entry)
