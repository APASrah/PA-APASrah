 <div align="center">

# 🏪 Sistem Reservasi Tenant Bazar

**Aplikasi berbasis terminal (CLI) untuk mengelola lapak bazar, saldo e-money, reservasi, dan invoice.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white)
![Storage](https://img.shields.io/badge/Storage-JSON-F7DF1E?logo=json&logoColor=black)

</div>

---

## 📑 Daftar Isi

1. [Judul / Tema](#1-judul--tema)
2. [Anggota & Peran](#2-anggota--peran)
3. [Deskripsi & Tujuan](#3-deskripsi--tujuan)
4. [Flowchart](#4-flowchart)
5. [Daftar Fitur per Role](#5-daftar-fitur-per-role)
6. [Screenshot Output & Penjelasan](#6-screenshot-output--penjelasan)
7. [Cara Menjalankan Program](#7-cara-menjalankan-program)

---

## 1. 🎯 Judul / Tema

| Keterangan | Isi |
|---|---|
| **Judul** | Sistem Reservasi Tenant Bazar |
| **Tema** | Manajemen penyewaan lapak bazar dengan pembayaran e-money |
| **Bahasa** | Python (CLI / terminal) |
| **Penyimpanan data** | File JSON (`users.json`, `tenant.json`, `transaksi.json`) |

---

## 2. 👥 Anggota & Peran

| No | Nama | NIM / ID | Peran | Tanggung Jawab | GitHub |
|:--:|---|---|---|---|---|
| 1 | **Muhammad Pasha Aditya** | `2609116085` | Ketua Tim | Autentikasi (login & registrasi), error handling, membantu CRUD dasar, membantu revisi flowchart dan laporan | [@MuhammadPashaAditya](https://github.com/MuhammadPashaAditya) |
| 2 | **Lithalia Geminifer Addawiyah** | `2609116088` | Pengembang Tenant | CRUD data tenant (tambah, tampil, ubah, hapus), menu admin | [@username2](https://github.com/username2) |
| 3 | **Muhammad Fahry Praditya** | `2609116104` | Coding, Flowchart, Laporam | Ngoding, Pengembangan dan revisi kode, revisi flowchart, revisi laporan,  | [@muhammadfahrypraditya](https://github.com/muhammadfahrypraditya) |
| 4 | **Astri Maharani** | `2609116106` | Dokumentasi & Pengujian | Riwayat transaksi, laporan admin, README, pengujian program | [@username4](https://github.com/username4) |

---

## 3. 📖 Deskripsi & Tujuan

### Deskripsi

**Sistem Reservasi Tenant Bazar** adalah program Python berbasis terminal yang membantu pengelolaan penyewaan lapak pada sebuah bazar. Program memiliki dua peran pengguna, yaitu **Admin** yang mengelola lapak dan memantau transaksi, serta **User** yang menyewa lapak dengan membayar menggunakan saldo e-money.

Setiap lapak induk memiliki kuota maksimal **20 lapak** dan dibagi ke dalam 5 kategori:

1. Makanan
2. Minuman
3. Fashion
4. Kerajinan
5. Lainnya

Ketika user menyewa lapak, kuota lapak induk akan berkurang. Tenant baru milik penyewa akan ditambahkan di bawah lapak induknya dengan status **Disewa**.

Setiap pembayaran reservasi menghasilkan kode transaksi unik dan invoice dalam format `.txt` yang dapat dicetak ulang.

### Tujuan

1. Memudahkan admin mengelola data lapak, stok, dan harga sewa secara terpusat.
2. Memudahkan user melakukan reservasi dan pembayaran lapak tanpa pencatatan manual.
3. Menyediakan pencatatan transaksi dan invoice yang rapi serta dapat dicetak ulang.
4. Memberikan laporan ringkas pendapatan dan tenant terlaris untuk admin.
5. Menerapkan konsep dasar pemrograman Python, seperti fungsi, struktur data, percabangan, perulangan, penanganan error, dan file JSON.

---

## 4. 🔀 Flowchart

> **Petunjuk:** Klik setiap gambar flowchart untuk membuka gambar dalam ukuran lebih besar.

### 4.1 Alur Program Utama

[![Flowchart alur program utama](https://github.com/user-attachments/assets/da813817-78d5-4118-81bf-b912fe7296c0)](https://github.com/user-attachments/assets/da813817-78d5-4118-81bf-b912fe7296c0)

#### Proses Awal (Load Data)

| No | Proses | Hasil |
|---|---|---|
| 1 | Baca `users.json` | Jika file hilang atau rusak, program berhenti |
| 2 | Cek data `users` | Jika kosong, program berhenti |
| 3 | Baca `transaksi.json` | Jika belum ada, diisi list kosong |
| 4 | Inisialisasi data awal | Masuk ke Menu Utama |

#### Menu Utama

| Pilihan | Menu | Aksi |
|---|---|---|
| `1` | Login | Masuk proses login |
| `2` | Registrasi | Membuat akun baru |
| `3` | Keluar | Program selesai |
| Lainnya | - | Menampilkan pesan "Pilihan tidak valid!" |

#### Proses Login (Maksimal 3 Kali)

| Langkah | Proses |
|---|---|
| 1 | Input `username` dan `password` (password tersamarkan) |
| 2 | Cocokkan username dan password dengan data `users` |
| 3 | Jika cocok, login berhasil dan dilanjutkan dengan pemeriksaan role |
| 4 | Jika tidak cocok, `percobaan += 1` dan program menampilkan sisa percobaan |
| 5 | Jika percobaan habis, kembali ke menu utama |

#### Proses Registrasi

| Langkah | Proses |
|---|---|
| 1 | Input `username` dan `password` (tidak boleh kosong) |
| 2 | Memeriksa apakah username belum digunakan |
| 3 | Menyimpan akun ke `users.json` dengan role `user` dan saldo `0` |
| 4 | Kembali ke menu utama |

### 4.2 Alur Menu Admin

[![Flowchart menu admin](https://github.com/user-attachments/assets/064cadf8-01d1-493c-bbea-befd8b18c481)](https://github.com/user-attachments/assets/064cadf8-01d1-493c-bbea-befd8b18c481)

#### Daftar Menu Admin

Admin memilih menu melalui `input pilihan`, kemudian program mencocokkan nilainya menggunakan percabangan.

| Pilihan | Menu | Keterangan |
|---|---|---|
| `1` | Tambah data tenant | Menambahkan lapak baru |
| `2` | Tampilkan data tenant | Menampilkan seluruh tenant dalam tabel |
| `3` | Ubah data tenant | Mengubah data tenant yang sudah ada |
| `4` | Hapus data tenant | Menghapus tenant setelah konfirmasi |
| `5` | Riwayat transaksi & cetak ulang invoice | Melanjutkan ke flowchart Invoice & Riwayat Transaksi (4.8) |
| `6` | Laporan ringkas | Melanjutkan ke flowchart Laporan Ringkas (4.4) |
| `7` | Tambah saldo user | Admin memilih user dan mengisi nominal Rp10.000 sampai Rp10.000.000 |
| `8` | Logout | Menampilkan pesan logout berhasil dan kembali ke menu utama |
| Lainnya | - | Menampilkan pesan "Pilihan tidak valid!" |

#### 1. Tambah Data Tenant

| Langkah | Proses | Validasi / Hasil |
|---|---|---|
| 1 | Input nama tenant | Tidak boleh kosong |
| 2 | Cek duplikat | Jika nama sudah ada, tampil pesan dan kembali ke menu |
| 3 | `kategori = pilih_kategori()` | Memilih kategori 1 sampai 5 |
| 4 | `harga = input_angka("Harga sewa (Rp)")` | Harus berupa angka |
| 5 | Menentukan stok lapak | Lapak baru memiliki kuota 20 |
| 6 | Membuat ID baru | ID otomatis bertambah 1 |
| 7 | Menyimpan ke `tenant.json` | Data tersimpan |
| 8 | Menampilkan pesan berhasil | Kembali ke menu admin |

#### 2. Tampilkan Data Tenant

| Langkah | Proses | Hasil |
|---|---|---|
| 1 | Memanggil `tampilkan_data()` | Data tenant tampil dalam tabel `PrettyTable`, terurut berdasarkan kategori |
| 2 | Memeriksa data kosong | Jika kosong, tampil pesan "Data tenant masih kosong" |
| 3 | Kembali ke menu admin | Admin dapat memilih menu lainnya |

#### 3. Ubah Data Tenant

| Langkah | Proses | Validasi / Hasil |
|---|---|---|
| 1 | Menampilkan data tenant | Admin melihat daftar tenant |
| 2 | Memilih tenant berdasarkan nomor tabel | Jika tidak ditemukan, tampil pesan error |
| 3 | Input data baru (nama, kategori, harga, stok) | Angka divalidasi dengan `input_angka()`, stok tidak boleh melebihi 20 |
| 4 | Menyimpan perubahan ke `tenant.json` | Tenant hasil sewa hanya dapat diubah namanya |
| 5 | Menampilkan pesan berhasil | Kembali ke menu admin |

#### 4. Hapus Data Tenant

| Langkah | Proses | Validasi / Hasil |
|---|---|---|
| 1 | Menampilkan data tenant | Admin melihat daftar tenant |
| 2 | Memilih tenant berdasarkan nomor tabel | Jika tidak ditemukan, tampil pesan error |
| 3 | Konfirmasi hapus (`y/n`) | Jika `n`, tampil pesan "Penghapusan dibatalkan" |
| 4 | Menghapus data dari list dan menyimpan ke `tenant.json` | Jika lapak induk dihapus, tenant hasil sewanya ikut terhapus |
| 5 | Menampilkan pesan berhasil | Kembali ke menu admin |

#### Konektor ke Flowchart Lain

| Simbol di Flowchart | Arti |
|---|---|
| Pentagon hijau (atas) | Titik masuk dari proses login dengan role `admin` |
| Pentagon hijau (menu 5 dan 6) | Alur dilanjutkan di flowchart fungsi lain |
| Lingkaran bertanda huruf | Kembali ke awal Menu Admin |

### 4.3 Alur Menu User

[![Flowchart menu user](https://github.com/user-attachments/assets/64992ee3-0c81-4b07-8418-80199f1a87b5)](https://github.com/user-attachments/assets/64992ee3-0c81-4b07-8418-80199f1a87b5)

#### Tampilan Awal

Setelah login dengan role `user`, program menjalankan `bersihkan_layar()` kemudian menampilkan header dan menu.

| Elemen | Isi |
|---|---|
| Judul | `=== MENU USER - {username} ===` |
| Saldo | `Saldo: Rp{saldo}` (diambil dari data user yang sedang login) |
| Input | `input pilihan` |

#### Daftar Menu User

| Pilihan | Menu | Aksi |
|---|---|---|
| `1` | Tampilkan data tenant | Menampilkan semua tenant, lalu kembali ke menu user |
| `2` | Top up saldo | Melanjutkan ke flowchart Top Up Saldo (4.5) |
| `3` | Reservasi & bayar tenant | Melanjutkan ke flowchart Reservasi dan Pembayaran (4.6) |
| `4` | Riwayat transaksi & cetak ulang invoice | Melanjutkan ke flowchart Invoice & Riwayat Transaksi (4.8) |
| `5` | Logout | Menampilkan pesan logout berhasil dan kembali ke menu utama |
| Lainnya | - | Menampilkan pesan "Pilihan tidak valid!" |

#### Detail Menu 1: Tampilkan Data Tenant

| Langkah | Proses | Hasil |
|---|---|---|
| 1 | Memanggil `tampilkan_data()` | Semua tenant tampil dalam tabel `PrettyTable` |
| 2 | Menampilkan "Tekan ENTER untuk kembali..." | Program menunggu input ENTER |
| 3 | Kembali ke menu user | Menu dan saldo ditampilkan ulang |

#### Alur Logout (Menu 5)

| Langkah | Proses |
|---|---|
| 1 | Menampilkan pesan "Logout berhasil" |
| 2 | Jeda menggunakan `time.sleep()` |
| 3 | Kembali ke Menu Utama (Login / Registrasi / Keluar) |

#### Penjelasan Konektor

| Simbol di Flowchart | Arti |
|---|---|
| Pentagon hijau (atas) | Titik masuk dari proses login dengan role `user` |
| Lingkaran `A` | Kembali ke awal Menu User |
| Pentagon hijau (menu 2, 3, 4) | Alur berlanjut di flowchart fungsi masing-masing |
| Pentagon hijau (setelah logout) | Kembali ke Menu Utama |

### 4.4 Laporan Ringkas (Admin)

[![Flowchart laporan ringkas](https://github.com/user-attachments/assets/6346f393-37cb-46a6-8bfe-c6aacb93926d)](https://github.com/user-attachments/assets/6346f393-37cb-46a6-8bfe-c6aacb93926d)

#### Gambaran Umum

Fitur ini dipanggil dari Menu Admin melalui konektor `P`. Program membaca seluruh data `transaksi.json`, menghitung total pendapatan dan jumlah transaksi reservasi, kemudian menampilkan tenant terlaris.

#### Variabel yang Digunakan

| Variabel | Fungsi |
|---|---|
| `pendapatan` | Total uang dari seluruh transaksi bertipe reservasi |
| `jumlah` | Jumlah transaksi reservasi |
| `penjualan` | Penampung jumlah `qty` per tenant untuk mencari tenant terlaris dan membuat tabel per tenant |

#### Alur Proses

| No | Proses | Kondisi | Hasil |
|---|---|---|---|
| 1 | Memulai laporan ringkas | - | Program masuk ke fungsi laporan |
| 2 | Inisialisasi `pendapatan`, `jumlah`, dan `penjualan` | - | Semua variabel diatur ke nilai awal |
| 3 | Memeriksa apakah masih ada transaksi | Ya | Lanjut ke langkah 4 |
| 3 | Memeriksa apakah masih ada transaksi | Tidak | Perulangan selesai, lanjut ke langkah 6 |
| 4 | Memeriksa tipe transaksi | Reservasi | Lanjut ke langkah 5 |
| 4 | Memeriksa tipe transaksi | Bukan reservasi | Dilewati dan kembali ke langkah 3 |
| 5 | Menambahkan data ke laporan | - | `pendapatan` bertambah, `jumlah` bertambah 1, dan qty tenant ditambahkan ke `penjualan` |
| 6 | Menampilkan ringkasan | - | Total pendapatan dan jumlah transaksi ditampilkan |
| 7 | Memeriksa apakah `penjualan` kosong | Ya | Menampilkan "Data belum ada" |
| 7 | Memeriksa apakah `penjualan` kosong | Tidak | Lanjut ke langkah 8 |
| 8 | Mencari tenant terlaris | - | Tenant dengan qty terbanyak dipilih |
| 9 | Menampilkan tenant terlaris dan tabel per tenant | - | Hasil ditampilkan menggunakan `PrettyTable` |

#### Penjelasan Konektor

| Simbol di Flowchart | Arti |
|---|---|
| Pentagon hijau `P` (atas) | Titik masuk dari Menu Admin |
| Lingkaran `A` | Titik kembali ke bagian sebelumnya dalam alur laporan |
| Pentagon hijau `A` (bawah) | Kembali ke Menu Admin |

### 4.5 Top Up Saldo (User)

[![Flowchart top up saldo](https://github.com/user-attachments/assets/d3f48b1a-3c39-41fd-9c39-64ea2bf36ada)](https://github.com/user-attachments/assets/d3f48b1a-3c39-41fd-9c39-64ea2bf36ada)

#### Gambaran Umum

Fitur ini dipanggil dari Menu User (pilihan `2`). User mengisi saldo dengan nominal yang dibatasi oleh `MIN_TOPUP` dan `MAX_TOPUP`. Transaksi kemudian dicatat dengan tipe `Top Up`.

#### Variabel dan Konstanta

| Nama | Fungsi |
|---|---|
| `MIN_TOPUP` | Batas minimal nominal top up, yaitu Rp10.000 |
| `MAX_TOPUP` | Batas maksimal nominal per transaksi, yaitu Rp10.000.000 |
| `nominal` | Jumlah uang yang diinput user dan divalidasi dengan `input_angka()` |
| `users[username]['saldo']` | Saldo user yang sedang login |
| `trx` | Hasil `catat_transaksi()`, berisi data transaksi termasuk `trx['kode']` |

#### Alur Proses

| No | Proses | Kondisi | Hasil |
|---|---|---|---|
| 1 | Menampilkan judul `=== TOP UP SALDO ===` | - | Halaman top up ditampilkan |
| 2 | Menampilkan saldo saat ini, minimal, dan maksimal top up | - | Nominal ditampilkan melalui `rupiah()` |
| 3 | `nominal = input_angka("Nominal top up (Rp)")` | - | Input harus berupa angka |
| 4 | Memeriksa `nominal < MIN_TOPUP` | Ya | Menampilkan pesan top up minimal dan kembali ke Menu User |
| 5 | Memeriksa `nominal > MAX_TOPUP` | Ya | Menampilkan pesan top up maksimal dan kembali ke Menu User |
| 6 | `konfirmasi("Lanjutkan top up?")` | - | Konfirmasi diulang sampai jawaban `y` atau `n` |
| 7 | Memeriksa jawaban konfirmasi | `n` | Top up dibatalkan |
| 8 | Menambah saldo | `y` | `saldo = saldo + nominal` |
| 9 | Menyimpan saldo ke `users.json` | - | Data saldo tersimpan |
| 10 | Memanggil `catat_transaksi(...)` | - | Transaksi bertipe `Top Up` dicatat ke `transaksi.json` |
| 11 | Menampilkan pesan berhasil | - | Saldo sekarang dan kode transaksi ditampilkan |
| 12 | Menunggu input ENTER | - | Kembali ke Menu User |

#### Validasi Nominal

| Kondisi | Pesan | Hasil |
|---|---|---|
| `nominal < MIN_TOPUP` | Top up minimal Rp10.000 | Ditolak |
| `nominal > MAX_TOPUP` | Top up maksimal Rp10.000.000 per transaksi | Ditolak |
| `MIN_TOPUP <= nominal <= MAX_TOPUP` | - | Lanjut ke konfirmasi |

#### Data yang Dicatat ke Transaksi

| Parameter `catat_transaksi` | Nilai | Keterangan |
|---|---|---|
| `username` | Username yang login | Pemilik transaksi |
| `tipe` | `Top Up` | Pembeda dengan transaksi reservasi |
| `tenant` | `None` | Top up tidak terkait tenant |
| `jumlah` | `nominal` | Jumlah uang yang ditambahkan |
| `qty` | `1` | Nilai tetap |
| `saldo_akhir` | Saldo sesudah top up | Untuk riwayat saldo |

#### Penjelasan Konektor

| Simbol di Flowchart | Arti |
|---|---|
| Pentagon hijau `E` (atas) | Titik masuk dari Menu User pilihan `2` |
| Lingkaran `A` (di kanan) | Kembali ke awal Menu User jika nominal ditolak atau top up dibatalkan |
| Lingkaran `A` (bawah) | Kembali ke awal Menu User setelah menekan ENTER |
| Pentagon hijau (paling bawah) | Kembali ke Menu User |

### 4.6 Reservasi & Pembayaran Tenant (User)

[![Flowchart reservasi dan pembayaran tenant](https://github.com/user-attachments/assets/d5af8391-63bd-4057-bb81-989420c6b539)](https://github.com/user-attachments/assets/d5af8391-63bd-4057-bb81-989420c6b539)

#### Gambaran Umum

Fitur ini dipanggil dari Menu User (pilihan `3`). User memilih lapak berdasarkan ID, menentukan jumlah lapak, memberi nama tenant miliknya, lalu membayar menggunakan saldo e-money.

Setelah pembayaran berhasil, kuota lapak induk berkurang, tenant baru berstatus `Disewa` ditambahkan, transaksi dicatat, dan invoice dicetak.

#### Variabel yang Digunakan

| Variabel | Fungsi |
|---|---|
| `id_tenant` | ID lapak yang dipilih user dan divalidasi dengan `input_angka()` |
| `tenant` | Data lapak hasil pencarian `cari_tenant()` |
| `qty` | Jumlah lapak yang ingin disewa |
| `total` | Total biaya (`harga * qty`) |
| `users[username]['saldo']` | Saldo user yang sedang login |
| `trx` | Hasil `catat_transaksi()`, digunakan untuk mencetak invoice |

#### Alur Proses

| No | Proses | Kondisi | Hasil |
|---|---|---|---|
| 1 | Menampilkan judul `=== RESERVASI & PEMBAYARAN TENANT ===` | - | Halaman reservasi ditampilkan |
| 2 | Menampilkan data tenant | - | Daftar tenant tampil dalam tabel |
| 3 | `id_tenant = input_angka(...)` | - | Input harus berupa angka |
| 4 | Mencari lapak berdasarkan ID | Tidak ditemukan | Menampilkan pesan error dan kembali ke Menu User |
| 5 | Mengambil data lapak yang ditemukan | Ditemukan | Lanjut ke langkah 6 |
| 6 | Memeriksa stok lapak | Stok habis | Menampilkan pesan stok habis |
| 7 | `qty = input_angka(...)` | - | User memasukkan jumlah lapak yang ingin disewa |
| 8 | Memeriksa apakah `qty` melebihi stok | Ya | Menampilkan pesan jumlah tidak valid |
| 9 | Memasukkan nama tenant | Kosong | Menampilkan pesan dan menolak input |
| 10 | Menghitung `total = harga * qty` | - | Ringkasan dan total bayar ditampilkan |
| 11 | Memeriksa saldo `< total` | Ya | Menampilkan pesan saldo tidak cukup beserta selisihnya |
| 12 | `konfirmasi("Lanjutkan pembayaran?")` | Jawaban `n` | Pembayaran dibatalkan |
| 13 | Mengurangi saldo user dan kuota lapak induk | Jawaban `y` | `saldo -= total`, `stok -= qty`, tenant baru berstatus `Disewa` ditambahkan |
| 14 | Menyimpan perubahan ke `users.json` dan `tenant.json` | - | Data tersimpan |
| 15 | Memanggil `catat_transaksi(...)` | - | Transaksi bertipe `Reservasi` dicatat |
| 16 | Menampilkan pesan pembayaran berhasil | - | Pembayaran berhasil diproses |
| 17 | Memanggil `cetak_invoice(trx)` | - | Invoice `.txt` dibuat di folder `invoice` |
| 18 | Menunggu input ENTER | - | Kembali ke Menu User |

#### Validasi Pemesanan

| Validasi | Kondisi Gagal | Hasil |
|---|---|---|
| ID lapak | Tidak ada di `tenant.json` | Ditolak |
| Stok lapak | Stok `0` | Ditolak |
| Jumlah lapak | `qty` melebihi stok tersedia | Ditolak |
| Nama tenant | Kosong | Ditolak |
| Saldo | Saldo `< total` | Pembayaran ditolak, user dapat melakukan top up |
| Konfirmasi | Jawaban `n` | Dibatalkan, tidak ada perubahan data |

#### Data yang Berubah Setelah Pembayaran

| File | Perubahan |
|---|---|
| `users.json` | Saldo user berkurang sebesar `total` |
| `tenant.json` | Stok lapak induk berkurang sebesar `qty`, tenant baru berstatus `Disewa` ditambahkan |
| `transaksi.json` | Bertambah satu transaksi bertipe `Reservasi` |
| Folder `invoice/` | Bertambah satu file invoice `.txt` |

#### Penjelasan Konektor

| Simbol di Flowchart | Arti |
|---|---|
| Pentagon hijau (atas) | Titik masuk dari Menu User pilihan `3` |
| Lingkaran `A` (di kanan) | Kembali ke awal Menu User jika validasi gagal atau pembayaran dibatalkan |
| Lingkaran `A` (bawah) | Kembali ke Menu User setelah menekan ENTER |
| Pentagon hijau (paling bawah) | Kembali ke Menu User |
| Silinder pink | Penyimpanan data ke file JSON |

### 4.7 Fungsi Pendukung

Tiga fungsi berikut dipanggil dari fitur lain, seperti top up, reservasi, dan pengelolaan tenant. Fungsi-fungsi ini tidak ditampilkan langsung sebagai menu kepada user.

#### 1. `perbarui_status(tenant)`

[![Flowchart perbarui_status](https://github.com/user-attachments/assets/bf00d338-15a3-46bb-b5eb-ab7ed6ec0dd4)](https://github.com/user-attachments/assets/bf00d338-15a3-46bb-b5eb-ab7ed6ec0dd4)

Fungsi `perbarui_status(tenant)` digunakan untuk memperbarui kolom status tenant berdasarkan sisa stok lapak.

**Logika fungsi:**

| Kondisi | Hasil |
|---|---|
| `tenant['stok'] > 0` | `tenant['status'] = "Tersedia"` |
| `tenant['stok'] == 0` | `tenant['status'] = "Penuh"` |

**Detail fungsi:**

| Detail | Keterangan |
|---|---|
| Tujuan | Memperbarui status ketersediaan lapak |
| Dipanggil dari | Tambah, ubah, hapus tenant, dan reservasi |
| Parameter | Data tenant dalam bentuk dictionary |
| Nilai kembali | Tidak ada, data tenant langsung diubah |

#### 2. `buat_kode()`

[![Flowchart buat_kode](https://github.com/user-attachments/assets/a5f705a3-1e85-4dea-b26f-83051faf188b)](https://github.com/user-attachments/assets/a5f705a3-1e85-4dea-b26f-83051faf188b)

Fungsi `buat_kode()` digunakan untuk membuat kode transaksi unik. Contoh format kode: `TRX-251103200500`.

**Alur proses:**

| No | Proses | Hasil |
|---|---|---|
| 1 | Membaca data transaksi dengan `baca_trx()` | Daftar transaksi dimuat |
| 2 | Menyusun `kode = "TRX-" + tanggal waktu` | Format waktu menggunakan `datetime.now().strftime(...)` |
| 3 | Mengatur `ada = False` | Penanda bahwa kode belum digunakan |
| 4 | Memeriksa apakah masih ada transaksi | Jika ada, lanjut ke langkah 5; jika tidak, lanjut ke langkah 6 |
| 5 | Memeriksa apakah kode sama dengan kode transaksi yang sudah ada | Jika sama, `ada = True` |
| 6 | Memeriksa `ada == False` | Jika benar, kembalikan kode; jika salah, buat kode baru |

**Detail fungsi:**

| Detail | Keterangan |
|---|---|
| Tujuan | Memastikan tidak ada dua transaksi dengan kode yang sama |
| Dipanggil dari | `catat_transaksi()` |
| Nilai kembali | String kode transaksi |

#### 3. `catat_transaksi(username, tipe, tenant, jumlah, qty, saldo_akhir)`

[![Flowchart catat_transaksi](https://github.com/user-attachments/assets/ad7826bb-1ea6-4a60-abfc-f03df682adbe)](https://github.com/user-attachments/assets/ad7826bb-1ea6-4a60-abfc-f03df682adbe)

Fungsi `catat_transaksi()` digunakan untuk menyimpan satu transaksi baru ke dalam file `transaksi.json`.

**Parameter fungsi:**

| Parameter | Fungsi |
|---|---|
| `username` | Pemilik transaksi |
| `tipe` | Jenis transaksi (`Top Up`, `Top Up Admin`, atau `Reservasi`) |
| `tenant` | Data tenant, atau `None` untuk transaksi top up |
| `jumlah` | Nominal uang transaksi |
| `qty` | Jumlah lapak |
| `saldo_akhir` | Saldo user setelah transaksi |

**Alur proses:**

| No | Proses | Hasil |
|---|---|---|
| 1 | Membaca data dengan `baca_trx()` | Daftar transaksi dimuat |
| 2 | Membuat `waktu` dari `datetime.now()` | Format `YYYY-MM-DD HH:MM:SS` |
| 3a | Memeriksa apakah `tenant` tersedia | Jika tersedia, `tenant_id` dan `tenant_nama` diambil dari data tenant |
| 3b | Jika `tenant` tidak tersedia | `tenant_id = 0` dan `tenant_nama = "-"` |
| 4 | Menyusun data `trx` dengan `kode = buat_kode()` | Dictionary berisi seluruh field transaksi |
| 5 | Menjalankan `transaksi.append(trx)` | Transaksi ditambahkan ke list |
| 6 | Menyimpan data ke `transaksi.json` | Data tersimpan |
| 7 | Mengembalikan `trx` | Digunakan untuk menampilkan kode dan mencetak invoice |

**Field di dalam `trx`:**

| Field | Isi |
|---|---|
| `kode` | Hasil dari `buat_kode()` |
| `waktu` | Tanggal dan jam transaksi |
| `username` | Pemilik transaksi |
| `tipe` | `Top Up`, `Top Up Admin`, atau `Reservasi` |
| `tenant_id` | ID tenant atau nilai `0` |
| `tenant_nama` | Nama tenant atau tanda `-` |
| `qty` | Jumlah lapak |
| `jumlah` | Nominal transaksi |
| `saldo_akhir` | Saldo setelah transaksi |

### 4.8 Invoice & Riwayat Transaksi

Tiga fungsi berikut digunakan dari Menu User (pilihan `4`), Menu Admin (pilihan `5`), dan setelah pembayaran reservasi.

#### 1. `cetak_invoice(trx)`

[![Flowchart cetak_invoice](https://github.com/user-attachments/assets/a1e089f6-8b76-4ac0-af52-a4763ccc13c5)](https://github.com/user-attachments/assets/a1e089f6-8b76-4ac0-af52-a4763ccc13c5)

Fungsi `cetak_invoice(trx)` digunakan untuk membuat invoice dari satu transaksi, menampilkannya di layar, kemudian menyimpannya sebagai file `.txt`.

**Alur proses:**

| No | Proses | Hasil |
|---|---|---|
| 1 | Menyusun teks invoice dari data `trx` | Berisi kode, waktu, pelanggan, tenant, kategori, jumlah lapak, total bayar, dan sisa saldo |
| 2 | Menampilkan invoice di layar | User langsung melihat struk transaksi |
| 3 | Menentukan nama file di folder `invoice/` | Contoh: `invoice/TRX-xxxx.txt` |
| 4 | Menulis teks ke file menggunakan `try` | File invoice dibuat |
| 5a | Proses berhasil | Menampilkan pesan "Invoice tersimpan di ..." |
| 5b | Proses gagal (`except`) | Menampilkan pesan gagal menyimpan, tetapi program tetap berjalan |

**Detail fungsi:**

| Detail | Keterangan |
|---|---|
| Parameter | `trx`, dictionary transaksi dari `catat_transaksi()` |
| Dipanggil dari | Proses reservasi dan `cetak_ulang_invoice()` |
| Nilai kembali | Tidak ada |

#### 2. `tampilkan_riwayat(username, role)`

[![Flowchart tampilkan_riwayat](https://github.com/user-attachments/assets/2a0cfd1a-1337-4f08-b05d-764fecf13d8e)](https://github.com/user-attachments/assets/2a0cfd1a-1337-4f08-b05d-764fecf13d8e)

Fungsi `tampilkan_riwayat(username, role)` digunakan untuk menampilkan riwayat transaksi dalam bentuk tabel.

Admin dapat melihat semua transaksi, sedangkan user hanya dapat melihat transaksi miliknya sendiri.

**Alur proses:**

| No | Proses | Hasil |
|---|---|---|
| 1 | Membuat tabel `PrettyTable` dengan kolom transaksi | Kode, Waktu, User, Tipe, Tenant, Nama Usaha, Qty, Jumlah, dan Saldo Akhir |
| 2 | Mengatur `ada = False` | Penanda belum ada baris transaksi |
| 3 | Memeriksa apakah masih ada transaksi | Jika ada, lanjut ke langkah 4; jika tidak, lanjut ke langkah 5 |
| 4 | Memeriksa `role == admin` atau username cocok | Jika sesuai, baris ditambahkan ke tabel dan `ada = True`; jika tidak, dilewati |
| 5 | Memeriksa `ada == True` | Jika benar, tampilkan tabel; jika salah, tampilkan "Belum ada transaksi" |

**Hak akses berdasarkan role:**

| Role | Data yang Ditampilkan |
|---|---|
| `admin` | Seluruh transaksi semua user |
| `user` | Hanya transaksi dengan username yang sama |

#### 3. `cetak_ulang_invoice(username, role)`

[![Flowchart cetak_ulang_invoice](https://github.com/user-attachments/assets/d079991d-5dce-44c9-9e87-f266f92b86dc)](https://github.com/user-attachments/assets/d079991d-5dce-44c9-9e87-f266f92b86dc)

Fungsi `cetak_ulang_invoice(username, role)` digunakan untuk mencetak ulang invoice berdasarkan kode transaksi yang dimasukkan oleh user. Fungsi ini memiliki beberapa validasi untuk memastikan transaksi ditemukan dan pengguna memiliki hak akses.

**Alur proses:**

| No | Proses | Kondisi | Hasil |
|---|---|---|---|
| 1 | Menampilkan riwayat dengan `tampilkan_riwayat()` | - | User melihat daftar kode transaksi |
| 2 | Memeriksa keberadaan transaksi | Tidak ada | Menampilkan "Riwayat kosong" |
| 3 | Memasukkan kode transaksi | - | Program mencari kode di `transaksi.json` |
| 4 | Memeriksa apakah kode ditemukan | Tidak ditemukan | Menampilkan "Kode tidak ditemukan" |
| 5 | Memeriksa hak akses | Bukan admin dan bukan pemilik transaksi | Menampilkan pesan tidak berhak |
| 6 | Memeriksa tipe transaksi | Bukan `Reservasi` | Menampilkan pesan bahwa transaksi tidak memiliki invoice |
| 7 | Memanggil `cetak_invoice(trx)` | Lolos semua validasi | Invoice ditampilkan dan disimpan ulang |

**Validasi yang Dilakukan:**

| Validasi | Alasan |
|---|---|
| Kode transaksi ditemukan | Mencegah error ketika kode tidak ada |
| Hak akses | User tidak boleh melihat invoice milik orang lain |
| Tipe transaksi | Invoice hanya dibuat untuk transaksi reservasi, bukan transaksi top up |

---

## 5. 📋 Daftar Fitur per Role

### 🌐 Umum (Tanpa Login)

| Fitur | Keterangan |
|---|---|
| Login | Maksimal 3 kali percobaan, password tersembunyi saat diketik |
| Registrasi | Username unik, tidak boleh kosong, tidak boleh mengandung spasi; akun baru otomatis memiliki role `user` dan saldo Rp0 |
| Keluar | Menutup program |

### 👑 Admin

| No | Fitur | Keterangan |
|:--:|---|---|
| 1 | Tambah data tenant | Input nama, kategori, dan harga sewa; lapak baru otomatis memiliki kuota 20 |
| 2 | Tampilkan data tenant | Tabel terurut per kategori, lapak induk diikuti tenant hasil sewa |
| 3 | Ubah data tenant | Mengubah nama, kategori, harga, dan stok; tenant hasil sewa hanya dapat diubah namanya |
| 4 | Hapus data tenant | Dengan konfirmasi `y/n`; menghapus lapak induk juga menghapus tenant hasil sewanya |
| 5 | Riwayat transaksi & cetak ulang invoice | Melihat transaksi seluruh user |
| 6 | Laporan ringkas | Menampilkan total pendapatan, jumlah transaksi reservasi, dan tenant terlaris |
| 7 | Tambah saldo user | Admin menambah saldo user dengan nominal Rp10.000 sampai Rp10.000.000 |
| 8 | Logout | Kembali ke menu utama |

### 👤 User

| No | Fitur | Keterangan |
|:--:|---|---|
| 1 | Tampilkan data tenant | Melihat daftar lapak, stok, dan status |
| 2 | Top up saldo | Minimal Rp10.000 dan maksimal Rp10.000.000 per transaksi, dengan konfirmasi |
| 3 | Reservasi & bayar tenant | Memilih lapak, jumlah, nama tenant, kemudian membayar menggunakan saldo |
| 4 | Riwayat transaksi & cetak ulang invoice | Melihat transaksi milik sendiri |
| 5 | Logout | Kembali ke menu utama |

---

## 6. 📸 Screenshot Output & Penjelasan

> 📝 **Petunjuk untuk tim:** Jalankan program, ambil screenshot setiap tampilan, kemudian simpan di folder `docs/screenshots/` menggunakan nama file seperti di bawah. Pastikan file gambar sudah diunggah ke repositori GitHub agar dapat ditampilkan. Hapus petunjuk ini setelah semua screenshot terpasang.

### 6.1 Menu Utama

![Menu Utama](docs/screenshots/01-menu-utama.png)

**Penjelasan:**

Tampilan awal program dengan tiga pilihan, yaitu Login, Registrasi, dan Keluar. Input selain angka 1 sampai 3 akan menampilkan pesan "Pilihan tidak valid".

### 6.2 Registrasi

![Registrasi](docs/screenshots/02-registrasi.png)

**Penjelasan:**

User mengisi username dan password. Program memeriksa apakah username kosong, mengandung spasi, atau sudah digunakan. Jika valid, akun disimpan ke `users.json` dengan role `user` dan saldo Rp0.

### 6.3 Login

![Login](docs/screenshots/03-login.png)

**Penjelasan:**

User memasukkan username dan password. Password disamarkan saat diketik. Jika salah, program menampilkan sisa percobaan. Setelah 3 kali gagal, pengguna kembali ke menu utama.

### 6.4 Menu Admin

![Menu Admin](docs/screenshots/04-menu-admin.png)

**Penjelasan:**

Admin memiliki 8 menu untuk mengelola tenant, melihat riwayat transaksi, mencetak ulang invoice, melihat laporan ringkas, menambah saldo user, dan logout.

### 6.5 Tampilkan Data Tenant

![Data Tenant](docs/screenshots/05-data-tenant.png)

**Penjelasan:**

Data tampil dalam tabel dengan kolom No, Nama Tenant, Kategori, Harga Sewa, Stok, Status, dan Penyewa. Lapak induk berstatus `Tersedia` atau `Penuh`, sedangkan tenant hasil sewa berstatus `Disewa` dan tampil di bawah lapak induknya.

### 6.6 Tambah Data Tenant

![Tambah Tenant](docs/screenshots/06-tambah-tenant.png)

**Penjelasan:**

Admin mengisi nama tenant, memilih kategori 1 sampai 5, dan menentukan harga sewa. Nama yang kosong atau sudah digunakan akan ditolak. Lapak baru otomatis memiliki stok 20.

### 6.7 Ubah Data Tenant

![Ubah Tenant](docs/screenshots/07-ubah-tenant.png)

**Penjelasan:**

Admin memilih tenant berdasarkan nomor di tabel, kemudian mengubah data tenant. Stok tidak boleh melebihi 20.

### 6.8 Hapus Data Tenant

![Hapus Tenant](docs/screenshots/08-hapus-tenant.png)

**Penjelasan:**

Program meminta konfirmasi `y/n` sebelum menghapus tenant. Jika yang dihapus adalah lapak induk, tenant hasil sewanya juga ikut terhapus dan peringatan ditampilkan terlebih dahulu.

### 6.9 Laporan Ringkas

![Laporan](docs/screenshots/09-laporan.png)

**Penjelasan:**

Laporan menampilkan total pendapatan, jumlah transaksi reservasi, tenant terlaris, dan tabel jumlah lapak yang dipesan per tenant.

### 6.10 Tambah Saldo User (Admin)

![Tambah Saldo](docs/screenshots/10-tambah-saldo.png)

**Penjelasan:**

Admin melihat daftar user beserta saldonya, memilih username tujuan, lalu mengisi nominal saldo. Transaksi dicatat dengan tipe `Top Up Admin`.

### 6.11 Menu User

![Menu User](docs/screenshots/11-menu-user.png)

**Penjelasan:**

User memiliki 5 menu, yaitu tampilkan tenant, top up saldo, reservasi, riwayat transaksi, dan logout.

### 6.12 Top Up Saldo

![Top Up](docs/screenshots/12-top-up.png)

**Penjelasan:**

Program menampilkan saldo saat ini serta batas minimal dan maksimal top up. Nominal di luar batas akan ditolak. Setelah dikonfirmasi, saldo bertambah dan kode transaksi ditampilkan.

### 6.13 Reservasi & Pembayaran

![Reservasi](docs/screenshots/13-reservasi.png)

**Penjelasan:**

User memilih lapak, menentukan jumlah, dan memasukkan nama tenant. Program menampilkan ringkasan serta total pembayaran. Jika saldo kurang, program menampilkan selisih kekurangannya. Jika saldo cukup dan pembayaran dikonfirmasi, stok berkurang dan saldo terpotong.

### 6.14 Invoice

![Invoice](docs/screenshots/14-invoice.png)

**Penjelasan:**

Setelah pembayaran reservasi berhasil, invoice ditampilkan di layar dan disimpan sebagai file `.txt` di folder `invoice`. Invoice berisi kode transaksi, waktu, pelanggan, tenant, kategori, jumlah lapak, total bayar, dan sisa saldo.

### 6.15 Riwayat Transaksi

![Riwayat](docs/screenshots/15-riwayat.png)

**Penjelasan:**

Tabel berisi kode, waktu, user, tipe transaksi, tenant, nama usaha, qty, jumlah, dan saldo akhir. User hanya melihat transaksinya sendiri, sedangkan admin dapat melihat semua transaksi. Invoice reservasi dapat dicetak ulang menggunakan kode transaksi.

---

## 7. 🚀 Cara Menjalankan Program

### 1. Clone Repositori

Buka terminal atau Command Prompt, kemudian jalankan perintah berikut:

```bash
git clone https://github.com/APASrah/PA-APASrah.git
cd PA-APASrah
```

### 2. Pasang Library

Program menggunakan library `prettytable` untuk menampilkan tabel dan `pwinput` untuk menyamarkan password ketika diketik.

```bash
pip install prettytable pwinput
```

### 3. Jalankan Program

```bash
python main.py
```

### Penyimpanan Data

Program membaca data dari folder `C:\ApasProjek`. Pastikan file `users.json` dan `tenant.json` sudah tersedia di folder tersebut.

Jika ingin menggunakan lokasi lain, ubah variabel `folder_data` pada kode program.

File `transaksi.json` dan folder `invoice` dibuat secara otomatis oleh program sesuai implementasinya.

### Contoh Struktur Folder

```text
C:\
└── ApasProjek\
    ├── users.json
    ├── tenant.json
    ├── transaksi.json
    └── invoice\
        ├── TRX-xxxx.txt
        └── TRX-yyyy.txt
```

### Contoh Isi `users.json`

Berikut contoh struktur data akun admin dan user:

```json
{
    "admin": {
        "password": "ganti_password_ini",
        "role": "admin",
        "saldo": 0
    },
    "budi": {
        "password": "rahasia123",
        "role": "user",
        "saldo": 0
    }
}
```

> **Catatan:** Username dan password di atas hanya contoh. Ganti dengan data akun yang digunakan pada program.

---

<div align="center">

**Dibuat oleh Tim APASrah**

*Sistem Reservasi Tenant Bazar*

</div>
