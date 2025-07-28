# 🛡️ OJS Path Scanner

**OJS Path Scanner** adalah alat untuk melakukan pengecekan path sensitif pada website berbasis **Open Journal Systems (OJS)**. Tujuannya untuk mengidentifikasi direktori terbuka, file sensitif, dan potensi celah keamanan yang umum pada sistem jurnal daring.

---

## 📦 Fitur

- Deteksi direktori terbuka (Index of)
- Cek status `200 OK`, `403 Forbidden`, dan lainnya
- Multi-threaded (cepat & efisien)
- Output otomatis ke file
- Dukungan HTTP/HTTPS
- Tampilan CLI dengan warna & banner

---

## 🚀 Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/ojs-path-scanner.git
cd ojs-path-scanner
pip install requests colorama pyfiglet
python3 ojs.py
```

Credit : @yourdre4m7
