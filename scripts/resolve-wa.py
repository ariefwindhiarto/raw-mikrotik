import socket
import os
from datetime import datetime

root_dir = os.path.dirname(os.path.dirname(__file__))
domain_path = os.path.join(root_dir, "domains-wa.txt")

with open(domain_path) as f:
    domains = [line.strip() for line in f if line.strip()]

ips = set()

for domain in domains:
    try:
        results = socket.gethostbyname_ex(domain)[2]
        for ip in results:
            ips.add(ip)
    except:
        continue

raw_dir = os.path.join(root_dir, "raw")
os.makedirs(raw_dir, exist_ok=True)

with open(os.path.join(raw_dir, "ip-whatsapp.rsc"), "w") as rsc:
    rsc.write("# Updated on {}\n".format(datetime.now()))
    for ip in sorted(ips):
        rsc.write(f"/ip firewall address-list add list=IP-Whatsapp address={ip} comment=auto-wa\n")

with open(os.path.join(raw_dir, "ip-whatsapp.txt"), "w") as txt:
    for ip in sorted(ips):
        txt.write(f"{ip}\n")
