<h1 align="center">raw-mikrotik 👑</h1>
<p align="center"><i>Auto-Update IP Address List Mobile Legends & WhatsApp untuk MikroTik</i></p>

<p align="center">
  <img src="https://img.shields.io/badge/status-AKTIF-success" alt="Status Aktif"/>
  <img src="https://img.shields.io/github/last-commit/ariefwindhiarto/raw-mikrotik?label=update" alt="Last Updated"/>
  <img src="https://img.shields.io/github/workflow/status/ariefwindhiarto/raw-mikrotik/Auto%20Update%20ML%20IPs?label=status" alt="Workflow Status"/>
  <img src="https://img.shields.io/github/license/ariefwindhiarto/raw-mikrotik" alt="License"/>
</p>

---

## 📁 Daftar File

| Nama File | Deskripsi | Link RAW |
|-----------|-----------|----------|
| `ip-mobilelegends.rsc` | Daftar IP Mobile Legends untuk MikroTik (format .rsc) | [Raw Link](https://raw.githubusercontent.com/ariefwindhiarto/raw-mikrotik/main/raw/ip-mobilelegends.rsc) |
| `ip-mobilelegends.txt` | Format alternatif Mobile Legends (TXT) | [Raw Link](https://raw.githubusercontent.com/ariefwindhiarto/raw-mikrotik/main/raw/ip-mobilelegends.txt) |
| `ip-whatsapp.rsc` | Daftar IP WhatsApp untuk MikroTik (format .rsc) | [Raw Link](https://raw.githubusercontent.com/ariefwindhiarto/raw-mikrotik/main/raw/ip-whatsapp.rsc) |
| `ip-whatsapp.txt` | Format alternatif WhatsApp (TXT) | [Raw Link](https://raw.githubusercontent.com/ariefwindhiarto/raw-mikrotik/main/raw/ip-whatsapp.txt) |

---

## ⚙️ Cara Pakai (untuk MikroTik)

Tambahkan scheduler berikut ke MikroTik Anda:

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

## 🔧 Struktur Folder

```bash
raw-mikrotik/
├── README.md                        # Dokumentasi utama
├── raw/
│   ├── ip-mobilelegends.rsc        # Format .rsc Mobile Legends
│   ├── ip-mobilelegends.txt        # Format .txt Mobile Legends
│   ├── ip-whatsapp.rsc             # Format .rsc WhatsApp
│   └── ip-whatsapp.txt             # Format .txt WhatsApp
├── .github/
│   └── workflows/
│       └── update-ips.yml          # Workflow GitHub Actions (update otomatis)
├── scripts/
│   ├── resolve-ml.py               # Resolver Python ML
│   └── resolve-wa.py               # Resolver Python WhatsApp
├── domains.txt                     # Domain Mobile Legends
└── domains-wa.txt                  # Domain WhatsApp
```

---

## 🎯 Tujuan Proyek

- Menyediakan sistem resolver IP dinamis untuk MikroTik
- Mendukung manajemen jaringan yang efisien dan otomatis
- Membantu pengguna rumahan atau warnet menjaga stabilitas akses aplikasi populer

---

## 🤝 Kontribusi

Silakan *fork* repo ini dan ajukan *pull request* untuk menambah domain baru, skrip tambahan, atau perbaikan.

---

## 🧾 Lisensi

Repositori ini bersifat **open-source** untuk tujuan pembelajaran, eksperimen, dan kontribusi digital. Silakan gunakan dan modifikasi dengan bijak.
