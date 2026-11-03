<div align="center">

# 🏪 Sistem Reservasi Tenant Bazar

**Aplikasi berbasis terminal (CLI) untuk mengelola lapak bazar, saldo e-money, reservasi, dan invoice.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white)
![Storage](https://img.shields.io/badge/Storage-JSON-F7DF1E?logo=json&logoColor=black)

</div>

---

## 📑 Daftar Isi

1. [Judul / Tema](#1--judul--tema)
2. [Anggota & Peran](#2--anggota--peran)
3. [Deskripsi & Tujuan](#3--deskripsi--tujuan)
4. [Flowchart](#4--flowchart)
5. [Daftar Fitur per Role](#5--daftar-fitur-per-role)
6. [Screenshot Output & Penjelasan](#6--screenshot-output--penjelasan)
7. [Cara Menjalankan Program](#7--cara-menjalankan-program)

---

## 1. 🎯 Judul / Tema

| | |
|---|---|
| **Judul** | Sistem Reservasi Tenant Bazar |
| **Tema** | Manajemen penyewaan lapak bazar dengan pembayaran e-money |
| **Bahasa** | Python (CLI / terminal) |
| **Penyimpanan data** | File JSON (`users.json`, `tenant.json`, `transaksi.json`) |

---

## 2. 👥 Anggota & Peran

| No | Nama | NIM / ID | Peran | Tanggung Jawab | GitHub |
|:--:|------|----------|-------|----------------|--------|
| 1 | **Muhammad Pasha Aditya** | `2609116085` | Ketua Tim | Autentikasi (login & registrasi), error handling, membantu CRUD dasar, membantu revisi flowchart dan laporan | [@MuhammadPashaAditya](https://github.com/MuhammadPashaAditya) |
| 2 | **Lithalia Geminifer Addawiyah** | `2609116088` | Pengembang Tenant | CRUD data tenant (tambah, tampil, ubah, hapus), menu admin | [@username2](https://github.com/username2) |
| 3 | **Muhammad Fahry Praditya** | `2609116104` | Pengembang Transaksi | Top up, reservasi & pembayaran, invoice, menu user | [@username3](https://github.com/username3) |
| 4 | **Astri Maharani** | `2609116106` | Dokumentasi & Pengujian | Riwayat transaksi, laporan admin, README, pengujian program | [@username4](https://github.com/username4) |

---

## 3. 📖 Deskripsi & Tujuan

### Deskripsi

**Sistem Reservasi Tenant Bazar** adalah program Python berbasis terminal yang membantu pengelolaan penyewaan lapak pada sebuah bazar. Program memiliki dua peran pengguna, yaitu **Admin** yang mengelola lapak dan memantau transaksi, serta **User** yang menyewa lapak dengan membayar memakai saldo e-money.

Setiap lapak induk memiliki kuota maksimal **20 lapak** dan dibagi ke dalam 5 kategori: Makanan, Minuman, Fashion, Kerajinan, dan Lainnya. Ketika user menyewa, kuota lapak induk berkurang dan tenant baru milik penyewa muncul di bawah lapak induknya dengan status **Disewa**. Setiap pembayaran menghasilkan kode transaksi unik dan invoice `.txt`.

### Tujuan

1. Memudahkan admin mengelola data lapak, stok, dan harga sewa secara terpusat.
2. Memudahkan user melakukan reservasi dan pembayaran lapak tanpa pencatatan manual.
3. Menyediakan pencatatan transaksi dan invoice yang rapi serta dapat dicetak ulang.
4. Memberikan laporan ringkas pendapatan dan tenant terlaris untuk admin.
5. Menerapkan konsep dasar pemrograman Python: fungsi, struktur data, percabangan, perulangan, penanganan error, dan file JSON.

---

## 4. 🔀 Flowchart

> Flowchart di bawah ditampilkan dalam bentuk gambar. Klik gambar untuk memperbesar.

### 4.1 Alur Program Utama

<table>
<tr>
<td valign="top">

<img src="https://github.com/user-attachments/assets/da813817-78d5-4118-81bf-b912fe7296c0" alt="Flowchart alur program utama" width="380">

</td>
<td valign="top">

#### Proses Awal (Load Data)

| No | Proses | Hasil |
|---|---|---|
| 1 | Baca `users.json` | Jika file hilang/rusak, program berhenti |
| 2 | Cek data `users` | Jika kosong, program berhenti |
| 3 | Baca `transaksi.json` | Jika belum ada, diisi list kosong |
| 4 | Inisialisasi data awal | Masuk ke Menu Utama |

#### Menu Utama

| Pilihan | Menu | Aksi |
|---|---|---|
| `1` | Login | Masuk proses login |
| `2` | Registrasi | Buat akun baru |
| `3` | Keluar | Program selesai |
| Lainnya | - | "Pilihan tidak valid!" |

#### Proses Login (maks. 3 kali)

| Langkah | Proses |
|---|---|
| 1 | Input `username` dan `password` (tersamarkan) |
| 2 | Cocokkan dengan data `users` |
| 3 | Cocok: login berhasil, lanjut cek role |
| 4 | Tidak cocok: `percobaan += 1`, tampil sisa percobaan |
| 5 | Percobaan habis: kembali ke menu utama |

#### Proses Registrasi

| Langkah | Proses |
|---|---|
| 1 | Input `username` dan `password` (tidak boleh kosong) |
| 2 | Cek username belum dipakai |
| 3 | Simpan ke `users.json` (role `user`, saldo `0`) |
| 4 | Kembali ke menu utama |

</td>
</tr>
</table>

### 4.2 Alur Menu Admin

<table>
<tr>
<td valign="top">

<img src="https://github.com/user-attachments/assets/064cadf8-01d1-493c-bbea-befd8b18c481" alt="Flowchart menu admin" width="380">

</td>
<td valign="top">

#### Daftar Menu

Admin memilih menu (`input pilihan`), lalu program mencocokkan nilainya dengan percabangan.

| Pilihan | Menu | Keterangan |
|---|---|---|
| `1` | Tambah data tenant | Menambah lapak baru |
| `2` | Tampilkan data tenant | Menampilkan seluruh tenant dalam tabel |
| `3` | Ubah data tenant | Mengubah data tenant yang sudah ada |
| `4` | Hapus data tenant | Menghapus tenant setelah konfirmasi |
| `5` | Riwayat transaksi & cetak ulang invoice | Lanjut ke flowchart Invoice & Riwayat Transaksi (4.8) |
| `6` | Laporan ringkas | Lanjut ke flowchart Laporan Ringkas (4.4) |
| `7` | Tambah saldo user | Admin memilih user, lalu mengisi nominal (Rp 10.000 sampai Rp 10.000.000) |
| `8` | Logout | Tampil "Logout berhasil", kembali ke menu utama |
| Lainnya | - | Tampil "Pilihan tidak valid!", jeda, kembali ke menu admin |

#### 1. Tambah Data Tenant

| Langkah | Proses | Validasi / Hasil |
|---|---|---|
| 1 | Input nama tenant | Tidak boleh kosong |
| 2 | Cek duplikat | Jika nama sudah ada, tampil pesan dan kembali ke menu |
| 3 | `kategori = pilih_kategori()` | Memilih kategori 1 sampai 5 |
| 4 | `harga = input_angka("Harga sewa (Rp)")` | Harus berupa angka |
| 5 | Tentukan stok lapak | Lapak baru berkuota 20 |
| 6 | Buat ID baru | ID otomatis bertambah 1 |
| 7 | Simpan ke `tenant.json` | Data tersimpan permanen |
| 8 | Tampil "Tenant berhasil ditambahkan" | Jeda, kembali ke menu admin |

#### 2. Tampilkan Data Tenant

| Langkah | Proses | Hasil |
|---|---|---|
| 1 | Panggil `tampilkan_data()` | Data tenant tampil dalam tabel (`PrettyTable`), terurut per kategori |
| 2 | Jika data kosong | Tampil pesan "Data tenant masih kosong" |
| 3 | Kembali ke menu admin | - |

#### 3. Ubah Data Tenant

| Langkah | Proses | Validasi / Hasil |
|---|---|---|
| 1 | Tampilkan data tenant | Admin melihat daftar tenant |
| 2 | Pilih tenant berdasarkan nomor di tabel | Jika tidak ditemukan, tampil pesan error |
| 3 | Input data baru (nama, kategori, harga, stok) | Angka divalidasi dengan `input_angka()`, stok tidak boleh melebihi 20 |
| 4 | Simpan perubahan ke `tenant.json` | Tenant hasil sewa hanya bisa diubah namanya |
| 5 | Tampil "Data berhasil diubah" | Jeda, kembali ke menu admin |

#### 4. Hapus Data Tenant

| Langkah | Proses | Validasi / Hasil |
|---|---|---|
| 1 | Tampilkan data tenant | - |
| 2 | Pilih tenant berdasarkan nomor di tabel | Jika tidak ditemukan, tampil pesan error |
| 3 | Konfirmasi hapus (`y/n`) | Jika `n`, tampil "Penghapusan dibatalkan" |
| 4 | Hapus dari list, simpan ke `tenant.json` | Jika lapak induk dihapus, tenant hasil sewanya ikut terhapus dan peringatan ditampilkan lebih dulu |
| 5 | Tampil "Tenant berhasil dihapus" | Jeda, kembali ke menu admin |

#### Konektor ke Flowchart Lain

| Simbol di flowchart | Arti |
|---|---|
| Pentagon hijau (atas) | Titik masuk dari proses login (role `admin`) |
| Pentagon hijau (menu 5 dan 6) | Alur dilanjutkan di flowchart fungsi lain |
| Lingkaran bertanda huruf | Kembali ke awal Menu Admin |

</td>
</tr>
</table>

### 4.3 Alur Menu User

<table>
<tr>
<td valign="top">

<img src="https://github.com/user-attachments/assets/64992ee3-0c81-4b07-8418-80199f1a87b5" alt="Flowchart menu user" width="380">

</td>
<td valign="top">

#### Tampilan Awal

Setelah login dengan role `user`, program menjalankan `bersihkan_layar()` lalu menampilkan header dan menu.

| Elemen | Isi |
|---|---|
| Judul | `=== MENU USER - {username} ===` |
| Saldo | `Saldo: Rp{saldo}` (diambil dari data user yang sedang login) |
| Input | `input pilihan` |

#### Daftar Menu

| Pilihan | Menu | Aksi |
|---|---|---|
| `1` | Tampilkan data tenant | Menampilkan semua tenant, lalu kembali ke menu user |
| `2` | Top up saldo | Lanjut ke flowchart Top Up Saldo (4.5) |
| `3` | Reservasi & bayar tenant | Lanjut ke flowchart Reservasi dan Pembayaran (4.6) |
| `4` | Riwayat transaksi & cetak ulang invoice | Lanjut ke flowchart Invoice & Riwayat Transaksi (4.8) |
| `5` | Logout | Tampil "Logout berhasil", jeda, kembali ke menu utama |
| Lainnya | - | Tampil "Pilihan tidak valid!", jeda, kembali ke menu user |

#### Detail Menu 1: Tampilkan Data Tenant

| Langkah | Proses | Hasil |
|---|---|---|
| 1 | Panggil `tampilkan_data()` | Semua tenant tampil dalam tabel (`PrettyTable`) |
| 2 | Tampil "Tekan ENTER untuk kembali..." | Program menunggu input ENTER |
| 3 | Kembali ke awal menu user | Menu dan saldo ditampilkan ulang |

#### Alur Logout (Menu 5)

| Langkah | Proses |
|---|---|
| 1 | Tampil "Logout berhasil" |
| 2 | Jeda (`time.sleep`) |
| 3 | Kembali ke Menu Utama (Login / Registrasi / Keluar) |

#### Penjelasan Konektor

| Simbol di flowchart | Arti |
|---|---|
| Pentagon hijau (atas) | Titik masuk dari proses login (role `user`) |
| Lingkaran `A` | Kembali ke awal Menu User |
| Pentagon hijau (menu 2, 3, 4) | Alur berlanjut di flowchart fungsi masing-masing |
| Pentagon hijau (setelah logout) | Kembali ke Menu Utama |

</td>
</tr>
</table>

### 4.4 Laporan Ringkas (Admin)

<table>
<tr>
<td valign="top">

<img src="https://github.com/user-attachments/assets/6346f393-37cb-46a6-8bfe-c6aacb93926d" alt="Flowchart laporan ringkas" width="380">

</td>
<td valign="top">

#### Gambaran Umum

Fitur ini dipanggil dari Menu Admin (konektor `P`). Program membaca seluruh data `transaksi.json`, menghitung total pendapatan dan jumlah transaksi reservasi, lalu menampilkan tenant terlaris.

#### Variabel yang Digunakan

| Variabel | Fungsi |
|---|---|
| `pendapatan` | Total uang dari seluruh transaksi bertipe reservasi |
| `jumlah` | Jumlah transaksi reservasi |
| `penjualan` | Penampung qty per tenant (dipakai untuk mencari tenant terlaris dan tabel per tenant) |

#### Alur Proses

| No | Proses | Kondisi | Hasil |
|---|---|---|---|
| 1 | Mulai laporan ringkas | - | Program masuk ke fungsi laporan |
| 2 | Inisialisasi `pendapatan`, `jumlah`, `penjualan` | - | Semua variabel diatur ke nilai awal (0 / kosong) |
| 3 | Cek apakah masih ada transaksi | Ya | Lanjut ke langkah 4 |
| 3 | Cek apakah masih ada transaksi | Tidak | Perulangan selesai, lanjut ke langkah 6 |
| 4 | Cek tipe transaksi | Tipe = Reservasi | Lanjut ke langkah 5 |
| 4 | Cek tipe transaksi | Bukan reservasi | Dilewati, kembali ke langkah 3 |
| 5 | Tambah ke laporan | - | `pendapatan` bertambah, `jumlah` +1, qty tenant ditambahkan ke `penjualan`, lalu kembali ke langkah 3 |
| 6 | Tampilkan ringkasan | - | Tampil total pendapatan dan jumlah transaksi |
| 7 | Cek `penjualan` kosong | Ya | Tampil "Data belum ada", kembali ke Menu Admin |
| 7 | Cek `penjualan` kosong | Tidak | Lanjut ke langkah 8 |
| 8 | Cari tenant terlaris | - | Tenant dengan qty terbanyak dipilih |
| 9 | Tampilkan tenant terlaris dan tabel per tenant | - | Hasil tampil dalam tabel (`PrettyTable`), lalu kembali ke Menu Admin |

#### Penjelasan Konektor

| Simbol di flowchart | Arti |
|---|---|
| Pentagon hijau `P` (atas) | Titik masuk dari Menu Admin |
| Lingkaran `A` | Titik kembali ke bagian sebelumnya dalam alur laporan |
| Pentagon hijau `A` (bawah) | Kembali ke Menu Admin |

</td>
</tr>
</table>

### 4.5 Top Up Saldo (User)

<table>
<tr>
<td valign="top">

<img src="https://github.com/user-attachments/assets/d3f48b1a-3c39-41fd-9c39-64ea2bf36ada" alt="Flowchart top up saldo" width="380">

</td>
<td valign="top">

#### Gambaran Umum

Fitur ini dipanggil dari Menu User (pilihan `2`). User mengisi saldo dengan nominal yang dibatasi `MIN_TOPUP` dan `MAX_TOPUP`, lalu transaksi dicatat dengan tipe `Top Up`.

#### Variabel dan Konstanta

| Nama | Fungsi |
|---|---|
| `MIN_TOPUP` | Batas minimal nominal per top up (Rp 10.000) |
| `MAX_TOPUP` | Batas maksimal nominal per transaksi top up (Rp 10.000.000) |
| `nominal` | Jumlah uang yang diinput user (divalidasi `input_angka()`) |
| `users[username]['saldo']` | Saldo user yang sedang login |
| `trx` | Hasil `catat_transaksi()`, berisi data transaksi termasuk `trx['kode']` |

#### Alur Proses

| No | Proses | Kondisi | Hasil |
|---|---|---|---|
| 1 | Tampil judul `=== TOP UP SALDO ===` | - | - |
| 2 | Tampil saldo saat ini, minimal, dan maksimal top up | - | Format rupiah lewat `rupiah()` |
| 3 | `nominal = input_angka("Nominal top up (Rp)")` | - | Input harus berupa angka |
| 4 | Cek `nominal < MIN_TOPUP` | Ya | Tampil "Top up minimal Rp...!", kembali ke Menu User |
| 5 | Cek `nominal > MAX_TOPUP` | Ya | Tampil "Top up maksimal Rp... per transaksi!", kembali ke Menu User |
| 6 | `konfirmasi("Lanjutkan top up?")` | - | Diulang sampai jawaban `y` atau `n` |
| 7 | Cek jawaban `== 'y'` | Tidak | Tampil "Top up dibatalkan.", kembali ke Menu User |
| 8 | Tambah saldo | Ya | `saldo = saldo + nominal` |
| 9 | Simpan saldo ke `users.json` | - | Data saldo tersimpan permanen |
| 10 | `catat_transaksi(...)` | - | Transaksi tipe `Top Up` tercatat di `transaksi.json` |
| 11 | Tampil "Top up berhasil!" | - | Menampilkan saldo sekarang dan kode transaksi |
| 12 | Tampil "Tekan ENTER untuk kembali..." | - | Menunggu ENTER, lalu kembali ke Menu User |

#### Validasi Nominal

| Kondisi | Pesan | Hasil |
|---|---|---|
| `nominal < MIN_TOPUP` | Top up minimal Rp... | Ditolak, kembali ke Menu User |
| `nominal > MAX_TOPUP` | Top up maksimal Rp... per transaksi | Ditolak, kembali ke Menu User |
| `MIN_TOPUP <= nominal <= MAX_TOPUP` | - | Lanjut ke konfirmasi |

#### Data yang Dicatat ke Transaksi

| Parameter `catat_transaksi` | Nilai | Keterangan |
|---|---|---|
| `username` | Username yang login | Pemilik transaksi |
| Tipe | `Top Up` | Pembeda dengan transaksi reservasi |
| Tenant | `None` | Top up tidak terkait tenant |
| Total | `nominal` | Jumlah uang yang ditambahkan |
| Qty | `1` | Nilai tetap |
| Saldo | Saldo sesudah top up | Untuk riwayat saldo |

#### Penjelasan Konektor

| Simbol di flowchart | Arti |
|---|---|
| Pentagon hijau `E` (atas) | Titik masuk dari Menu User pilihan `2` |
| Lingkaran `A` (3 buah di kanan) | Kembali ke awal Menu User (jalur nominal ditolak atau dibatalkan) |
| Lingkaran `A` (bawah) | Kembali ke awal Menu User setelah ENTER |
| Pentagon hijau (paling bawah) | Kembali ke Menu User |

</td>
</tr>
</table>

### 4.6 Reservasi & Pembayaran Tenant (User)

<table>
<tr>
<td valign="top">

<img src="https://github.com/user-attachments/assets/d5af8391-63bd-4057-bb81-989420c6b539" alt="Flowchart reservasi dan pembayaran tenant" width="380">

</td>
<td valign="top">

#### Gambaran Umum

Fitur ini dipanggil dari Menu User (pilihan `3`). User memilih lapak berdasarkan ID, menentukan jumlah lapak, memberi nama tenant miliknya, lalu membayar memakai saldo. Setelah berhasil, kuota lapak induk berkurang, tenant baru berstatus `Disewa` ditambahkan, transaksi dicatat, dan invoice dicetak.

#### Variabel yang Digunakan

| Variabel | Fungsi |
|---|---|
| `id_tenant` | ID lapak yang dipilih user (divalidasi `input_angka()`) |
| `tenant` | Data lapak hasil `cari_tenant()` |
| `qty` | Jumlah lapak yang ingin disewa |
| `total` | Total biaya (`harga * qty`) |
| `users[username]['saldo']` | Saldo user yang sedang login |
| `trx` | Hasil `catat_transaksi()`, dipakai untuk mencetak invoice |

#### Alur Proses

| No | Proses | Kondisi | Hasil |
|---|---|---|---|
| 1 | Tampil judul `=== RESERVASI & PEMBAYARAN TENANT ===` | - | - |
| 2 | Tampilkan data tenant | - | Daftar tenant tampil dalam tabel |
| 3 | `id_tenant = input_angka(...)` | - | Input harus berupa angka |
| 4 | Cari lapak berdasarkan ID | Tidak ditemukan | Tampil pesan error, kembali ke Menu User |
| 5 | Ambil data lapak yang ditemukan | Ditemukan | Lanjut ke langkah 6 |
| 6 | Cek stok lapak | Stok habis | Tampil pesan stok habis, kembali ke Menu User |
| 7 | `qty = input_angka(...)` | - | Jumlah lapak yang ingin disewa |
| 8 | Cek `qty` melebihi stok | Ya | Tampil pesan jumlah tidak valid, kembali ke Menu User |
| 9 | Input nama tenant | Kosong | Tampil pesan, kembali ke Menu User |
| 10 | Hitung `total = harga * qty` | - | Ringkasan dan total bayar ditampilkan |
| 11 | Cek saldo `< total` | Ya | Tampil "Saldo tidak cukup" beserta selisihnya, kembali ke Menu User |
| 12 | `konfirmasi("Lanjutkan pembayaran?")` | Jawaban bukan `y` | Tampil "Pembayaran dibatalkan", kembali ke Menu User |
| 13 | Kurangi saldo user dan kuota lapak induk | Jawaban `y` | `saldo -= total`, `stok -= qty`, tenant baru berstatus `Disewa` ditambahkan |
| 14 | Simpan perubahan ke `users.json` dan `tenant.json` | - | Data tersimpan permanen |
| 15 | `catat_transaksi(...)` | - | Transaksi tipe `Reservasi` tercatat |
| 16 | Tampil "Pembayaran berhasil!" | - | - |
| 17 | `cetak_invoice(trx)` | - | Invoice `.txt` dibuat di folder `invoice` |
| 18 | Tampil "Tekan ENTER untuk kembali..." | - | Menunggu ENTER, lalu kembali ke Menu User |

#### Validasi Pemesanan

| Validasi | Kondisi gagal | Hasil |
|---|---|---|
| ID lapak | Tidak ada di `tenant.json` | Ditolak, kembali ke Menu User |
| Stok lapak | Stok `0` | Ditolak, kembali ke Menu User |
| Jumlah lapak | `qty` melebihi stok tersedia | Ditolak, kembali ke Menu User |
| Nama tenant | Kosong | Ditolak, kembali ke Menu User |
| Saldo | Saldo `< total` | Ditolak, user diarahkan top up |
| Konfirmasi | Jawaban `n` | Dibatalkan, tidak ada perubahan data |

#### Data yang Berubah Setelah Pembayaran

| File | Perubahan |
|---|---|
| `users.json` | Saldo user berkurang sebesar `total` |
| `tenant.json` | Stok lapak induk berkurang sebesar `qty`, tenant baru berstatus `Disewa` bertambah |
| `transaksi.json` | Bertambah satu transaksi bertipe `Reservasi` |
| Folder `invoice/` | Bertambah satu file invoice `.txt` |

#### Penjelasan Konektor

| Simbol di flowchart | Arti |
|---|---|
| Pentagon hijau (atas) | Titik masuk dari Menu User pilihan `3` |
| Lingkaran `A` (di kanan) | Kembali ke awal Menu User (jalur validasi gagal atau dibatalkan) |
| Lingkaran `A` (bawah) | Kembali ke Menu User setelah ENTER |
| Pentagon hijau (paling bawah) | Kembali ke Menu User |
| Silinder pink | Penyimpanan data ke file JSON |

</td>
</tr>
</table>

### 4.7 Fungsi Pendukung

Tiga fungsi ini dipanggil dari fitur lain (top up, reservasi, tenant) dan tidak tampil langsung ke user.

---

#### 1. `perbarui_status(tenant)`

<table>
<tr>
<td valign="top">

<img src="https://github.com/user-attachments/assets/bf00d338-15a3-46bb-b5eb-ab7ed6ec0dd4" alt="Flowchart perbarui_status" width="380">

</td>
<td valign="top">

Memperbarui kolom status tenant sesuai sisa stok lapak.

| Kondisi | Hasil |
|---|---|
| `tenant['stok'] > 0` | `tenant['status'] = "Tersedia"` |
| `tenant['stok'] == 0` | `tenant['status'] = "Penuh"` |

| Detail | Keterangan |
|---|---|
| Dipanggil dari | Tambah, ubah, hapus tenant, dan reservasi |
| Parameter | Data tenant (dictionary) |
| Nilai kembali | Tidak ada, data tenant langsung diubah |

</td>
</tr>
</table>

---

#### 2. `buat_kode()`

<table>
<tr>
<td valign="top">

<img src="https://github.com/user-attachments/assets/a5f705a3-1e85-4dea-b26f-83051faf188b" alt="Flowchart buat_kode" width="380">

</td>
<td valign="top">

Membuat kode transaksi unik (contoh: `TRX-251103200500`).

| No | Proses | Hasil |
|---|---|---|
| 1 | Baca data transaksi dengan `baca_trx()` | Daftar transaksi dimuat |
| 2 | Susun `kode = "TRX-" + tanggal waktu` | Format dari `datetime.now().strftime(...)` |
| 3 | Set `ada = False` | Penanda kode belum dipakai |
| 4 | Cek apakah masih ada transaksi | Ya: lanjut ke langkah 5. Tidak: ke langkah 6 |
| 5 | Cek `kode` sama dengan kode transaksi | Jika sama, `ada = True`, lanjut cek transaksi berikutnya |
| 6 | Cek `ada == False` | Ya: kembalikan `kode`. Tidak: buat kode baru, ulang dari langkah 3 |

| Detail | Keterangan |
|---|---|
| Tujuan | Menjamin tidak ada dua transaksi dengan kode yang sama |
| Dipanggil dari | `catat_transaksi()` |
| Nilai kembali | String kode transaksi |

</td>
</tr>
</table>

---

#### 3. `catat_transaksi(username, tipe, tenant, jumlah, qty, saldo_akhir)`

<table>
<tr>
<td valign="top">

<img src="https://github.com/user-attachments/assets/ad7826bb-1ea6-4a60-abfc-f03df682adbe" alt="Flowchart catat_transaksi" width="380">

</td>
<td valign="top">

Menyimpan satu transaksi baru ke `transaksi.json`.

| Parameter | Fungsi |
|---|---|
| `username` | Pemilik transaksi |
| `tipe` | Jenis transaksi (`Top Up`, `Top Up Admin`, atau `Reservasi`) |
| `tenant` | Data tenant, atau `None` untuk top up |
| `jumlah` | Nominal uang transaksi |
| `qty` | Jumlah lapak |
| `saldo_akhir` | Saldo user setelah transaksi |

| No | Proses | Hasil |
|---|---|---|
| 1 | Baca data dengan `baca_trx()` | Daftar transaksi dimuat |
| 2 | Buat `waktu` dari `datetime.now()` | Format `YYYY-MM-DD HH:MM:SS` |
| 3 | Cek `tenant` ada | Ya: `tenant_id` dan `tenant_nama` diambil dari data tenant |
| 3 | Cek `tenant` ada | Tidak: `tenant_id = 0`, `tenant_nama = "-"` |
| 4 | Susun data `trx` dengan `kode = buat_kode()` | Dictionary berisi seluruh field transaksi |
| 5 | `transaksi.append(trx)` | Transaksi masuk ke list |
| 6 | Simpan ke `transaksi.json` | Data tersimpan permanen |
| 7 | Kembalikan `trx` | Dipakai untuk menampilkan kode dan mencetak invoice |

| Field di `trx` | Isi |
|---|---|
| `kode` | Hasil `buat_kode()` |
| `waktu` | Tanggal dan jam transaksi |
| `username` | Pemilik transaksi |
| `tipe` | `Top Up`, `Top Up Admin`, atau `Reservasi` |
| `tenant_id`, `tenant_nama` | Data tenant (atau nilai kosong) |
| `qty`, `jumlah`, `saldo_akhir` | Jumlah lapak, nominal, saldo sesudah transaksi |

</td>
</tr>
</table>


### 4.8 Invoice & Riwayat Transaksi

Tiga fungsi ini dipanggil dari Menu User (pilihan `4`), Menu Admin (pilihan `5`), dan setelah pembayaran reservasi.

---

#### 1. `cetak_invoice(trx)`

<table>
<tr>
<td width="45%" valign="top">

<img src="https://github.com/user-attachments/assets/a1e089f6-8b76-4ac0-af52-a4763ccc13c5" />

</td>
<td width="55%" valign="top">

Membuat invoice dari satu transaksi, menampilkannya di layar, lalu menyimpannya sebagai file `.txt`.

| No | Proses | Hasil |
|---|---|---|
| 1 | Susun teks invoice dari data `trx` | Berisi kode, waktu, pelanggan, tenant, kategori, jumlah lapak, total bayar, dan sisa saldo |
| 2 | Tampilkan invoice di layar | User langsung melihat struknya |
| 3 | Tentukan nama file di folder `invoice/` | Contoh: `invoice/TRX-xxxx.txt` |
| 4 | Tulis teks ke file (`try`) | File invoice dibuat |
| 5a | Berhasil | Tampil "Invoice tersimpan di ..." |
| 5b | Gagal (`except`) | Tampil pesan gagal menyimpan, program tetap berjalan |

| Detail | Keterangan |
|---|---|
| Parameter | `trx`, dictionary transaksi dari `catat_transaksi()` |
| Dipanggil dari | Reservasi dan `cetak_ulang_invoice()` |
| Nilai kembali | Tidak ada |

</td>
</tr>
</table>

---

#### 2. `tampilkan_riwayat(username, role)`

<table>
<tr>
<td width="45%" valign="top">

<img src="https://github.com/user-attachments/assets/2a0cfd1a-1337-4f08-b05d-764fecf13d8e" alt="Flowchart tampilkan_riwayat" width="380">

</td>
<td width="55%" valign="top">

Menampilkan riwayat transaksi dalam bentuk tabel. Admin dapat melihat semua transaksi, sedangkan user hanya dapat melihat transaksi miliknya sendiri.

| No | Proses | Hasil |
|---|---|---|
| 1 | Buat tabel `PrettyTable` dengan kolom transaksi | Kode, Waktu, User, Tipe, Tenant, Nama Usaha, Qty, Jumlah, Saldo Akhir |
| 2 | Set `ada = False` | Penanda belum ada baris |
| 3 | Cek apakah masih ada transaksi | Ya: lanjut ke langkah 4. Tidak: ke langkah 5 |
| 4 | Cek `role == admin` atau `username` cocok | Ya: baris ditambahkan ke tabel, `ada = True`. Tidak: dilewati |
| 5 | Cek `ada == True` | Ya: tampilkan tabel. Tidak: tampil "Belum ada transaksi" |

| Role | Data yang tampil |
|---|---|
| `admin` | Seluruh transaksi semua user |
| `user` | Hanya transaksi dengan `username` yang sama |

</td>
</tr>
</table>

---

#### 3. `cetak_ulang_invoice(username, role)`

<table>
<tr>
<td width="45%" valign="top">

<img src="https://github.com/user-attachments/assets/d079991d-5dce-44c9-9e87-f266f92b86dc" alt="Flowchart cetak_ulang_invoice" width="380">

</td>
<td width="55%" valign="top">

Mencetak ulang invoice berdasarkan kode transaksi yang dimasukkan oleh user. Fungsi ini memiliki beberapa validasi untuk memastikan transaksi ditemukan dan pengguna memiliki hak akses.

| No | Proses | Kondisi | Hasil |
|---|---|---|---|
| 1 | Tampilkan riwayat dengan `tampilkan_riwayat()` | - | User melihat daftar kode |
| 2 | Cek ada transaksi | Tidak ada | Tampil "Riwayat kosong", kembali ke menu |
| 3 | Input kode transaksi | - | Pencarian di `transaksi.json` |
| 4 | Cek kode ditemukan | Tidak ditemukan | Tampil "Kode tidak ditemukan", kembali ke menu |
| 5 | Cek hak akses | Bukan admin dan bukan pemilik | Tampil pesan tidak berhak, kembali ke menu |
| 6 | Cek tipe transaksi | Tipe `Top Up` | Tampil "Top Up tidak memiliki invoice", kembali ke menu |
| 7 | Panggil `cetak_invoice(trx)` | Lolos semua validasi | Invoice ditampilkan dan disimpan ulang |

| Validasi | Alasan |
|---|---|
| Kode ditemukan | Mencegah error saat kode tidak ada |
| Hak akses | User tidak boleh melihat invoice milik orang lain |
| Tipe transaksi | Invoice hanya dibuat untuk reservasi, bukan top up |

</td>
</tr>
</table>

---
## 5. 📋 Daftar Fitur per Role

### 🌐 Umum (Tanpa Login)

| Fitur | Keterangan |
|-------|------------|
| Login | Maksimal 3 kali percobaan, password tersembunyi saat diketik |
| Registrasi | Username unik, tidak boleh kosong, tidak boleh mengandung spasi; akun baru otomatis berperan `user` dengan saldo Rp 0 |
| Keluar | Menutup program |

### 👑 Admin

| No | Fitur | Keterangan |
|:--:|-------|------------|
| 1 | Tambah data tenant | Input nama, kategori, dan harga sewa; lapak baru otomatis berkuota 20 |
| 2 | Tampilkan data tenant | Tabel terurut per kategori, lapak induk diikuti tenant hasil sewa |
| 3 | Ubah data tenant | Ubah nama, kategori, harga, dan stok; tenant hasil sewa hanya bisa diubah namanya |
| 4 | Hapus data tenant | Dengan konfirmasi y/n; menghapus lapak induk ikut menghapus tenant hasil sewanya |
| 5 | Riwayat transaksi & cetak ulang invoice | Melihat transaksi seluruh user |
| 6 | Laporan ringkas | Total pendapatan, jumlah transaksi reservasi, tenant terlaris |
| 7 | Tambah saldo user | Admin menambah saldo user (Rp 10.000 sampai Rp 10.000.000) |
| 8 | Logout | Kembali ke menu utama |

### 👤 User

| No | Fitur | Keterangan |
|:--:|-------|------------|
| 1 | Tampilkan data tenant | Melihat daftar lapak, stok, dan status |
| 2 | Top up saldo | Minimal Rp 10.000, maksimal Rp 10.000.000 per transaksi, dengan konfirmasi |
| 3 | Reservasi & bayar tenant | Memilih lapak, jumlah, nama tenant, lalu bayar dengan saldo |
| 4 | Riwayat transaksi & cetak ulang invoice | Hanya transaksi milik sendiri |
| 5 | Logout | Kembali ke menu utama |

---

## 6. 📸 Screenshot Output & Penjelasan

> 📝 **Petunjuk untuk tim:** jalankan program, ambil screenshot tiap tampilan, simpan di folder `docs/screenshots/` dengan nama file seperti di bawah, lalu gambar akan muncul otomatis. Hapus petunjuk ini setelah semua screenshot terpasang.

### 6.1 Menu Utama

![Menu Utama](docs/screenshots/01-menu-utama.png)

**Penjelasan:** Tampilan awal program dengan tiga pilihan: Login, Registrasi, dan Keluar. Input selain 1 sampai 3 menampilkan pesan "Pilihan tidak valid".

### 6.2 Registrasi

![Registrasi](docs/screenshots/02-registrasi.png)

**Penjelasan:** User mengisi username dan password. Program memeriksa username kosong, mengandung spasi, atau sudah dipakai. Jika valid, akun tersimpan ke `users.json` dengan role `user` dan saldo Rp 0.

### 6.3 Login

![Login](docs/screenshots/03-login.png)

**Penjelasan:** Password tampil sebagai karakter bintang. Jika salah, program menampilkan sisa percobaan. Setelah 3 kali gagal, program berhenti.

### 6.4 Menu Admin

![Menu Admin](docs/screenshots/04-menu-admin.png)

**Penjelasan:** Admin melihat 8 menu: kelola tenant, riwayat, laporan, tambah saldo user, dan logout.

### 6.5 Tampilkan Data Tenant

![Data Tenant](docs/screenshots/05-data-tenant.png)

**Penjelasan:** Data tampil dalam tabel dengan kolom No, Nama Tenant, Kategori, Harga Sewa, Stok, Status, dan Penyewa. Lapak induk berstatus `Tersedia` atau `Penuh`, sedangkan tenant hasil sewa berstatus `Disewa` dan tampil di bawah lapak induknya.

### 6.6 Tambah Data Tenant

![Tambah Tenant](docs/screenshots/06-tambah-tenant.png)

**Penjelasan:** Admin mengisi nama, memilih kategori (1 sampai 5), dan menentukan harga sewa. Nama yang kosong atau sudah ada akan ditolak. Lapak baru otomatis memiliki stok 20.

### 6.7 Ubah Data Tenant

![Ubah Tenant](docs/screenshots/07-ubah-tenant.png)

**Penjelasan:** Admin memilih tenant berdasarkan nomor di tabel, lalu mengubah data. Stok tidak boleh melebihi 20.

### 6.8 Hapus Data Tenant

![Hapus Tenant](docs/screenshots/08-hapus-tenant.png)

**Penjelasan:** Program meminta konfirmasi (y/n) sebelum menghapus. Jika yang dihapus adalah lapak induk, tenant hasil sewanya ikut terhapus dan muncul peringatan lebih dulu.

### 6.9 Laporan Ringkas

![Laporan](docs/screenshots/09-laporan.png)

**Penjelasan:** Menampilkan total pendapatan, jumlah transaksi reservasi, tenant terlaris, dan tabel jumlah lapak yang dipesan per tenant.

### 6.10 Tambah Saldo User (Admin)

![Tambah Saldo](docs/screenshots/10-tambah-saldo.png)

**Penjelasan:** Admin melihat daftar user beserta saldonya, memilih username tujuan, lalu mengisi nominal. Transaksi tercatat sebagai "Top Up Admin".

### 6.11 Menu User

![Menu User](docs/screenshots/11-menu-user.png)

**Penjelasan:** User melihat 5 menu: lihat tenant, top up, reservasi, riwayat, dan logout.

### 6.12 Top Up Saldo

![Top Up](docs/screenshots/12-top-up.png)

**Penjelasan:** Program menampilkan saldo saat ini dan batas top up. Nominal di luar batas ditolak. Setelah dikonfirmasi, saldo bertambah dan kode transaksi ditampilkan.

### 6.13 Reservasi & Pembayaran

![Reservasi](docs/screenshots/13-reservasi.png)

**Penjelasan:** User memilih lapak, jumlah, dan nama tenant, lalu program menampilkan ringkasan dan total bayar. Jika saldo kurang, ditampilkan selisihnya. Jika cukup dan dikonfirmasi, stok berkurang dan saldo terpotong.

### 6.14 Invoice

![Invoice](docs/screenshots/14-invoice.png)

**Penjelasan:** Setelah pembayaran berhasil, invoice tampil di layar dan tersimpan sebagai file `.txt` di folder `invoice`. Isinya kode transaksi, waktu, pelanggan, tenant, kategori, jumlah lapak, total bayar, dan sisa saldo.

### 6.15 Riwayat Transaksi

![Riwayat](docs/screenshots/15-riwayat.png)

**Penjelasan:** Tabel berisi kode, waktu, user, tipe, tenant, nama usaha, qty, jumlah, dan saldo akhir. User hanya melihat transaksinya sendiri, admin melihat semua. Invoice reservasi dapat dicetak ulang dengan memasukkan kode transaksi.

---

## 7. 🚀 Cara Menjalankan Program

```bash
# 1. Clone repositori
git clone https://github.com/APASrah/PA-APASrah.git
cd PA-APASrah

# 2. Pasang library
pip install prettytable pwinput

# 3. Jalankan
python main.py
```

Program membaca data dari folder `C:\ApasProjek`. Pastikan `users.json` dan `tenant.json` ada di folder tersebut (ubah variabel `folder_data` jika ingin lokasi lain). `transaksi.json` dan folder `invoice` dibuat otomatis.

Contoh `users.json`:

```json
{
    "admin": { "password": "ganti_password_ini", "role": "admin", "saldo": 0 },
    "budi":  { "password": "rahasia123", "role": "user", "saldo": 0 }
}
```

---

<div align="center">

Dibuat oleh **Tim APASrah**

</div>
