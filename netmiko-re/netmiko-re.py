from netmiko import ConnectHandler
import re

devices = [
    {
        "device_type": "cisco_ios",
        "host": "172.31.144.4",  # R1
        "username": "admin",
        "use_keys": True,
        "key_file": "/home/user/.ssh/id_rsa",
    },
    {
        "device_type": "cisco_ios",
        "host": "172.31.144.5",  # R2
        "username": "admin",
        "use_keys": True,
        "key_file": "/home/user/.ssh/id_rsa",
    }
]

# Regular expression pattern
# ตัวอย่างที่เราจะดึง: "GigabitEthernet0/1 is up, line protocol is up (connected)"
interface_status_pattern = r"(^\S+ is up, line protocol is up)"

# ตัวอย่าง uptime:
# "GigabitEthernet0/1 is up, line protocol is up"
# "  Last input 00:00:03, output 00:00:03, output hang never"
uptime_pattern = r"Last input (.*?), output"

for device in devices:
    print(f"\n[+] Connecting to {device['host']}")

    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show interfaces")
    net_connect.disconnect()

    print("Active Interfaces and Uptime:")
    interfaces = output.splitlines()
    i = 0
    while i < len(interfaces):
        line = interfaces[i]
        match = re.match(interface_status_pattern, line)
        if match:
            iface_name = line.split(" ")[0]
            # หาค่า uptime จากบรรทัดถัด ๆ ไป
            for j in range(i + 1, min(i + 10, len(interfaces))):
                up_match = re.search(uptime_pattern, interfaces[j])
                if up_match:
                    print(f"- {iface_name} → Uptime: {up_match.group(1)}")
                    break
        i += 1
