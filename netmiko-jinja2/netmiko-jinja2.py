import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

# โหลด device data
with open("device_data.yaml") as f:
    devices_data = yaml.safe_load(f)

# เตรียม Jinja2 template
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("config_template.j2")

# วนลูปอุปกรณ์
for device in devices_data["devices"]:
    rendered_config = template.render(**device)
    print(f"Rendering config for {device['name']}:\n{rendered_config}")

    netmiko_device = {
        "device_type": "cisco_ios",
        "host": device["host"],
        "username": "admin",
        "use_keys": True,
        "key_file": "/home/user/.ssh/id_rsa",
    }

    # เชื่อมต่อและส่ง config
    ssh = ConnectHandler(**netmiko_device)
    output = ssh.send_config_set(rendered_config.splitlines())
    print(output)
    ssh.disconnect()
