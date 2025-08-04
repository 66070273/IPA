import paramiko

devices = {
    "R0": "172.31.144.1",
    "R1": "172.31.144.4",
    "R2": "172.31.144.5",
    "S0": "172.31.144.2",
    "S1": "172.31.144.3",
}

for name, ip in devices.items():
    print(f"\nConnecting to {name} ({ip})...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    ssh.connect(
        hostname=ip,
        username="admin",
        key_filename="/home/youruser/.ssh/id_rsa",  # ← แก้ให้ตรง path จริง
        look_for_keys=True
    )

    stdin, stdout, stderr = ssh.exec_command("show clock")
    print(stdout.read().decode())

    ssh.close()
