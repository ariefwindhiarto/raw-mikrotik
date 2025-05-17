import socket
from datetime import datetime
import os

base_dir = os.path.dirname(__file__)
domain_path = os.path.join(base_dir, "../domains.txt")
rsc_path = os.path.join(base_dir, "../raw/ip-mobilelegends.rsc")
txt_path = os.path.join(base_dir, "../raw/ip-mobilelegends.txt")

with open("../domains.txt") as f:
    domains = [line.strip() for line in f if line.strip()]

ips = set()

for domain in domains:
    try:
        results = socket.gethostbyname_ex(domain)[2]
        for ip in results:
            ips.add(ip)
    except:
        continue

with open(rsc_path, "w") as rsc:
    rsc.write("# Updated on {}\n".format(datetime.now()))
    for ip in sorted(ips):
        rsc.write(f"/ip firewall address-list add list=mobilelegends address={ip} comment=auto-ml\n")

with open(txt_path, "w") as txt:
    for ip in sorted(ips):
        txt.write(f"{ip}\n")
