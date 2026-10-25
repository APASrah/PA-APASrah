# 🎪 Sistem Reservasi Tenant Bazar

Aplikasi **CLI (Command Line Interface)** berbasis Python untuk mengelola reservasi lapak/tenant bazar. Dilengkapi sistem **login & registrasi**, **e-money (saldo & top up)**, **pembayaran reservasi**, **invoice otomatis**, **riwayat transaksi**, dan **laporan ringkas admin**. Seluruh data disimpan dalam file **JSON**.

---

## 📑 Daftar Isi

1. [Fitur Utama](#-fitur-utama)
2. [Teknologi & Library](#-teknologi--library)
3. [Struktur Folder & File Data](#-struktur-folder--file-data)
4. [Cara Menjalankan](#-cara-menjalankan)
5. [Penjelasan Kode (Kiri: Kode, Kanan: Penjelasan)](#-penjelasan-kode)
   - [1. Import & Konfigurasi](#1-import--konfigurasi)
   - [2. Memuat Data dari JSON](#2-memuat-data-dari-json)
   - [3. Fungsi Bantu](#3-fungsi-bantu)
   - [4. Pencatatan Transaksi](#4-pencatatan-transaksi)
   - [5. Autentikasi (Login & Registrasi)](#5-autentikasi-login--registrasi)
   - [6. Manajemen Data Tenant (CRUD)](#6-manajemen-data-tenant-crud)
   - [7. E-Money (Saldo & Top Up)](#7-e-money-saldo--top-up)
   - [8. Invoice & Reservasi](#8-invoice--reservasi)
   - [9. Riwayat, Cetak Ulang & Laporan](#9-riwayat-cetak-ulang--laporan)
   - [10. Menu Admin, Menu User & Main](#10-menu-admin-menu-user--main)
6. [Format File JSON](#-format-file-json)
7. [Catatan & Pengembangan Lanjutan](#-catatan--pengembangan-lanjutan)

---

## ✨ Fitur Utama

| Role | Fitur |
|------|-------|
| **Umum** | Login (maks. 3 percobaan), Registrasi akun baru, input password tersembunyi |
| **Admin** | Tambah / lihat / ubah / hapus tenant, riwayat seluruh transaksi, laporan ringkas, cetak ulang invoice |
| **User** | Lihat tenant, cek & top up saldo, reservasi + bayar pakai saldo, riwayat pribadi, cetak ulang invoice |

---

## 🛠 Teknologi & Library

| Library | Fungsi |
|---------|--------|
| `os` | Membersihkan layar & membuat folder |
| `time` | Memberi jeda agar pesan terbaca |
| `json` | Membaca & menyimpan data |
| `random` | Membuat angka acak untuk kode transaksi |
| `datetime` | Mengambil waktu saat ini |
| `prettytable` | Menampilkan data dalam bentuk tabel |
| `pwinput` | Input password tampil sebagai `*` |

Instalasi library tambahan:

```bash
pip install prettytable pwinput
```

---

## 📂 Struktur Folder & File Data

```
C:\ApasProjek\
├── users.json        # data akun (wajib ada)
├── tenants.json      # data tenant (wajib ada)
├── transaksi.json    # riwayat transaksi (dibuat otomatis)
└── invoice\          # folder invoice .txt (dibuat otomatis)
    └── TRX-xxxxxxxxxxxx-xxx.txt
```

---

## ▶ Cara Menjalankan

1. Pastikan Python 3 sudah terpasang.
2. Install library: `pip install prettytable pwinput`.
3. Buat folder `C:\ApasProjek` lalu isi `users.json` dan `tenants.json` (contoh format ada di bagian [Format File JSON](#-format-file-json)).
4. Jalankan program:

```bash
python nama_file.py
```

---

## 📖 Penjelasan Kode

> Tabel di bawah menampilkan **kode di kolom kiri** dan **penjelasannya di kolom kanan**.

### 1. Import & Konfigurasi

<table>
<tr>
<th width="50%">Kode</th>
<th width="50%">Penjelasan</th>
</tr>
<tr>
<td valign="top">

```python
import os
import time
import json
import random
from datetime import datetime
from prettytable import PrettyTable
import pwinput
```

</td>
<td valign="top">

Mengimpor seluruh library yang dibutuhkan:

- `os` → perintah sistem (clear screen, buat folder).
- `time` → fungsi `sleep()` untuk jeda.
- `json` → baca/tulis file JSON.
- `random` → angka acak untuk kode transaksi.
- `datetime` → waktu transaksi.
- `PrettyTable` → tabel rapi di terminal.
- `pwinput` → input password yang disamarkan.

</td>
</tr>
<tr>
<td valign="top">

```python
folder_data = r"C:\ApasProjek"
path_users = folder_data + r"\users.json"
path_tenants = folder_data + r"\tenants.json"
path_transaksi = folder_data + r"\transaksi.json"
folder_invoice = folder_data + r"\invoice"
```

</td>
<td valign="top">

Menentukan **lokasi penyimpanan data**.

- Awalan `r"..."` (raw string) membuat tanda `\` tidak dianggap karakter escape.
- Semua path dibentuk dari satu `folder_data`, jadi jika ingin memindah folder cukup ubah satu baris.

</td>
</tr>
<tr>
<td valign="top">

```python
KATEGORI = ("Makanan", "Minuman", "Fashion", "Kerajinan", "Lainnya")

MIN_TOPUP = 10000
MAX_TOPUP = 10000000
```

</td>
<td valign="top">

**Konstanta program.**

- `KATEGORI` berupa **tuple** (isinya tidak bisa diubah) berisi daftar kategori tenant yang valid.
- `MIN_TOPUP` → batas minimal top up (Rp 10.000).
- `MAX_TOPUP` → batas maksimal top up per transaksi (Rp 10.000.000).

Penulisan huruf kapital menandakan nilai ini konstan.

</td>
</tr>
</table>

---

### 2. Memuat Data dari JSON

<table>
<tr>
<th width="50%">Kode</th>
<th width="50%">Penjelasan</th>
</tr>
<tr>
<td valign="top">

```python
try:
    with open(path_users, "r", encoding="utf-8") as f:
        users = json.load(f)
    with open(path_tenants, "r", encoding="utf-8") as f:
        tenants = json.load(f)
except FileNotFoundError:
    print("File data tidak ditemukan! Pastikan users.json dan tenants.json ada.")
    exit()
except json.JSONDecodeError:
    print("Isi file JSON rusak atau kosong!")
    exit()
```

</td>
<td valign="top">

Membaca `users.json` dan `tenants.json` ke dalam variabel Python.

- `users` → **dictionary** (kunci = username).
- `tenants` → **list** berisi dictionary tenant.
- `FileNotFoundError` → file tidak ada, program berhenti.
- `JSONDecodeError` → isi file rusak/kosong, program berhenti.
- `with open(...)` otomatis menutup file setelah selesai.

</td>
</tr>
<tr>
<td valign="top">

```python
# transaksi.json dibuat otomatis kalau belum ada
try:
    with open(path_transaksi, "r", encoding="utf-8") as f:
        transaksi = json.load(f)
except FileNotFoundError:
    transaksi = []
except json.JSONDecodeError:
    print("Isi transaksi.json rusak!")
    exit()
```

</td>
<td valign="top">

Memuat riwayat transaksi.

- Jika file **belum ada**, tidak dianggap error: `transaksi` dimulai dari list kosong `[]` (file akan dibuat saat transaksi pertama disimpan).
- Jika file **rusak**, program berhenti agar data tidak tertimpa.

</td>
</tr>
<tr>
<td valign="top">

```python
for t in tenants:
    if "stok" not in t:
        t["stok"] = 1
for nama_user in users:
    if "saldo" not in users[nama_user]:
        users[nama_user]["saldo"] = 0
```

</td>
<td valign="top">

**Migrasi data lama** agar kompatibel dengan fitur baru.

- Tenant lama yang belum punya `stok` diberi stok `1`.
- User lama yang belum punya `saldo` diberi saldo `0`.

Sehingga file lama tetap bisa dipakai tanpa error `KeyError`.

</td>
</tr>
</table>

---

### 3. Fungsi Bantu

<table>
<tr>
<th width="50%">Kode</th>
<th width="50%">Penjelasan</th>
</tr>
<tr>
<td valign="top">

```python
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")
```

</td>
<td valign="top">

**Membersihkan layar terminal.**

- `os.name == "nt"` → Windows → pakai `cls`.
- Selain itu (Linux/Mac) → pakai `clear`.

</td>
</tr>
<tr>
<td valign="top">

```python
def jeda():
    time.sleep(1.5)
```

</td>
<td valign="top">

Menahan program **1,5 detik** supaya pesan (berhasil/gagal) sempat dibaca sebelum layar dibersihkan.

</td>
</tr>
<tr>
<td valign="top">

```python
def rupiah(angka):
    return "Rp " + format(angka, ",").replace(",", ".")
```

</td>
<td valign="top">

**Format angka menjadi Rupiah.**

- `format(15000, ",")` → `"15,000"`.
- `.replace(",", ".")` → `"15.000"`.
- Hasil akhir: `Rp 15.000`.

</td>
</tr>
<tr>
<td valign="top">

```python
def input_angka(pesan, minimal=0):
    while True:
        try:
            angka = int(input(pesan))
            if angka < minimal:
                print("Nilai minimal adalah", minimal)
            else:
                return angka
        except ValueError:
            print("Input harus angka!")
```

</td>
<td valign="top">

**Input angka yang aman.**

- Perulangan `while True` terus meminta input sampai valid.
- `int()` gagal (huruf/kosong) → `ValueError` → pesan "Input harus angka!".
- Angka di bawah `minimal` → ditolak.
- Parameter `minimal` default `0`, bisa diganti (mis. `1`).

</td>
</tr>
<tr>
<td valign="top">

```python
def konfirmasi(pesan):
    while True:
        jawab = input(pesan + " (y/n) : ").lower()
        if jawab == "y":
            return True
        if jawab == "n":
            return False
        print("Jawab dengan y atau n saja!")
```

</td>
<td valign="top">

**Konfirmasi ya/tidak.**

- `.lower()` membuat `Y` dan `y` sama saja.
- Mengembalikan `True` untuk `y`, `False` untuk `n`.
- Jawaban lain → diulang terus.

</td>
</tr>
<tr>
<td valign="top">

```python
def simpan_data(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
```

</td>
<td valign="top">

**Menyimpan data ke JSON.**

- Mode `"w"` menulis ulang seluruh isi file.
- `indent=4` membuat file rapi dan mudah dibaca manusia.
- Dipakai ulang oleh users, tenants, dan transaksi.

</td>
</tr>
</table>

---

### 4. Pencatatan Transaksi

<table>
<tr>
<th width="50%">Kode</th>
<th width="50%">Penjelasan</th>
</tr>
<tr>
<td valign="top">

```python
def buat_kode():
    while True:
        kode = "TRX-" + datetime.now().strftime("%y%m%d%H%M%S") + "-" + str(random.randint(100, 999))
        ada = False
        for t in transaksi:
            if t["kode"] == kode:
                ada = True
        if not ada:
            return kode
```

</td>
<td valign="top">

**Membuat kode transaksi unik**, contoh: `TRX-261025153200-482`.

- `TRX-` + tanggal-jam (`yyMMddHHmmss`) + 3 angka acak.
- Dicek ke seluruh riwayat; jika kebetulan sudah ada, kode dibuat ulang.
- Hanya mengembalikan kode yang **belum pernah dipakai**.

</td>
</tr>
<tr>
<td valign="top">

```python
def catat_transaksi(username, tipe, tenant, jumlah, qty, saldo_akhir):
    trx = {
        "kode": buat_kode(),
        "waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "username": username,
        "tipe": tipe,
        "tenant_id": tenant["id"] if tenant else 0,
        "tenant_nama": tenant["nama"] if tenant else "-",
        "qty": qty,
        "jumlah": jumlah,
        "saldo_akhir": saldo_akhir
    }
    transaksi.append(trx)
    simpan_data(path_transaksi, transaksi)
    return trx
```

</td>
<td valign="top">

**Mencatat satu transaksi** dan langsung menyimpannya.

- `tipe` bernilai `"Top Up"` atau `"Reservasi"`.
- Untuk **Top Up**, `tenant=None` sehingga `tenant_id = 0` dan `tenant_nama = "-"`.
- `saldo_akhir` menyimpan sisa saldo setelah transaksi.
- Data ditambahkan ke list `transaksi`, ditulis ke file, lalu dikembalikan (`return trx`) agar bisa dipakai untuk mencetak invoice.

</td>
</tr>
</table>

---

### 5. Autentikasi (Login & Registrasi)

<table>
<tr>
<th width="50%">Kode</th>
<th width="50%">Penjelasan</th>
</tr>
<tr>
<td valign="top">

```python
def login():
    print("\n=== LOGIN ===")
    percobaan = 0
    while percobaan < 3:
        try:
            username = input("Username : ")
            password = pwinput.pwinput("Password : ")

            if username in users and users[username]["password"] == password:
                print("Login berhasil")
                jeda()
                return username
            else:
                percobaan = percobaan + 1
                print("Username atau password salah! Sisa percobaan :", 3 - percobaan)

        except KeyboardInterrupt:
            print("\nProses dibatalkan (dilarang mengisi memakai Ctrl+C)")
            percobaan = percobaan + 1
            print("Sisa percobaan :", 3 - percobaan)

    return ""
```

</td>
<td valign="top">

**Proses login dengan batas 3 kali percobaan.**

- Password diinput lewat `pwinput` (tampil `*`).
- Username harus ada **dan** password harus cocok.
- Berhasil → mengembalikan `username`.
- Salah → hitungan `percobaan` bertambah dan sisa percobaan ditampilkan.
- Menekan `Ctrl+C` ditangkap (`KeyboardInterrupt`) dan **tetap dihitung sebagai percobaan**, sehingga tidak bisa dipakai untuk kabur dari login.
- Setelah 3 kali gagal → mengembalikan string kosong `""`.

</td>
</tr>
<tr>
<td valign="top">

```python
def registrasi():
    print("\n=== REGISTRASI ===")
    try:
        username = input("Username : ").strip()
        password = pwinput.pwinput("Password : ")

        if username == "":
            print("Username tidak boleh kosong!")
            return ""
        if " " in username:
            print("Username tidak boleh mengandung spasi!")
            return ""
        if username in users:
            print("Username sudah dipakai!")
            return ""
        if password == "":
            print("Password tidak boleh kosong!")
            return ""
        users[username] = {"password": password, "role": "user", "saldo": 0}
        simpan_data(path_users, users)
        print("Registrasi berhasil! Silakan login.")
    except KeyboardInterrupt:
        print("\nProses registrasi dibatalkan (dilarang mengisi memakai Ctrl+C)")

    return ""
```

</td>
<td valign="top">

**Pendaftaran akun baru dengan validasi.**

Aturan yang dicek berurutan:

1. Username tidak boleh kosong.
2. Username tidak boleh mengandung spasi.
3. Username belum dipakai orang lain.
4. Password tidak boleh kosong.

Jika lolos, akun dibuat dengan **role `user`** dan **saldo `0`**, lalu disimpan ke `users.json`. Akun admin tidak bisa dibuat lewat registrasi (harus diisi manual di file JSON).

</td>
</tr>
</table>

---

### 6. Manajemen Data Tenant (CRUD)

<table>
<tr>
<th width="50%">Kode</th>
<th width="50%">Penjelasan</th>
</tr>
<tr>
<td valign="top">

```python
def pilih_kategori():
    print("1. Makanan  2. Minuman  3. Fashion  4. Kerajinan  5. Lainnya")
    while True:
        nomor = input_angka("Pilih kategori (1-5) : ")
        if 1 <= nomor <= 5:
            return KATEGORI[nomor - 1]
        print("Nomor tidak ada.")
```

</td>
<td valign="top">

**Memilih kategori lewat nomor.**

- Input diulang sampai angka 1–5.
- `KATEGORI[nomor - 1]` mengambil nama kategori (indeks tuple dimulai dari 0).
- Mencegah salah ketik nama kategori.

</td>
</tr>
<tr>
<td valign="top">

```python
def cari_index(id_tenant):
    index = 0
    for tenant in tenants:
        if tenant["id"] == id_tenant:
            return index
        index = index + 1
    raise ValueError("ID tidak ditemukan!")
```

</td>
<td valign="top">

**Mencari posisi (index) tenant berdasarkan ID.**

- Menelusuri list satu per satu.
- Ketemu → mengembalikan index.
- Tidak ketemu → `raise ValueError(...)` (sengaja melempar error) yang nanti ditangkap oleh fungsi pemanggil dengan `try/except`.

</td>
</tr>
<tr>
<td valign="top">

```python
def perbarui_status(tenant):
    if tenant["stok"] > 0:
        tenant["status"] = "Tersedia"
    else:
        tenant["status"] = "Penuh"
```

</td>
<td valign="top">

**Status otomatis mengikuti stok.**

- Stok &gt; 0 → `Tersedia`.
- Stok 0 → `Penuh`.

Admin tidak perlu mengisi status manual sehingga data selalu konsisten.

</td>
</tr>
<tr>
<td valign="top">

```python
def tampilkan_data():
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Tenant", "Kategori", "Harga Sewa", "Stok", "Status"]
    for t in tenants:
        tabel.add_row([t["id"], t["nama"], t["kategori"], rupiah(t["harga"]), t["stok"], t["status"]])
    print(tabel)
```

</td>
<td valign="top">

**Menampilkan seluruh tenant dalam tabel.**

- Membuat objek `PrettyTable`, menentukan judul kolom.
- Tiap tenant ditambahkan sebagai satu baris; harga diformat dengan `rupiah()`.
- Dipakai oleh admin dan user.

</td>
</tr>
<tr>
<td valign="top">

```python
def tambah_data():
    print("\n=== TAMBAH DATA TENANT ===")
    nama = input("Nama Tenant : ").strip()
    if nama == "":
        print("Nama tidak boleh kosong!")
        return
    for tenant in tenants:
        if tenant["nama"].lower() == nama.lower():
            print("Tenant sudah ada!")
            return

    kategori = pilih_kategori()
    harga = input_angka("Harga sewa (Rp) : ", 1)
    stok = input_angka("Stok lapak : ", 0)
```

</td>
<td valign="top">

**CREATE – bagian input.**

- `.strip()` membuang spasi di awal/akhir.
- Nama kosong ditolak.
- Cek duplikat **tanpa membedakan huruf besar/kecil** (`.lower()`).
- Harga minimal `1`, stok minimal `0`.

</td>
</tr>
<tr>
<td valign="top">

```python
    id_baru = 1
    for tenant in tenants:
        if tenant["id"] >= id_baru:
            id_baru = tenant["id"] + 1

    tenant_baru = {"id": id_baru, "nama": nama, "kategori": kategori, "harga": harga, "stok": stok, "status": "Tersedia"}
    perbarui_status(tenant_baru)
    tenants.append(tenant_baru)
    simpan_data(path_tenants, tenants)
    print("Data tenant berhasil ditambahkan!")
```

</td>
<td valign="top">

**CREATE – bagian penyimpanan.**

- **ID otomatis**: mencari ID terbesar lalu ditambah 1, jadi ID tidak bentrok walau ada tenant yang dihapus.
- Membuat dictionary tenant baru, status disesuaikan stok lewat `perbarui_status()`.
- Ditambahkan ke list dan disimpan ke `tenants.json`.

</td>
</tr>
<tr>
<td valign="top">

```python
def ubah_data():
    print("\n=== UBAH DATA TENANT ===")
    tampilkan_data()
    id_tenant = input_angka("Masukkan ID tenant : ")

    try:
        index = cari_index(id_tenant)
    except ValueError as e:
        print(e)
        return

    nama = input("Nama baru : ").strip()
    if nama == "":
        print("Nama tidak boleh kosong!")
        return
    kategori = pilih_kategori()
    harga = input_angka("Harga sewa baru (Rp) : ", 1)
    stok = input_angka("Stok lapak baru : ", 0)

    tenants[index]["nama"] = nama
    tenants[index]["kategori"] = kategori
    tenants[index]["harga"] = harga
    tenants[index]["stok"] = stok
    perbarui_status(tenants[index])
    simpan_data(path_tenants, tenants)
    print("Data tenant berhasil diubah!")
```

</td>
<td valign="top">

**UPDATE – mengubah tenant.**

1. Tampilkan tabel agar admin tahu ID yang tersedia.
2. Cari index dengan `cari_index()`; jika ID salah, error ditangkap (`except ValueError as e`) dan pesannya ditampilkan.
3. Minta data baru (nama, kategori, harga, stok).
4. Timpa nilai lama pada `tenants[index]`.
5. Status diperbarui otomatis dan data disimpan.

</td>
</tr>
<tr>
<td valign="top">

```python
def hapus_data():
    print("\n=== HAPUS DATA TENANT ===")
    tampilkan_data()
    id_tenant = input_angka("Masukkan ID tenant : ")

    try:
        index = cari_index(id_tenant)
    except ValueError as e:
        print(e)
        return

    if not konfirmasi("Yakin ingin menghapus?"):
        print("Penghapusan dibatalkan.")
        return

    tenant = tenants.pop(index)
    simpan_data(path_tenants, tenants)
    print("Tenant", tenant["nama"], "berhasil dihapus!")
```

</td>
<td valign="top">

**DELETE – menghapus tenant.**

- Mencari tenant berdasarkan ID (dengan penanganan error yang sama).
- Meminta **konfirmasi y/n** agar tidak terhapus tidak sengaja.
- `tenants.pop(index)` menghapus dari list sekaligus mengembalikan datanya, sehingga nama tenant bisa ditampilkan di pesan sukses.
- Perubahan disimpan ke file.

</td>
</tr>
</table>

---

### 7. E-Money (Saldo & Top Up)

<table>
<tr>
<th width="50%">Kode</th>
<th width="50%">Penjelasan</th>
</tr>
<tr>
<td valign="top">

```python
def lihat_saldo(username):
    print("\nSaldo Anda :", rupiah(users[username]["saldo"]))
```

</td>
<td valign="top">

Menampilkan saldo user yang sedang login dalam format Rupiah.

</td>
</tr>
<tr>
<td valign="top">

```python
def top_up(username):
    print("\n=== TOP UP SALDO ===")
    print("Saldo saat ini :", rupiah(users[username]["saldo"]))
    print("Minimal top up", rupiah(MIN_TOPUP), "- maksimal", rupiah(MAX_TOPUP))
    nominal = input_angka("Nominal top up (Rp) : ")

    if nominal < MIN_TOPUP:
        print("Top up minimal", rupiah(MIN_TOPUP), "!")
        return
    if nominal > MAX_TOPUP:
        print("Top up maksimal", rupiah(MAX_TOPUP), "per transaksi!")
        return
```

</td>
<td valign="top">

**Top up – bagian validasi.**

- Menampilkan saldo dan batas top up.
- Nominal di bawah `MIN_TOPUP` atau di atas `MAX_TOPUP` ditolak, lalu fungsi berhenti (`return`).

</td>
</tr>
<tr>
<td valign="top">

```python
    if not konfirmasi("Lanjutkan top up " + rupiah(nominal) + "?"):
        print("Top up dibatalkan.")
        return

    users[username]["saldo"] = users[username]["saldo"] + nominal
    simpan_data(path_users, users)
    trx = catat_transaksi(username, "Top Up", None, nominal, 1, users[username]["saldo"])
    print("Top up berhasil! Saldo sekarang :", rupiah(users[username]["saldo"]))
    print("Kode transaksi :", trx["kode"])
```

</td>
<td valign="top">

**Top up – bagian eksekusi.**

1. Meminta konfirmasi y/n.
2. Saldo user ditambah nominal.
3. Saldo disimpan ke `users.json`.
4. Transaksi dicatat bertipe `"Top Up"` (tanpa tenant → `None`).
5. Menampilkan saldo baru dan kode transaksi.

</td>
</tr>
</table>

---

### 8. Invoice & Reservasi

<table>
<tr>
<th width="50%">Kode</th>
<th width="50%">Penjelasan</th>
</tr>
<tr>
<td valign="top">

```python
def cetak_invoice(trx):
    garis = "=" * 44
    baris = [
        garis,
        "        INVOICE RESERVASI TENANT BAZAR",
        garis,
        "Kode Transaksi : " + trx["kode"],
        "Waktu          : " + trx["waktu"],
        "Pelanggan      : " + trx["username"],
        "-" * 44,
        "Tenant         : " + trx["tenant_nama"],
        "Jumlah Lapak   : " + str(trx["qty"]),
        "Total Bayar    : " + rupiah(trx["jumlah"]),
        "Sisa Saldo     : " + rupiah(trx["saldo_akhir"]),
        garis,
        "   Terima kasih telah melakukan reservasi",
        garis
    ]
    for b in baris:
        print(b)
```

</td>
<td valign="top">

**Invoice – tampil di layar.**

- `"=" * 44` membuat garis dari 44 tanda sama dengan.
- Isi invoice disusun sebagai **list baris** (`baris`), lalu dicetak satu per satu.
- `str(trx["qty"])` mengubah angka menjadi teks agar bisa digabung dengan `+`.
- Menggunakan list memudahkan untuk dipakai ulang saat menyimpan ke file.

</td>
</tr>
<tr>
<td valign="top">

```python
    try:
        os.makedirs(folder_invoice, exist_ok=True)
        nama_file = folder_invoice + "\\" + trx["kode"] + ".txt"
        with open(nama_file, "w", encoding="utf-8") as f:
            f.write("\n".join(baris))
        print("Invoice tersimpan di :", nama_file)
    except OSError:
        print("Invoice gagal disimpan ke file, tetapi transaksi tetap tercatat.")
```

</td>
<td valign="top">

**Invoice – simpan ke file `.txt`.**

- `os.makedirs(..., exist_ok=True)` membuat folder invoice jika belum ada (tidak error bila sudah ada).
- Nama file = kode transaksi, misalnya `TRX-...-482.txt`.
- `"\n".join(baris)` menyatukan semua baris dengan pemisah baris baru.
- Jika gagal menulis (`OSError`), program tidak crash dan transaksi tetap aman.

</td>
</tr>
<tr>
<td valign="top">

```python
def reservasi_tenant(username):
    print("\n=== RESERVASI & PEMBAYARAN TENANT ===")
    tampilkan_data()
    print("Saldo Anda :", rupiah(users[username]["saldo"]))
    id_tenant = input_angka("Masukkan ID tenant : ")

    try:
        index = cari_index(id_tenant)
    except ValueError as e:
        print(e)
        return

    tenant = tenants[index]
    if tenant["stok"] <= 0:
        print("Maaf, stok lapak tenant ini sudah habis!")
        return
```

</td>
<td valign="top">

**Reservasi – memilih tenant.**

- Menampilkan daftar tenant dan saldo user.
- Mencari tenant berdasarkan ID; ID salah → pesan error lalu keluar.
- Jika stok `<= 0`, reservasi ditolak.

</td>
</tr>
<tr>
<td valign="top">

```python
    qty = input_angka("Jumlah lapak yang dipesan (maks " + str(tenant["stok"]) + ") : ", 1)
    if qty > tenant["stok"]:
        print("Jumlah melebihi stok yang tersedia!")
        return

    total = tenant["harga"] * qty
    print("Total bayar :", rupiah(total))
    if users[username]["saldo"] < total:
        kurang = total - users[username]["saldo"]
        print("Saldo tidak cukup! Kurang", rupiah(kurang), "- silakan top up dulu.")
        return
```

</td>
<td valign="top">

**Reservasi – validasi jumlah & saldo.**

- Jumlah lapak minimal `1` dan tidak boleh melebihi stok.
- `total = harga × qty`.
- Jika saldo kurang, program menghitung dan menampilkan **selisih kekurangan**, lalu menyarankan top up.

</td>
</tr>
<tr>
<td valign="top">

```python
    if not konfirmasi("Bayar " + rupiah(total) + " dengan saldo?"):
        print("Pembayaran dibatalkan.")
        return

    # saldo dan stok dikurangi (sudah dicek, jadi tidak mungkin negatif)
    users[username]["saldo"] = users[username]["saldo"] - total
    tenant["stok"] = tenant["stok"] - qty
    perbarui_status(tenant)
    simpan_data(path_users, users)
    simpan_data(path_tenants, tenants)

    trx = catat_transaksi(username, "Reservasi", tenant, total, qty, users[username]["saldo"])
    print("\nPembayaran berhasil!\n")
    cetak_invoice(trx)
```

</td>
<td valign="top">

**Reservasi – pembayaran.**

1. Konfirmasi y/n sebelum bayar.
2. Saldo user **dikurangi** total, stok tenant **dikurangi** qty.
3. Status tenant diperbarui (stok habis → `Penuh`).
4. `users.json` dan `tenants.json` disimpan.
5. Transaksi bertipe `"Reservasi"` dicatat.
6. Invoice langsung dicetak dan disimpan.

Karena semua validasi sudah dilakukan sebelumnya, saldo dan stok dijamin tidak negatif.

</td>
</tr>
</table>

---

### 9. Riwayat, Cetak Ulang & Laporan

<table>
<tr>
<th width="50%">Kode</th>
<th width="50%">Penjelasan</th>
</tr>
<tr>
<td valign="top">

```python
def tampilkan_riwayat(username, semua):
    tabel = PrettyTable()
    tabel.field_names = ["Kode", "Waktu", "User", "Tipe", "Tenant", "Qty", "Jumlah", "Saldo Akhir"]
    ada = False
    for t in transaksi:
        if semua or t["username"] == username:
            tabel.add_row([t["kode"], t["waktu"], t["username"], t["tipe"], t["tenant_nama"], t["qty"], rupiah(t["jumlah"]), rupiah(t["saldo_akhir"])])
            ada = True
    if ada:
        print(tabel)
    else:
        print("Belum ada riwayat transaksi.")
```

</td>
<td valign="top">

**Tabel riwayat transaksi.**

- Parameter `semua`:
  - `True` → admin, tampil **semua** transaksi.
  - `False` → user, hanya transaksi **milik sendiri**.
- Variabel `ada` menandai apakah ada baris yang cocok.
- Jika tidak ada → tampil "Belum ada riwayat transaksi."

</td>
</tr>
<tr>
<td valign="top">

```python
def cetak_ulang_invoice(username, semua):
    kode = input("Masukkan kode transaksi : ").strip()
    for t in transaksi:
        if t["kode"] == kode:
            if t["tipe"] != "Reservasi":
                print("Invoice hanya tersedia untuk transaksi reservasi.")
                return
            if not semua and t["username"] != username:
                print("Transaksi tidak ditemukan!")
                return
            cetak_invoice(t)
            return
    print("Transaksi tidak ditemukan!")
```

</td>
<td valign="top">

**Cetak ulang invoice berdasarkan kode.**

- Hanya transaksi `Reservasi` yang punya invoice (Top Up ditolak).
- User biasa hanya boleh mencetak invoice **miliknya**; jika milik orang lain, pesannya dibuat sama dengan "tidak ditemukan" agar data user lain tidak bocor.
- Admin (`semua=True`) boleh mencetak invoice siapa pun.

</td>
</tr>
<tr>
<td valign="top">

```python
def laporan_admin():
    print("\n=== LAPORAN RINGKAS ===")
    total_pendapatan = 0
    jumlah_transaksi = 0
    penjualan = {}

    for t in transaksi:
        if t["tipe"] == "Reservasi":
            total_pendapatan = total_pendapatan + t["jumlah"]
            jumlah_transaksi = jumlah_transaksi + 1
            nama = t["tenant_nama"]
            if nama in penjualan:
                penjualan[nama] = penjualan[nama] + t["qty"]
            else:
                penjualan[nama] = t["qty"]
```

</td>
<td valign="top">

**Laporan admin – menghitung data.**

Hanya transaksi `Reservasi` yang dihitung (top up bukan pendapatan).

- `total_pendapatan` → jumlah seluruh uang reservasi.
- `jumlah_transaksi` → banyaknya reservasi.
- `penjualan` → dictionary `{nama_tenant: total_lapak_dipesan}`.

</td>
</tr>
<tr>
<td valign="top">

```python
    print("Total pendapatan  :", rupiah(total_pendapatan))
    print("Jumlah transaksi  :", jumlah_transaksi, "(reservasi)")

    if len(penjualan) == 0:
        print("Tenant terlaris   : belum ada data")
        return

    terlaris = ""
    terbanyak = 0
    for nama in penjualan:
        if penjualan[nama] > terbanyak:
            terbanyak = penjualan[nama]
            terlaris = nama
    print("Tenant terlaris   :", terlaris, "(" + str(terbanyak) + " lapak dipesan)")

    tabel = PrettyTable()
    tabel.field_names = ["Tenant", "Lapak Dipesan"]
    for nama in penjualan:
        tabel.add_row([nama, penjualan[nama]])
    print(tabel)
```

</td>
<td valign="top">

**Laporan admin – menampilkan hasil.**

- Menampilkan total pendapatan dan jumlah transaksi.
- Jika belum ada penjualan → tampil "belum ada data" dan fungsi berhenti.
- Mencari **tenant terlaris** dengan mencari nilai terbesar di `penjualan`.
- Menampilkan tabel rekap lapak dipesan per tenant.

</td>
</tr>
</table>

---

### 10. Menu Admin, Menu User & Main

<table>
<tr>
<th width="50%">Kode</th>
<th width="50%">Penjelasan</th>
</tr>
<tr>
<td valign="top">

```python
def menu_admin(username):
    try:
        while True:
            bersihkan_layar()
            print("\n=== MENU ADMIN -", username, "===")
            print("1. Tambah data tenant")
            print("2. Tampilkan data tenant")
            print("3. Ubah data tenant")
            print("4. Hapus data tenant")
            print("5. Riwayat seluruh transaksi")
            print("6. Laporan ringkas")
            print("7. Cetak ulang invoice")
            print("8. Logout")
            pilihan = input("Pilih menu: ")
```

</td>
<td valign="top">

**Menu admin – tampilan.**

- Perulangan menu berjalan terus sampai logout.
- Layar dibersihkan tiap kali menu muncul.
- Admin memiliki 8 pilihan, mencakup CRUD tenant, riwayat, laporan, dan cetak invoice.

</td>
</tr>
<tr>
<td valign="top">

```python
            if pilihan == "1":
                tambah_data()
                jeda()
            elif pilihan == "2":
                tampilkan_data()
                input("\nTekan ENTER untuk kembali...")
            elif pilihan == "3":
                ubah_data()
                jeda()
            elif pilihan == "4":
                hapus_data()
                jeda()
            elif pilihan == "5":
                tampilkan_riwayat(username, True)
                input("\nTekan ENTER untuk kembali...")
            elif pilihan == "6":
                laporan_admin()
                input("\nTekan ENTER untuk kembali...")
            elif pilihan == "7":
                cetak_ulang_invoice(username, True)
                input("\nTekan ENTER untuk kembali...")
            elif pilihan == "8":
                print("Logout berhasil")
                jeda()
                break
            else:
                print("Pilihan tidak valid")
                jeda()
    except KeyboardInterrupt:
        print("dilarang mengisi memakai Ctrl")
    return menu_admin
```

</td>
<td valign="top">

**Menu admin – aksi.**

- Pilihan yang menampilkan data memakai `input("Tekan ENTER...")` agar tabel tidak langsung terhapus.
- Pilihan yang hanya memberi pesan singkat memakai `jeda()`.
- `tampilkan_riwayat(username, True)` dan `cetak_ulang_invoice(username, True)` → admin melihat **semua** data.
- Pilihan `8` → `break` keluar dari perulangan (logout).
- `Ctrl+C` ditangkap agar program tidak berhenti paksa.

</td>
</tr>
<tr>
<td valign="top">

```python
def menu_user(username):
    while True:
        try:
            bersihkan_layar()
            print("\n=== MENU USER -", username, "===")
            print("Saldo :", rupiah(users[username]["saldo"]))
            print("1. Tampilkan data tenant")
            print("2. Top up saldo")
            print("3. Reservasi & bayar tenant")
            print("4. Riwayat transaksi saya")
            print("5. Cetak ulang invoice")
            print("6. Logout")
            pilihan = input("Pilih menu: ")
```

</td>
<td valign="top">

**Menu user – tampilan.**

- Saldo ditampilkan di bagian atas setiap kali menu muncul.
- `try` berada **di dalam** `while`, sehingga jika `Ctrl+C` ditekan, program hanya menampilkan pesan lalu menu muncul kembali (tidak keluar dari menu).

</td>
</tr>
<tr>
<td valign="top">

```python
            if pilihan == "1":
                tampilkan_data()
                input("\nTekan ENTER untuk kembali...")
            elif pilihan == "2":
                top_up(username)
                input("\nTekan ENTER untuk kembali...")
            elif pilihan == "3":
                reservasi_tenant(username)
                input("\nTekan ENTER untuk kembali...")
            elif pilihan == "4":
                tampilkan_riwayat(username, False)
                input("\nTekan ENTER untuk kembali...")
            elif pilihan == "5":
                cetak_ulang_invoice(username, False)
                input("\nTekan ENTER untuk kembali...")
            elif pilihan == "6":
                print("Logout berhasil")
                jeda()
                break
            else:
                print("Pilihan tidak valid")
                jeda()
        except KeyboardInterrupt:
            print("dilarang mengisi memakai Ctrl")
            jeda()
```

</td>
<td valign="top">

**Menu user – aksi.**

- Memanggil fungsi sesuai pilihan: lihat tenant, top up, reservasi, riwayat, cetak invoice.
- `False` pada `tampilkan_riwayat` dan `cetak_ulang_invoice` membatasi data hanya milik user tersebut.
- Pilihan `6` → logout.
- Input selain 1–6 → "Pilihan tidak valid".

</td>
</tr>
<tr>
<td valign="top">

```python
def main():
    while True:
        try:
            bersihkan_layar()
            print("\n=== SISTEM RESERVASI TENANT BAZAR ===")
            print("1. Login")
            print("2. Registrasi")
            print("3. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                username = login()
                if username == "":
                    print("Gagal login 3 kali. Kembali ke menu utama.")
                    jeda()
                else:
                    if users[username]["role"] == "admin":
                        menu_admin(username)
                    else:
                        menu_user(username)
            elif pilihan == "2":
                registrasi()
                jeda()
            elif pilihan == "3":
                print("Terima kasih")
                break
            else:
                print("Pilihan tidak valid")
                jeda()
        except KeyboardInterrupt:
            print("\nDilarang mengisi memakai Ctrl+C")
            jeda()
main()
```

</td>
<td valign="top">

**Titik masuk program.**

- Menampilkan menu utama: Login, Registrasi, Keluar.
- Setelah login berhasil, **role** di `users.json` menentukan menu:
  - `"admin"` → `menu_admin()`
  - selain itu → `menu_user()`
- Login gagal 3 kali (`username == ""`) → kembali ke menu utama.
- Pilihan `3` → `break`, program selesai.
- `main()` di baris terakhir menjalankan seluruh program.

</td>
</tr>
</table>

---

## 🗃 Format File JSON

**`users.json`**

```json
{
    "admin": {
        "password": "admin123",
        "role": "admin",
        "saldo": 0
    },
    "budi": {
        "password": "12345",
        "role": "user",
        "saldo": 50000
    }
}
```

**`tenants.json`**

```json
[
    {
        "id": 1,
        "nama": "Warung Bu Siti",
        "kategori": "Makanan",
        "harga": 150000,
        "stok": 5,
        "status": "Tersedia"
    }
]
```

**`transaksi.json`** (dibuat otomatis)

```json
[
    {
        "kode": "TRX-261025153200-482",
        "waktu": "25-10-2026 15:32:00",
        "username": "budi",
        "tipe": "Reservasi",
        "tenant_id": 1,
        "tenant_nama": "Warung Bu Siti",
        "qty": 2,
        "jumlah": 300000,
        "saldo_akhir": 200000
    }
]
```

---

## 📝 Catatan & Pengembangan Lanjutan

- **Password masih disimpan sebagai teks biasa.** Untuk keamanan lebih baik, gunakan hashing (mis. `hashlib` atau `bcrypt`).
- **Akun admin dibuat manual** di `users.json` dengan `"role": "admin"`; registrasi hanya membuat akun `user`.
- **Path memakai format Windows** (`C:\ApasProjek`). Untuk Linux/Mac, ubah `folder_data` dan pemisah `"\\"` pada `cetak_invoice()` (disarankan memakai `os.path.join`).
- **Fungsi `menu_admin` mengembalikan `menu_admin`** di akhir (`return menu_admin`). Nilai ini tidak dipakai di mana pun, jadi aman dihapus.
- **Fungsi `lihat_saldo()` belum dipanggil** dari menu mana pun (saldo sudah tampil di header menu user), bisa dihapus atau dijadikan menu tersendiri.
- Ide pengembangan: pembatalan reservasi, pencarian/filter tenant per kategori, ekspor laporan ke CSV, dan hashing password.

---

<p align="center">Dibuat dengan 🐍 Python</p>
