import socket
import os
from datetime import datetime

# Lokasi file domains.txt (pastikan sesuai struktur repo)
domain_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../domains.txt"))
raw_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../raw"))

# Baca daftar domain
if not os.path.isfile(domain_path):
    raise FileNotFoundError(f"File tidak ditemukan: {domain_path}")

with open(domain_path) as f:
    domains = [line.strip() for line in f if line.strip()]

# Resolve domain → IP
ips = set()
for domain in domains:
    try:
        results = socket.gethostbyname_ex(domain)[2]
        for ip in results:
            ips.add(ip)
    except Exception as e:
        print(f"[!] Gagal resolve: {domain} ({e})")

# Buat folder raw jika belum ada
os.makedirs(raw_dir, exist_ok=True)

# Tulis file .rsc untuk MikroTik
rsc_path = os.path.join(raw_dir, "ip-mobilelegends.rsc")
with open(rsc_path, "w") as rsc:
    rsc.write(f"# Updated on {datetime.now()}\n")
    for ip in sorted(ips):
        rsc.write(f"/ip firewall address-list add list=mobilelegends address={ip} comment=auto-ml\n")

# Tulis file .txt (opsional)
txt_path = os.path.join(raw_dir, "ip-mobilelegends.txt")
with open(txt_path, "w") as txt:
    for ip in sorted(ips):
        txt.write(ip + "\n")
