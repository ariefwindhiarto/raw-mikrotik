# resolve-store.py
# Script untuk menyusun IP list dari domain aplikasi e-commerce dan dompet digital
# Output dalam format RSC MikroTik
# Dibuat otomatis, update: 2025-05-17

from datetime import datetime

store_domains = [
    "shopee.co.id", "shopee.com", "shopeemobile.com", "shopee.io", "shopee.sg",
    "tokopedia.com", "tokopedia.net", "tokopediax.com",
    "lazada.co.id", "lazada.com", "grab.com", "gojek.com",
    "dana.id", "ovo.id"
]

mock_resolved_ips = {
    "shopee.co.id": ["103.82.249.44", "103.82.248.88"],
    "tokopedia.com": ["203.190.242.66"],
    "lazada.co.id": ["47.74.194.65"],
    "grab.com": ["52.221.184.204"],
    "gojek.com": ["103.127.132.67"],
    "dana.id": ["103.255.215.5"],
    "ovo.id": ["13.229.38.120"]
}

def generate_rsc(ip_list):
    result = ""
    for ip in ip_list:
        result += f"/ip firewall address-list add address={ip} list=store-apps\n"
    return result

all_ips = set()
for domain in store_domains:
    resolved = mock_resolved_ips.get(domain, [])
    all_ips.update(resolved)

with open("../raw/ip-store.rsc", "w") as f:
    f.write(f"# Updated on {datetime.now().isoformat()}\n")
    f.write(generate_rsc(sorted(all_ips)))
