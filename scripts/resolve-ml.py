import socket
from datetime import datetime

import os
base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, "../domains.txt")) as f:

    domains = [line.strip() for line in f if line.strip()]

ips = set()

for domain in domains:
    try:
        results = socket.gethostbyname_ex(domain)[2]
        for ip in results:
            ips.add(ip)
    except:
        continue

with open("raw/ip-mobilelegends.rsc", "w") as rsc:
    rsc.write("# Updated on {}\n".format(datetime.now()))
    for ip in sorted(ips):
        rsc.write(f"/ip firewall address-list add list=mobilelegends address={ip} comment=auto-ml\n")

with open("raw/ip-mobilelegends.txt", "w") as txt:
    for ip in sorted(ips):
        txt.write(f"{ip}\n")
