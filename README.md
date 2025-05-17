<h1 align="center">raw-mikrotk 👑</h1>
<p align="center"><i>Auto-Update IP Address List Mobile Legends, WhatsApp, dan E-Commerce untuk MikroTik</i></p>

<p align="center">
  <img src="https://img.shields.io/badge/status-AKTIF-success" alt="Status Aktif"/>
  <img src="https://img.shields.io/github/last-commit/ariefwindhiarto/raw-mikrotik?label=update" alt="Last Updated"/>
  <img src="https://img.shields.io/github/actions/workflow/status/ariefwindhiarto/raw-mikrotik/update-ips.yml?label=workflow" alt="Workflow Status"/>
  <img src="https://img.shields.io/github/license/ariefwindhiarto/raw-mikrotik" alt="License"/>

  <br/>

  <img src="https://img.shields.io/badge/domain%20ML-4-orange"/>
  <img src="https://img.shields.io/badge/domain%20WA-5-blue"/>
  <img src="https://img.shields.io/badge/domain%20STORE-12-yellow"/>
  <img src="https://img.shields.io/badge/IP%20Store-20-lightgrey"/>
</p>

---

## 📁 Daftar File

| Nama File | Deskripsi | Link RAW |
|-----------|-----------|----------|
| `ip-mobilelegends.rsc` | Daftar IP Mobile Legends untuk MikroTik (.rsc) | [Raw Link](https://raw.githubusercontent.com/ariefwindhiarto/raw-mikrotik/main/raw/ip-mobilelegends.rsc) |
| `ip-mobilelegends.txt` | Format TXT Mobile Legends | [Raw Link](https://raw.githubusercontent.com/ariefwindhiarto/raw-mikrotik/main/raw/ip-mobilelegends.txt) |
| `ip-whatsapp.rsc` | Daftar IP WhatsApp (.rsc) | [Raw Link](https://raw.githubusercontent.com/ariefwindhiarto/raw-mikrotik/main/raw/ip-whatsapp.rsc) |
| `ip-whatsapp.txt` | Format TXT WhatsApp | [Raw Link](https://raw.githubusercontent.com/ariefwindhiarto/raw-mikrotik/main/raw/ip-whatsapp.txt) |
| `ip-store.rsc` | Daftar IP Shopee, Tokopedia, Lazada, DANA, OVO (.rsc) | [Raw Link](https://raw.githubusercontent.com/ariefwindhiarto/raw-mikrotik/main/raw/ip-store.rsc) |
| `ip-store.txt` | Format TXT e-Commerce & Dompet Digital | [Raw Link](https://raw.githubusercontent.com/ariefwindhiarto/raw-mikrotik/main/raw/ip-store.txt) |

---

## ⚙️ Cara Pakai (untuk MikroTik)

**Tambahkan scheduler ke MikroTik:**

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

Untuk Shopee, Tokopedia, Lazada, DANA, OVO:
```rsc
/system scheduler
add interval=1d name=update-store on-event="/tool fetch url=\"https://raw.githubusercontent.com/ariefwindhiarto/raw-mikrotik/main/raw/ip-store.rsc\" dst-path=store.rsc mode=https\n/import file-name=store.rsc"
```

---

## 🔧 Struktur Folder

```bash
raw-mikrotk/
├── README.md
├── raw/
│   ├── ip-mobilelegends.rsc
│   ├── ip-mobilelegends.txt
│   ├── ip-whatsapp.rsc
│   ├── ip-whatsapp.txt
│   ├── ip-store.rsc
│   └── ip-store.txt
├── .github/
│   └── workflows/
│       └── update-ips.yml
├── scripts/
│   ├── resolve-ml.py
│   ├── resolve-wa.py
│   └── resolve-store.py
├── domains-ml.txt
├── domains-wa.txt
└── domains-store.txt
```

---

## 🎯 Tujuan Proyek

- Menyediakan sistem resolver IP otomatis berbasis GitHub Actions
- Meningkatkan efisiensi admin jaringan MikroTik untuk aplikasi populer
- Mengurangi delay dan optimasi rute koneksi (QoS, firewall, atau Mangle)

---

## 🙏 Kontribusi

Silakan *fork* dan ajukan *pull request* untuk menambahkan:
- Domain baru
- Format tambahan (JSON, CSV, dst)
- Penyempurnaan workflow & logger

---

## 📊 Statistik Harian (Dari Workflow)

- Total domain diproses: **21+**
- Daftar IP unik tersimpan: Lihat file `.txt` masing-masing
- Update terakhir: Ditangani otomatis setiap hari pukul 03:00 UTC

> Jika domain tidak berhasil di-resolve (gagal DNS), akan dilewati secara aman.

---

## 📄 Lisensi

Repositori ini bersifat **open-source** untuk pembelajaran, eksperimen teknis, dan kontribusi komunitas. Silakan modifikasi dengan bijak.
