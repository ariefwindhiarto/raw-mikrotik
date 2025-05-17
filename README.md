---
title: raw-mikrotk 
status: Public Repo
---

# 🎮 raw-mikrotk — Auto-Update IP Address List Mobile Legends & WhatsApp untuk MikroTik

Sistem ini membuat daftar alamat IP layanan Mobile Legends (Moonton) dan WhatsApp yang akan diperbarui otomatis setiap hari, agar bisa di-*fetch* oleh MikroTik dan dimasukkan ke dalam `address-list`.

---

## 📂 Struktur Folder

```bash
raw-mikrotk/
├── README.md                        # Dokumentasi utama
├── raw/
│   ├── ip-mobilelegends.rsc        # Format .rsc untuk import MikroTik (Mobile Legends)
│   ├── ip-mobilelegends.txt        # Format .txt (alternatif ML)
│   ├── ip-whatsapp.rsc             # Format .rsc untuk WhatsApp
│   └── ip-whatsapp.txt             # Format .txt WhatsApp
├── .github/
│   └── workflows/
│       └── update-ips.yml          # Workflow GitHub Actions (update otomatis)
├── scripts/
│   ├── resolve-ml.py               # Script Python untuk resolve domain Moonton
│   └── resolve-wa.py               # Script Python untuk resolve domain WhatsApp
├── domains.txt                     # Daftar domain Mobile Legends
└── domains-wa.txt                  # Daftar domain WhatsApp
```

---

## 🛠️ Cara Kerja

1. File `domains.txt` dan `domains-wa.txt` berisi domain yang akan direzolusi.
2. Script Python akan memetakan domain menjadi IP publik.
3. File `.rsc` akan terupdate otomatis setiap hari via GitHub Actions.
4. MikroTik bisa fetch file `.rsc` via scheduler.

---

## 📌 Contoh Scheduler MikroTik

Untuk Mobile Legends:
```rsc
/system scheduler
add interval=1d name=update-ml on-event="/tool fetch url=\"https://raw.githubusercontent.com/ariefwindhiarto/raw-mikrotik/main/raw/ip-mobilelegends.rsc\" dst-path=ml.rsc mode=https\n/import file-name=ml.rsc"
```

Untuk WhatsApp:
```rsc
/system scheduler
add interval=1d name=update-wa on-event="/tool fetch url=\"https://raw.githubusercontent.com/ariefwindhiarto/raw-mikrotik/main/raw/ip-whatsapp.rsc\" dst-path=wa.rsc mode=https\n/import file-name=wa.rsc"
```

---

## ✨ Kelebihan

- Otomatis: tidak perlu update manual IP
- Modular: bisa ditambah layanan lain (Telegram, Zoom, TikTok)
- Transparan: semua log perubahan dan script terbuka di GitHub

---

## 🤝 Kontribusi

Silakan *fork* repo ini dan ajukan *pull request* jika ingin menambah daftar domain atau perbaikan script.

---

**raw-mikrotk** by Arief Windhiarto © 2025
