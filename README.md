# groq-api
Aplikasi python flask sederhana, untuk memproses permintaan API endpoin from user

## **Petunjuk Lengkap Aplikasi groq-API**

### **1. Deskripsi Aplikasi groq-API**
groq-API adalah aplikasi flask python sederhana yang menggunakan model AI Groq untuk memproses permintaan endpoint API dari pengguna. 

Fitur utama aplikasi:
- Menerima input teks (`msg`) melalui parameter query.
- Memilih model AI berdasarkan parameter `model`.
- Mengembalikan respons JSON berisi hasil pemrosesan dari model AI.

---

### **2. Persyaratan Sistem**

#### **a. Lokal (PC/Laptop):**
- **Sistem Operasi**: Linux, macOS, atau Windows.
- **Python**: Versi 3.8 atau lebih baru (jika tidak menggunakan Docker).
  - Unduh Python: [https://www.python.org/](https://www.python.org/)
- **Docker**: Instal Docker Desktop (Windows/macOS) atau Docker Engine (Linux) jika ingin menggunakan Docker.
  - Unduh Docker: [https://www.docker.com/](https://www.docker.com/)
- **Git** (opsional): Untuk mengunduh kode dari repository Git.
- **Groq API Key**: Diperlukan untuk mengakses layanan Groq.
  - Dapatkan API key dari [https://console.groq.com/](https://console.groq.com/) (lihat petunjuk di bawah).

#### **b. Server/Cloud:**
- **Sistem Operasi**: Linux (Ubuntu/Debian lebih disarankan).
- **Python**: Versi 3.8 atau lebih baru (jika tidak menggunakan Docker).
- **Docker**: Instal Docker Engine jika ingin menggunakan Docker.
- **Port 8080**: Pastikan port 8080 tidak diblokir oleh firewall.
- **Groq API Key**: Diperlukan untuk mengakses layanan Groq.

---

### **3. Struktur Direktori**
Pastikan struktur direktori proyek Anda terlihat seperti ini:

```
project/
├── api.py                # File utama aplikasi Flask
├── Dockerfile            # File untuk membangun image Docker (opsional)
├── requirements.txt      # Daftar dependensi Python
├── .env                  # File untuk menyimpan environment variable
├── docker-compose.yml    # File untuk menjalankan aplikasi dengan Docker Compose (opsional)
├── .dockerignore         # File untuk mengecualikan file dari image Docker (opsional)
└── .gitignore            # File untuk mengecualikan file dari Git
```

---

### **4. Langkah-Langkah Penggunaan**

#### **a. Clone Repository (Opsional)**
Jika Anda menggunakan repository Git, clone proyek ke direktori lokal:

```bash
git clone https://github.com/MuhammadGagah/groq-api.git
cd groq-api
```

#### **b. Konfigurasi File `.env`**
Buat file `.env` di direktori groq-api dan isi dengan nilai berikut:

```env
FLASK_DEBUG=False
GROQ_API_KEY=your_groq_API_key_here
```

> **Catatan**: Ganti `your_groq_API_key_here` dengan API key Groq Anda. Jika belum memiliki API key, ikuti petunjuk di bawah untuk mendapatkannya.

---

### **5. Cara Mendapatkan Groq API Key**

Untuk menggunakan layanan Groq, Anda memerlukan API key. Berikut adalah langkah-langkah untuk mendapatkannya:

#### **Langkah 1: Daftar Akun di Groq**
1. Kunjungi [https://console.groq.com/](https://console.groq.com/).
2. Klik tombol **Sign Up** atau **Log In** jika Anda sudah memiliki akun.
3. Isi formulir pendaftaran dengan alamat email dan kata sandi Anda.

#### **Langkah 2: Masuk ke Dashboard**
Setelah berhasil mendaftar atau masuk, Anda akan diarahkan ke dashboard Groq.

#### **Langkah 3: Dapatkan API Key**
1. Di dashboard Groq, navigasikan ke bagian **API Keys**.
2. Klik tombol **Create API Key** atau **Generate API Key**.
3. Salin API key yang dihasilkan dan simpan di tempat yang aman.

#### **Langkah 4: Tambahkan API Key ke File `.env`**
Salin API key yang Anda dapatkan ke file `.env` di proyek Anda:

```env
GROQ_API_KEY=your_groq_API_key_here
```

---

### **6. Cara Menjalankan Aplikasi**

#### **Metode 1: Tanpa Docker**

##### **Langkah 1: Instal Dependensi Python**
1. **Buat Virtual Environment (Opsional tapi Disarankan)**:
   ```bash
   python3 -m venv venv
   ```

2. **Aktifkan Virtual Environment**:
   - **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```

3. **Instal Dependensi**:
   Gunakan file `requirements.txt` untuk menginstal semua dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

   > **Catatan**: Pastikan file `requirements.txt` berisi dependensi berikut:
   ```
   flask
   groq
   requests
   python-dotenv
   ```

##### **Langkah 2: Jalankan Aplikasi**
Gunakan perintah berikut untuk menjalankan aplikasi Flask:

```bash
python api.py
```

Outputnya akan terlihat seperti ini:
```
 * Serving Flask app 'api'
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
```

---

#### **Metode 2: Dengan Docker**

##### **Langkah 1: Build dan Jalankan Container**
Anda dapat menjalankan aplikasi menggunakan salah satu metode berikut:

###### **Opsi 1: Menggunakan Docker CLI**
1. **Build Image**:
   ```bash
   docker build -t groq-api .
   ```

2. **Jalankan Container**:
   ```bash
   docker run -d -p 8080:8080 --restart unless-stopped \
     --env-file .env \
     --name groq-api-container groq-api
   ```

3. **Verifikasi**:
   Cek status container:
   ```bash
   docker ps
   ```

###### **Opsi 2: Menggunakan Docker Compose**
1. **Install Docker Compose**:
   Pastikan Docker Compose sudah terinstal. Jika belum, instal dengan perintah berikut (Linux):
   ```bash
   sudo apt-get install docker-compose-plugin
   ```

2. **Jalankan Aplikasi**:
   Gunakan perintah berikut untuk membangun image (jika belum tersedia) dan menjalankan container:
   ```bash
   docker compose up -d
   ```

3. **Verifikasi**:
   Cek status container:
   ```bash
   docker ps
   ```

---

### **7. Cara Menggunakan API**

#### **a. Endpoint Utama**
API memiliki satu endpoint utama:

```
GET /
```

#### **b. Parameter Query**
- **`msg`** (wajib): Pesan atau pertanyaan yang ingin diproses oleh model AI.
- **`model`** (opsional): Nama model AI yang ingin digunakan. Default: `llama`.

Contoh nilai `model` yang valid:
- `deepseek-r1`
- `llama`
- `mixtral`
- `gemma2`
- `llama70b`

#### **c. Contoh Permintaan**
Gunakan browser, Postman, atau `curl` untuk mengirim permintaan ke API.

##### **Contoh 1: Menggunakan Browser**
```
http://localhost:8080/?msg=Halo%20AI&model=llama
```

##### **Contoh 2: Menggunakan Curl**
```bash
curl "http://localhost:8080/?msg=Halo%20AI&model=llama"
```

##### **Contoh 3: Menggunakan Postman**
1. Buka Postman.
2. Pilih metode `GET`.
3. Masukkan URL:
   ```
   http://localhost:8080/?msg=Halo%20AI&model=llama
   ```
4. Klik tombol "Send".

#### **d. Contoh Respons**
Respons API berupa JSON dengan format berikut:

```json
{
  "developer": "Muhammad Gagah",
  "model": "llama",
  "message": "Halo! Ada yang bisa saya bantu?"
}
```

---

### **8. Menjalankan di Lingkungan Berbeda**

#### **a. Lokal**
Ikuti langkah-langkah di atas untuk menjalankan aplikasi di PC/laptop Anda.

#### **b. Server**
1. **Upload Proyek ke Server**:
   Gunakan SCP atau Git untuk mengupload proyek ke server:
   ```bash
   scp -r project/ user@server-ip:/path/to/destination
   ```

2. **SSH ke Server**:
   ```bash
   ssh user@server-ip
   ```

3. **Pilih Metode**:
   - **Tanpa Docker**: Ikuti langkah-langkah pada **Metode 1**.
   - **Dengan Docker**: Ikuti langkah-langkah pada **Metode 2**.

4. **Akses API**:
   Ganti `localhost` dengan alamat IP server:
   ```
   http://server-ip:8080/?msg=Halo%20AI&model=llama
   ```

#### **c. Cloud (AWS, Google Cloud, Azure)**
1. **Deploy di Instance Cloud**:
   - Buat instance VM di AWS, Google Cloud, atau Azure.
   - Install Python dan dependensi (untuk metode tanpa Docker) atau Docker (untuk metode dengan Docker).

2. **Upload Proyek**:
   Gunakan SCP atau Git untuk mengupload proyek ke instance cloud.

3. **Jalankan Aplikasi**:
   - **Tanpa Docker**: Ikuti langkah-langkah pada **Metode 1**.
   - **Dengan Docker**: Ikuti langkah-langkah pada **Metode 2**.

4. **Akses API**:
   Gunakan alamat IP publik instance cloud:
   ```
   http://public-ip:8080/?msg=Halo%20AI&model=llama
   ```

---

### **9. Tips Tambahan**

#### **a. Keamanan**
- Pastikan file `.env` tidak termasuk dalam docker image (jika anda menggunakan docker, buat file  `.dockerignore`, dan isi .env).
- Gunakan HTTPS jika aplikasi diakses melalui internet.

#### **b. Logging**
- **Tanpa Docker**: Semua log akan ditampilkan di terminal tempat aplikasi berjalan.
- **Dengan Docker**: Gunakan perintah berikut untuk melihat log container:
  ```bash
  docker logs groq-api-container
  ```

#### **c. Menjalankan di Background**
- **Tanpa Docker**:
  ```bash
  nohup python api.py > app.log 2>&1 &
  ```
- **Dengan Docker**:
  Gunakan `docker compose up -d` atau `docker run -d` untuk menjalankan container di background.

#### **d. Membersihkan Sumber Daya**
- **Tanpa Docker**: Hentikan aplikasi dengan menekan `CTRL+C` di terminal.
- **Dengan Docker**:
  ```bash
  docker compose down
  ```

---

### **10. Thank You**
Selamat mencoba aplikasi groq-API ini, jika menemukan bug atau ingin fix something, jangan ragu untuk create issue dan PR!
