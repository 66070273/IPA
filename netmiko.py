from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_ios",
        "host": "172.31.144.4",
        "username": "admin",
        "use_keys": True,
        "key_file": "/home/user/.ssh/id_rsa",
    },
    # เพิ่ม R2 และ S1 ด้วย
]

commands = [
    "conf t",
    "vlan 101",
    "exit",
    "interface g0/1",
    "switchport mode access",
    "switchport access vlan 101",
    "exit",
    # เพิ่มคำสั่ง OSPF, ACL, NAT ตามบทบาทแต่ละอุปกรณ์
]

for device in devices:
    print(f"Connecting to {device['host']}")
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(commands)
    print(output)
    net_connect.disconnect()
