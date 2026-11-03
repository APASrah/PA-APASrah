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
5. [Struktur Folder dan File](#5-Struktur--Folder--dan--File)
6. [Persiapan](#6-Persiapan)
7. [Penjelasan Kode Program](#7-Penjelasan--kode--program)
8. [Struktur Data JSON](#8-Struktur--Data--JSON)
9. [Aturan dan Validasi Sistem](#9-Aturan--dan--Validasi)
10. [Alur Kerja Sistem](#10-Alur--Kerja-sistem)
11. [Daftar Fitur per Role](#11-daftar-fitur-per-role)
12. [Screenshot Output & Penjelasan](#12-screenshot-output--penjelasan)

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
| 2 | **Lithalia Geminifer Addawiyah** | `2609116088` | Flowchart, Laporan | Flowchart, Laporan | [@lithaliageminiferaddawiyah](https://github.com/lithaliageminiferaddawiyah) |
| 3 | **Muhammad Fahry Praditya** | `2609116104` | Coding, Flowchart, Laporan | Ngoding, Pengembangan dan revisi kode, revisi flowchart, revisi laporan,  | [@muhammadfahrypraditya](https://github.com/muhammadfahrypraditya) |
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

## 5. Struktur Folder dan File

Program menggunakan folder `C:\ApasProjek` sebagai lokasi penyimpanan data.

```text
C:\ApasProjek
│
├── main.py
│
├── users.json
│
├── tenant.json
│
├── transaksi.json
│
└── invoice
    ├── TRX-261103201530-482.txt
    ├── TRX-261103201645-731.txt
    └── ...
```

**Penjelasan setiap file:**

| File/Folder | Fungsi |
|---|---|
| `main.py` | File utama yang berisi seluruh kode program Python. |
| `users.json` | Menyimpan informasi akun pengguna, password, role, dan saldo. |
| `tenant.json` | Menyimpan data tenant, kategori, harga, stok, status, dan informasi penyewa. |
| `transaksi.json` | Menyimpan seluruh riwayat transaksi. |
| `invoice` | Folder untuk menyimpan invoice reservasi dalam format `.txt`. |

**Catatan:** File `users.json` dan `tenant.json` harus tersedia sebelum program dijalankan. File `transaksi.json` akan diinisialisasi sebagai list kosong jika belum tersedia. Folder `invoice` dibuat ketika invoice disimpan.

## 6. Cara Instalasi dan Menjalankan Program

### 6.1 Persiapan

Pastikan komputer sudah memiliki Python. Kemudian siapkan folder proyek sesuai lokasi yang digunakan program.

### 6.2 Instalasi Library

Buka terminal atau Command Prompt, kemudian jalankan perintah berikut:

```bash
pip install prettytable pwinput
```

Perintah tersebut digunakan untuk menginstal library yang dibutuhkan oleh program.

### 6.3 Menyiapkan File JSON

Pastikan terdapat file `users.json` dan `tenant.json` di dalam folder `C:\ApasProjek`.

Contoh isi awal `users.json`:

```json
{
    "admin": {
        "password": "admin123",
        "role": "admin",
        "saldo": 0
    },
    "budi": {
        "password": "rahasia123",
        "role": "user",
        "saldo": 50000
    }
}
```

Contoh isi awal `tenant.json`:

```json
[
    {
        "id": 1,
        "nama": "Tenant Makanan A",
        "kategori": [
            "Makanan"
        ],
        "harga": 50000,
        "stok": 20,
        "status": "Tersedia"
    }
]
```

Contoh tersebut hanya data awal. Username, password, harga, dan tenant dapat disesuaikan.

### 6.4 Menjalankan Program

Masuk ke folder tempat file Python disimpan, kemudian jalankan:

```bash
python main.py
```

Jika nama file Python berbeda, sesuaikan nama file pada perintah tersebut.

### 6.5 Tampilan Awal Program

Ketika program berhasil dijalankan, sistem akan menampilkan menu utama:

```text
=== SISTEM RESERVASI TENANT BAZAR ===

1. Login
2. Registrasi
3. Keluar

Pilih menu:
```

Pengguna dapat memilih login, melakukan registrasi, atau keluar dari program.

## 7. Penjelasan Kode Program

### 7.1 Import Library

Bagian ini digunakan untuk memanggil library Python yang dibutuhkan oleh program.

```python
import os
import time
import json
import random
from datetime import datetime
from prettytable import PrettyTable
import pwinput
```

**Penjelasan:**

- `os`: Mengelola sistem operasi, seperti membersihkan layar dan membuat folder.
- `time`: Memberikan jeda waktu menggunakan `time.sleep()`.
- `json`: Membaca dan menyimpan data dalam format JSON.
- `random`: Menghasilkan angka acak untuk kode transaksi.
- `datetime`: Mengambil tanggal dan waktu saat transaksi dilakukan.
- `PrettyTable`: Menampilkan data dalam bentuk tabel.
- `pwinput`: Menyembunyikan karakter password ketika pengguna melakukan login atau registrasi.

### 7.2 Konfigurasi Folder dan Variabel

Bagian ini menentukan lokasi penyimpanan data serta nilai-nilai yang digunakan dalam program.

```python
folder_data = r"C:\ApasProjek"
path_users = folder_data + r"\users.json"
path_tenants = folder_data + r"\tenant.json"
path_transaksi = folder_data + r"\transaksi.json"
folder_invoice = folder_data + r"\invoice"

KATEGORI = ("Makanan", "Minuman", "Fashion", "Kerajinan", "Lainnya")
MAX_STOK = 20
MIN_TOPUP = 10000
MAX_TOPUP = 10000000
```

**Penjelasan:**

1. `folder_data` menentukan folder utama tempat penyimpanan data program.
2. `path_users` menunjukkan lokasi file data akun pengguna.
3. `path_tenants` menunjukkan lokasi file data tenant bazar.
4. `path_transaksi` menunjukkan lokasi penyimpanan riwayat transaksi.
5. `folder_invoice` merupakan folder untuk menyimpan invoice transaksi.
6. `KATEGORI` berisi lima kategori tenant yang tersedia.
7. `MAX_STOK` menentukan jumlah maksimal stok lapak, yaitu 20.
8. `MIN_TOPUP` menentukan nominal minimal pengisian saldo sebesar Rp10.000.
9. `MAX_TOPUP` menentukan nominal maksimal pengisian saldo sebesar Rp10.000.000 per transaksi.

### 7.3 Membaca dan Memuat Data JSON

Bagian ini digunakan untuk mengambil data akun, tenant, dan transaksi dari file JSON.

```python
try:
    with open(path_users, "r", encoding="utf-8") as f:
        users = json.load(f)
    with open(path_tenants, "r", encoding="utf-8") as f:
        tenants = json.load(f)
except FileNotFoundError:
    print("File data tidak ditemukan! Pastikan users.json dan tenant.json ada.")
    exit()
except json.JSONDecodeError:
    print("Isi file JSON rusak atau kosong!")
    exit()
```

**Penjelasan:**

- `open()` digunakan untuk membuka file JSON.
- `json.load()` membaca isi file dan mengubahnya menjadi struktur data Python.
- `try` dan `except` digunakan untuk menangani kesalahan ketika file tidak ditemukan atau format JSON tidak valid.
- Program akan dihentikan apabila file utama tidak dapat dibaca.

Selanjutnya, program membaca file transaksi.

```python
try:
    with open(path_transaksi, "r", encoding="utf-8") as f:
        transaksi = json.load(f)
except FileNotFoundError:
    transaksi = []
except json.JSONDecodeError:
    print("Isi transaksi.json rusak!")
    exit()
```

Jika `transaksi.json` belum tersedia, program akan menggunakan data transaksi awal berupa list kosong. Jika file tersedia, seluruh riwayat transaksi akan dimuat.

### 7.4 Penyesuaian Data Lama

Bagian ini berfungsi menyesuaikan data JSON lama agar tetap sesuai dengan struktur program terbaru.

```python
for t in tenants:
    if "kategori" not in t:
        t["kategori"] = []
    if "induk" not in t and t.get("stok") is None:
        t["stok"] = MAX_STOK
    if "status" not in t:
        t["status"] = "Tersedia"
```

**Penjelasan:**

1. Memeriksa apakah data tenant sudah memiliki atribut kategori.
2. Memberikan stok maksimal kepada lapak induk lama yang belum memiliki nilai stok.
3. Memberikan status `Tersedia` apabila atribut status belum ada.

Program juga menghubungkan data tenant hasil sewa lama dengan lapak induknya berdasarkan kategori.

```python
for t in tenants:
    if "induk" not in t and t["status"] == "Disewa":
        for p in tenants:
            if p is not t and "induk" not in p and p["status"] != "Disewa" and p["kategori"] == t["kategori"]:
                t["induk"] = p["id"]
                break
```

Bagian tersebut mencari lapak induk yang memiliki kategori sama dengan tenant hasil sewa. Jika ditemukan, ID lapak induk dimasukkan ke atribut `induk`.

Selanjutnya, program mengambil informasi penyewa dari riwayat transaksi apabila data penyewa belum tersedia.

```python
for t in tenants:
    if "induk" in t and "penyewa" not in t:
        for trx in transaksi:
            if trx["tipe"] == "Reservasi" and trx["tenant_id"] == t["id"]:
                t["penyewa"] = trx["username"]
```

Terakhir, program memastikan setiap akun mempunyai atribut saldo.

```python
for nama_user in users:
    if "saldo" not in users[nama_user]:
        users[nama_user]["saldo"] = 0
```

### 7.5 Fungsi Pendukung Program

Bagian ini berisi fungsi umum yang digunakan oleh beberapa menu.

#### A. Fungsi `bersihkan_layar()`

```python
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")
```

Digunakan untuk membersihkan tampilan terminal. Perintah `cls` digunakan pada Windows, sedangkan `clear` digunakan pada sistem operasi selain Windows.

#### B. Fungsi `jeda()`

```python
def jeda():
    time.sleep(1.5)
```

Memberikan jeda selama 1,5 detik agar pesan yang ditampilkan dapat dibaca pengguna sebelum program melanjutkan proses.

#### C. Fungsi `rupiah(angka)`

```python
def rupiah(angka):
    return "Rp " + format(angka, ",").replace(",", ".")
```

Mengubah angka menjadi format mata uang Rupiah. Contohnya, angka `15000` akan ditampilkan menjadi `Rp 15.000`.

#### D. Fungsi `input_angka(pesan, minimal=0)`

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

Digunakan untuk menerima input berupa angka. Jika pengguna memasukkan huruf atau angka di bawah batas minimal, program akan meminta input kembali.

#### E. Fungsi `konfirmasi(pesan)`

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

Digunakan untuk meminta persetujuan pengguna sebelum melakukan tindakan tertentu. Jawaban `y` berarti setuju, sedangkan `n` berarti membatalkan.

#### F. Fungsi `simpan_data(nama_file, data)`

```python
def simpan_data(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
```

Berfungsi menyimpan data ke file JSON. Parameter `nama_file` menentukan lokasi file, sedangkan `data` merupakan informasi yang akan disimpan. `indent=4` membuat struktur JSON lebih mudah dibaca.

### 7.6 Fungsi Login dan Registrasi

#### A. Fungsi `login()`

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

Fungsi ini digunakan untuk memverifikasi username dan password pengguna. Password dimasukkan menggunakan `pwinput` agar tidak terlihat di terminal.

Pengguna diberikan maksimal tiga kali percobaan login. Jika berhasil, fungsi mengembalikan username. Jika seluruh percobaan gagal, fungsi mengembalikan string kosong.

#### B. Fungsi `registrasi()`

```python
def registrasi():
    print("\n=== REGISTRASI ===")
    try:
        username = input("Username : ").strip()
        password = pwinput.pwinput("Password : ")

        if username == "":
            print("Username tidak boleh kosong!")
            return
        if " " in username:
            print("Username tidak boleh mengandung spasi!")
            return
        if username in users:
            print("Username sudah dipakai!")
            return
        if password == "":
            print("Password tidak boleh kosong!")
            return
        users[username] = {"password": password, "role": "user", "saldo": 0}
        simpan_data(path_users, users)
        print("Registrasi berhasil! Silakan login.")
    except KeyboardInterrupt:
        print("\nProses registrasi dibatalkan (dilarang mengisi memakai Ctrl+C)")
```

Fungsi registrasi digunakan untuk membuat akun pengguna baru. Program melakukan beberapa validasi, yaitu username tidak boleh kosong, tidak boleh mengandung spasi, tidak boleh digunakan akun lain, dan password tidak boleh kosong.

Jika semua persyaratan terpenuhi, akun baru disimpan dengan role `user` dan saldo awal `0`.

### 7.7 Fungsi Pengelolaan Kategori dan Tenant

#### A. Fungsi `pilih_kategori()`

```python
def pilih_kategori():
    print("1. Makanan  2. Minuman  3. Fashion  4. Kerajinan  5. Lainnya")
    while True:
        nomor = input_angka("Pilih kategori (1-5) : ")
        if 1 <= nomor <= 5:
            return KATEGORI[nomor - 1]
        print("Nomor tidak ada.")
```

Menampilkan lima pilihan kategori tenant. Pengguna memilih kategori melalui nomor 1 sampai 5. Program mengembalikan nama kategori sesuai nomor yang dipilih.

#### B. Fungsi `format_kategori(kategori)`

```python
def format_kategori(kategori):
    if isinstance(kategori, list):
        return ", ".join(kategori) if kategori else "-"
    return kategori if kategori else "-"
```

Mengubah data kategori menjadi teks agar mudah ditampilkan. Jika kategori berbentuk list, elemen di dalamnya digabungkan menjadi satu teks.

#### C. Fungsi `buat_id_baru()`

```python
def buat_id_baru():
    id_baru = 1
    for tenant in tenants:
        if tenant["id"] >= id_baru:
            id_baru = tenant["id"] + 1
    return id_baru
```

Menghasilkan ID tenant baru berdasarkan ID terbesar yang sudah tersedia. Dengan demikian, setiap tenant memiliki ID yang berbeda.

#### D. Fungsi `nama_sudah_ada(nama)`

```python
def nama_sudah_ada(nama):
    for t in tenants:
        if t["nama"].lower() == nama.lower():
            return True
    return False
```

Memeriksa apakah nama tenant sudah digunakan. Perbandingan menggunakan `lower()` sehingga huruf besar dan kecil tidak dianggap berbeda.

#### E. Fungsi `perbarui_status(tenant)`

```python
def perbarui_status(tenant):
    if "induk" in tenant:
        tenant["status"] = "Disewa"
    elif tenant["stok"] is None or tenant["stok"] > 0:
        tenant["status"] = "Tersedia"
    else:
        tenant["status"] = "Penuh"
```

Menentukan status tenant berdasarkan jenis dan jumlah stok.

| Kondisi | Status |
|---|---|
| Tenant memiliki atribut `induk` | Disewa |
| Lapak induk memiliki stok lebih dari 0 | Tersedia |
| Lapak induk tidak memiliki batas stok (`None`) | Tersedia |
| Stok lapak induk habis | Penuh |

#### F. Fungsi `urutan_tampil(tenant)`

```python
def urutan_tampil(tenant):
    induk = tenant
    if "induk" in tenant:
        for t in tenants:
            if t["id"] == tenant["induk"]:
                induk = t
    kat = induk["kategori"][0] if induk["kategori"] else ""
    posisi = KATEGORI.index(kat) if kat in KATEGORI else len(KATEGORI)
    anak = 1 if "induk" in tenant else 0
    return (posisi, induk["id"], anak, tenant["id"])
```

Mengatur urutan tampilan tenant berdasarkan kategori, ID lapak induk, dan ID tenant. Tenant hasil sewa akan ditampilkan di bawah lapak induknya.

#### G. Fungsi `tampilkan_data()`

```python
def tampilkan_data():
    daftar = sorted(tenants, key=urutan_tampil)
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Tenant", "Kategori", "Harga Sewa", "Stok", "Status", "Penyewa"]
    no = 1
    for t in daftar:
        stok = t["stok"] if t["stok"] is not None else "-"
        tabel.add_row([no, t["nama"], format_kategori(t["kategori"]),
                    rupiah(t["harga"]), stok, t["status"], t.get("penyewa", "-")])
        no = no + 1
    print(tabel)
    return daftar
```

Menampilkan seluruh data tenant dalam bentuk tabel menggunakan `PrettyTable`. Data yang ditampilkan meliputi nomor, nama tenant, kategori, harga sewa, stok, status, dan penyewa.

#### H. Fungsi `pilih_tenant(daftar)`

```python
def pilih_tenant(daftar):
    nomor = input_angka("Masukkan No tenant : ", 1)
    if nomor > len(daftar):
        raise ValueError("Nomor tidak ditemukan!")
    return daftar[nomor - 1]
```

Memungkinkan pengguna memilih tenant berdasarkan nomor pada tabel. Jika nomor tidak ditemukan, program menghasilkan `ValueError`.

### 7.8 Fungsi Pengelolaan Data Tenant oleh Admin

#### A. Fungsi `tambah_data()`

```python
def tambah_data():
    print("\n=== TAMBAH DATA TENANT ===")
    nama = input("Nama Tenant : ").strip()
    if nama == "":
        print("Nama tidak boleh kosong!")
        return
    if nama_sudah_ada(nama):
        print("Tenant sudah ada!")
        return

    kategori = pilih_kategori()
    harga = input_angka("Harga sewa (Rp) : ", 1)

    tenant_baru = {"id": buat_id_baru(), "nama": nama, "kategori": [kategori],
                "harga": harga, "stok": MAX_STOK, "status": "Tersedia"}
    perbarui_status(tenant_baru)
    tenants.append(tenant_baru)
    simpan_data(path_tenants, tenants)
    print("Data tenant berhasil ditambahkan!")
```

Digunakan oleh admin untuk menambahkan lapak baru. Program meminta nama tenant, kategori, dan harga sewa. Nama diperiksa agar tidak kosong atau sama dengan tenant lain.

Tenant baru mendapatkan ID otomatis dan stok awal sebanyak 20 lapak. Setelah itu, data disimpan ke `tenant.json`.

#### B. Fungsi `ubah_data()`

```python
def ubah_data():
    print("\n=== UBAH DATA TENANT ===")
    daftar = tampilkan_data()
    try:
        tenant = pilih_tenant(daftar)
    except ValueError as e:
        print(e)
        return

    nama = input("Nama baru : ").strip()
    if nama == "":
        print("Nama tidak boleh kosong!")
        return
    if nama.lower() != tenant["nama"].lower() and nama_sudah_ada(nama):
        print("Nama tenant sudah dipakai!")
        return

    if "induk" in tenant:
        tenant["nama"] = nama
        simpan_data(path_tenants, tenants)
        print("Nama tenant berhasil diubah!")
        return

    kategori = pilih_kategori()
    harga = input_angka("Harga sewa baru (Rp) : ", 1)
    while True:
        stok = input_angka("Stok lapak baru (0-" + str(MAX_STOK) + ") : ", 0)
        if stok <= MAX_STOK:
            break
        print("Stok maksimal adalah", MAX_STOK, "lapak!")

    tenant["nama"] = nama
    tenant["kategori"] = [kategori]
    tenant["harga"] = harga
    tenant["stok"] = stok
    perbarui_status(tenant)
    simpan_data(path_tenants, tenants)
    print("Data tenant berhasil diubah!")
```

Digunakan untuk mengubah data tenant yang sudah tersimpan. Admin dapat mengubah nama, kategori, harga, dan stok lapak induk.

Khusus tenant hasil sewa, admin hanya dapat mengubah nama tenant. Hal ini dilakukan agar data penyewaan tetap terhubung dengan lapak induknya.

#### C. Fungsi `hapus_data()`

```python
def hapus_data():
    print("\n=== HAPUS DATA TENANT ===")
    daftar = tampilkan_data()
    try:
        tenant = pilih_tenant(daftar)
    except ValueError as e:
        print(e)
        return

    if "induk" not in tenant:
        print("Peringatan: tenant hasil sewa di bawah lapak ini ikut terhapus.")
    if not konfirmasi("Yakin ingin menghapus?"):
        print("Penghapusan dibatalkan.")
        return

    tenants.remove(tenant)
    if "induk" not in tenant:
        sisa = []
        for t in tenants:
            if t.get("induk") != tenant["id"]:
                sisa.append(t)
        tenants[:] = sisa
    simpan_data(path_tenants, tenants)
    print("Tenant", tenant["nama"], "berhasil dihapus!")
```

Digunakan untuk menghapus data tenant. Sebelum menghapus, program meminta konfirmasi kepada admin.

Jika yang dihapus adalah lapak induk, seluruh tenant hasil sewa yang terhubung dengan lapak tersebut juga akan dihapus. Jika yang dihapus hanya tenant hasil sewa, data lapak induk tetap dipertahankan.

### 7.9 Fungsi E-Money dan Transaksi

#### A. Fungsi `buat_kode()`

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

Menghasilkan kode transaksi dengan menggabungkan teks `TRX`, tanggal dan waktu, serta angka acak tiga digit. Program memeriksa kode tersebut agar tidak sama dengan kode transaksi yang sudah tersimpan.

#### B. Fungsi `catat_transaksi()`

```python
def catat_transaksi(username, tipe, tenant, jumlah, qty, saldo_akhir, nama_usaha="-", kategori="-"):
    trx = {
        "kode": buat_kode(),
        "waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "username": username,
        "tipe": tipe,
        "tenant_id": tenant["id"] if tenant else 0,
        "tenant_nama": tenant["nama"] if tenant else "-",
        "nama_usaha": nama_usaha,
        "kategori": kategori,
        "qty": qty,
        "jumlah": jumlah,
        "saldo_akhir": saldo_akhir
    }
    transaksi.append(trx)
    simpan_data(path_transaksi, transaksi)
    return trx
```

Digunakan untuk mencatat setiap transaksi yang dilakukan oleh pengguna atau admin. Informasi yang disimpan meliputi kode transaksi, waktu, username, jenis transaksi, ID tenant, nama tenant, nama usaha, kategori, jumlah lapak, nominal transaksi, dan saldo akhir.

Jika transaksi bukan reservasi, informasi tenant akan diisi dengan nilai default.

#### C. Fungsi `top_up(username)`

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
    if not konfirmasi("Lanjutkan top up " + rupiah(nominal) + "?"):
        print("Top up dibatalkan.")
        return

    users[username]["saldo"] = users[username]["saldo"] + nominal
    simpan_data(path_users, users)
    trx = catat_transaksi(username, "Top Up", None, nominal, 1, users[username]["saldo"])
    print("Top up berhasil! Saldo sekarang :", rupiah(users[username]["saldo"]))
    print("Kode transaksi :", trx["kode"])
```

Digunakan oleh user untuk menambahkan saldo e-money. Program memeriksa nominal minimal dan maksimal, kemudian meminta konfirmasi sebelum menambahkan saldo.

Setelah saldo berhasil ditambahkan, perubahan disimpan ke `users.json` dan transaksi dicatat ke `transaksi.json`.

#### D. Fungsi `tambah_saldo_user()`

```python
def tambah_saldo_user():
    print("\n=== TAMBAH SALDO USER ===")
    tabel = PrettyTable()
    tabel.field_names = ["Username", "Saldo"]
    for nama in users:
        if users[nama]["role"] == "user":
            tabel.add_row([nama, rupiah(users[nama]["saldo"])])
    print(tabel)

    target = input("Username tujuan : ").strip()
    if target not in users or users[target]["role"] != "user":
        print("User tidak ditemukan!")
        return

    print("Minimal", rupiah(MIN_TOPUP), "- maksimal", rupiah(MAX_TOPUP))
    nominal = input_angka("Nominal saldo (Rp) : ")
    if nominal < MIN_TOPUP:
        print("Minimal", rupiah(MIN_TOPUP), "!")
        return
    if nominal > MAX_TOPUP:
        print("Maksimal", rupiah(MAX_TOPUP), "per transaksi!")
        return
    if not konfirmasi("Tambah " + rupiah(nominal) + " ke saldo " + target + "?"):
        print("Dibatalkan.")
        return

    users[target]["saldo"] = users[target]["saldo"] + nominal
    simpan_data(path_users, users)
    trx = catat_transaksi(target, "Top Up Admin", None, nominal, 1, users[target]["saldo"])
    print("Berhasil! Saldo", target, "sekarang :", rupiah(users[target]["saldo"]))
    print("Kode transaksi :", trx["kode"])
```

Digunakan admin untuk menambahkan saldo ke akun user tertentu. Program menampilkan daftar pengguna beserta saldo, memvalidasi username tujuan dan nominal, lalu meminta konfirmasi.

Transaksi dicatat dengan tipe `Top Up Admin` agar dapat dibedakan dari top up yang dilakukan langsung oleh user.

### 7.10 Fungsi Reservasi dan Pembayaran

#### Fungsi `reservasi_tenant(username)`

```python
def reservasi_tenant(username):
    print("\n=== RESERVASI & PEMBAYARAN TENANT ===")
    daftar = tampilkan_data()
    print("Saldo Anda :", rupiah(users[username]["saldo"]))
    try:
        lapak = pilih_tenant(daftar)
    except ValueError as e:
        print(e)
        return
```

Bagian awal fungsi menampilkan daftar tenant, saldo pengguna, dan meminta pengguna memilih lapak yang ingin disewa.

Program kemudian memeriksa apakah lapak dapat dipesan.

```python
if "induk" in lapak or lapak["stok"] is None or lapak["stok"] <= 0:
    print("Lapak ini tidak bisa dipesan (sudah disewa / stok habis)!")
    return
```

Lapak hasil sewa tidak dapat dipesan kembali. Lapak induk juga tidak dapat dipesan jika stoknya habis atau tidak memiliki stok yang dapat digunakan.

Selanjutnya, program meminta jumlah lapak dan nama usaha penyewa.

```python
while True:
    qty = input_angka("Jumlah lapak yang diinginkan (1-" + str(lapak["stok"]) + ") : ", 1)
    if qty <= lapak["stok"]:
        break
    print("Stok tersisa hanya", lapak["stok"], "lapak!")

while True:
    nama_baru = input("Nama tenant Anda : ").strip()
    if nama_baru == "":
        print("Nama tenant tidak boleh kosong!")
        continue
    if nama_sudah_ada(nama_baru):
        print("Nama tenant sudah dipakai!")
        continue
    break
```

Jumlah lapak harus lebih dari nol dan tidak boleh melebihi stok yang tersedia. Nama usaha juga harus diisi dan tidak boleh sama dengan nama tenant yang sudah ada.

Program menghitung total biaya sewa.

```python
total = lapak["harga"] * qty
```

Jika saldo pengguna tidak mencukupi, reservasi dibatalkan dan pengguna diminta melakukan top up terlebih dahulu.

```python
if users[username]["saldo"] < total:
    kurang = total - users[username]["saldo"]
    print("Saldo tidak cukup! Kurang", rupiah(kurang), "- silakan top up dulu.")
    return
```

Jika saldo mencukupi dan pengguna menyetujui pembayaran, stok lapak induk dikurangi sesuai jumlah yang dipesan.

```python
lapak["stok"] -= qty
perbarui_status(lapak)
```

Program kemudian membuat data tenant baru yang terhubung dengan lapak induk melalui atribut `induk`.

```python
tenant_baru = {
    "id": buat_id_baru(),
    "nama": nama_baru,
    "kategori": list(kategori),
    "harga": lapak["harga"],
    "stok": qty,
    "status": "Disewa",
    "induk": lapak["id"],
    "penyewa": username
}
tenants.append(tenant_baru)
```

Setelah data tenant dibuat, saldo pengguna dikurangi dan seluruh perubahan disimpan.

```python
users[username]["saldo"] -= total
simpan_data(path_users, users)
simpan_data(path_tenants, tenants)
```

Terakhir, program mencatat transaksi dan mencetak invoice.

```python
trx = catat_transaksi(username, "Reservasi", tenant_baru, total, qty,
                    users[username]["saldo"], nama_baru, format_kategori(kategori))
print("\nPembayaran berhasil!\n")
cetak_invoice(trx)
```

**Kesimpulan fungsi:** `reservasi_tenant()` mengatur seluruh proses penyewaan, mulai dari pemilihan lapak, validasi stok, pengisian nama usaha, perhitungan biaya, pengecekan saldo, pengurangan stok, penyimpanan data, pencatatan transaksi, hingga pencetakan invoice.

### 7.11 Fungsi Invoice dan Riwayat Transaksi

#### A. Fungsi `cetak_invoice(trx)`

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
        "Nama Usaha     : " + trx.get("nama_usaha", "-"),
        "Kategori       : " + trx.get("kategori", "-"),
        "Jumlah Lapak   : " + str(trx["qty"]),
        "Total Bayar    : " + rupiah(trx["jumlah"]),
        "Sisa Saldo     : " + rupiah(trx["saldo_akhir"]),
        garis,
        "   Terima kasih telah melakukan reservasi",
        garis
    ]
```

Fungsi ini menyusun informasi transaksi menjadi invoice yang berisi kode transaksi, waktu, pelanggan, tenant, nama usaha, kategori, jumlah lapak, total pembayaran, dan saldo akhir.

Invoice ditampilkan di terminal dan disimpan sebagai file `.txt`.

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

`os.makedirs()` membuat folder invoice apabila belum tersedia. Nama file menggunakan kode transaksi sehingga setiap invoice memiliki nama yang berbeda.

#### B. Fungsi `tampilkan_riwayat(username, semua)`

```python
def tampilkan_riwayat(username, semua):
    tabel = PrettyTable()
    tabel.field_names = ["Kode", "Waktu", "User", "Tipe", "Tenant", "Nama Usaha", "Qty", "Jumlah", "Saldo Akhir"]
    ada = False
    for t in transaksi:
        if semua or t["username"] == username:
            tabel.add_row([t["kode"], t["waktu"], t["username"], t["tipe"], t["tenant_nama"],
                        t.get("nama_usaha", "-"), t["qty"], rupiah(t["jumlah"]), rupiah(t["saldo_akhir"])])
            ada = True
    if ada:
        print(tabel)
    else:
        print("Belum ada riwayat transaksi.")
    return ada
```

Digunakan untuk menampilkan riwayat transaksi dalam bentuk tabel.

Parameter `username` menentukan akun yang sedang mengakses menu, sedangkan parameter `semua` menentukan cakupan data:

- `semua=True`: admin dapat melihat seluruh riwayat transaksi.
- `semua=False`: user hanya dapat melihat transaksi miliknya sendiri.

Fungsi mengembalikan nilai `True` jika terdapat transaksi dan `False` jika belum ada transaksi.

#### C. Fungsi `cetak_ulang_invoice(username, semua)`

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

Digunakan untuk mencetak ulang invoice berdasarkan kode transaksi.

Program hanya mengizinkan pencetakan invoice untuk transaksi bertipe `Reservasi`. Transaksi top up tidak memiliki invoice reservasi.

Admin dapat mencetak ulang invoice dari seluruh transaksi reservasi, sedangkan user hanya dapat mencetak invoice miliknya sendiri.

#### D. Fungsi `riwayat_dan_invoice(username, semua)`

```python
def riwayat_dan_invoice(username, semua):
    print("\n=== RIWAYAT TRANSAKSI ===")
    ada = tampilkan_riwayat(username, semua)
    if ada and konfirmasi("\nCetak ulang invoice?"):
        cetak_ulang_invoice(username, semua)
```

Menggabungkan tampilan riwayat transaksi dan fitur cetak ulang invoice dalam satu menu. Setelah riwayat ditampilkan, program menawarkan pilihan untuk mencetak ulang invoice apabila terdapat transaksi.

### 7.12 Fungsi Laporan Admin

#### Fungsi `laporan_admin()`

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

Fungsi ini digunakan untuk membuat laporan ringkas bagi admin. Program membaca seluruh data transaksi, tetapi hanya menghitung transaksi dengan tipe `Reservasi`.

Informasi yang dihitung meliputi:

1. Total pendapatan dari seluruh reservasi.
2. Jumlah transaksi reservasi.
3. Jumlah lapak yang dipesan untuk setiap tenant.
4. Tenant dengan jumlah lapak yang paling banyak dipesan.

Bagian berikut menampilkan hasil perhitungan.

```python
print("Total pendapatan  :", rupiah(total_pendapatan))
print("Jumlah transaksi  :", jumlah_transaksi, "(reservasi)")
```

Jika belum terdapat transaksi reservasi, program menampilkan informasi bahwa data tenant terlaris belum tersedia.

Selanjutnya, program mencari tenant dengan jumlah lapak dipesan terbanyak dan menampilkannya dalam tabel menggunakan `PrettyTable`.

### 7.13 Menu Admin

#### Fungsi `menu_admin(username)`

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
            print("5. Riwayat transaksi & cetak ulang invoice")
            print("6. Laporan ringkas")
            print("7. Tambah saldo user")
            print("8. Logout")
            pilihan = input("Pilih menu: ")
```

Fungsi ini menampilkan menu khusus admin setelah proses login berhasil. Admin memiliki delapan pilihan menu.

| Pilihan | Menu | Fungsi |
|---|---|---|
| 1 | Tambah data tenant | Menambahkan lapak baru. |
| 2 | Tampilkan data tenant | Melihat seluruh data tenant. |
| 3 | Ubah data tenant | Mengubah informasi tenant. |
| 4 | Hapus data tenant | Menghapus tenant dari sistem. |
| 5 | Riwayat transaksi & cetak ulang invoice | Melihat seluruh transaksi dan mencetak ulang invoice reservasi. |
| 6 | Laporan ringkas | Melihat pendapatan dan tenant terlaris. |
| 7 | Tambah saldo user | Menambahkan saldo ke akun pengguna. |
| 8 | Logout | Keluar dari akun admin. |

Pemilihan menu diproses menggunakan percabangan `if`, `elif`, dan `else`. Setiap pilihan akan memanggil fungsi yang sesuai.

### 7.14 Menu User

#### Fungsi `menu_user(username)`

```python
def menu_user(username):
    try:
        while True:
            bersihkan_layar()
            print("\n=== MENU USER -", username, "===")
            print("1. Tampilkan data tenant")
            print("2. Top up saldo")
            print("3. Reservasi & bayar tenant")
            print("4. Riwayat transaksi & cetak ulang invoice")
            print("5. Logout")
            pilihan = input("Pilih menu: ")
```

Fungsi ini menampilkan menu khusus user setelah login berhasil.

| Pilihan | Menu | Fungsi |
|---|---|---|
| 1 | Tampilkan data tenant | Melihat daftar lapak dan stok yang tersedia. |
| 2 | Top up saldo | Mengisi saldo e-money. |
| 3 | Reservasi & bayar tenant | Memesan lapak dan melakukan pembayaran. |
| 4 | Riwayat transaksi & cetak ulang invoice | Melihat transaksi pribadi dan mencetak ulang invoice reservasi. |
| 5 | Logout | Keluar dari akun user. |

Setiap pilihan menu akan memanggil fungsi yang sesuai. User hanya dapat mengakses data dan transaksi miliknya sendiri melalui menu yang disediakan.

### 7.15 Program Utama

#### Fungsi `main()`

```python
def main():
    try:
        while True:
            bersihkan_layar()
            print("\n=== SISTEM RESERVASI TENANT BAZAR ===")
            print("1. Login")
            print("2. Registrasi")
            print("3. Keluar")
            pilihan = input("Pilih menu: ")
```

Fungsi `main()` merupakan bagian utama yang menjalankan seluruh sistem. Program menampilkan tiga pilihan menu, yaitu login, registrasi, dan keluar.

Jika pengguna memilih login, program memanggil fungsi `login()` untuk memeriksa akun.

```python
if pilihan == "1":
    username = login()
    if username == "":
        print("Login gagal 3 kali. Program berhenti.")
        break
    if users[username]["role"] == "admin":
        menu_admin(username)
    else:
        menu_user(username)
```

Setelah login berhasil, program memeriksa atribut `role` pada akun pengguna.

- Jika role bernilai `admin`, program menjalankan `menu_admin()`.
- Jika role bukan admin, program menjalankan `menu_user()`.

Jika pengguna memilih registrasi, program memanggil fungsi `registrasi()` untuk membuat akun baru. Jika memilih keluar, program menghentikan perulangan dan menampilkan pesan terima kasih.

Bagian terakhir merupakan perintah untuk menjalankan program utama.

```python
main()
```

Dengan pemanggilan tersebut, seluruh proses program dimulai dari menu utama hingga pengguna keluar dari sistem.

## 8. Struktur Data JSON

Program menggunakan tiga file JSON sebagai tempat penyimpanan data utama.

### 8.1 File `users.json`

File ini menyimpan informasi akun pengguna.

Contoh:

```json
{
    "admin": {
        "password": "admin123",
        "role": "admin",
        "saldo": 0
    },
    "budi": {
        "password": "rahasia123",
        "role": "user",
        "saldo": 50000
    }
}
```

**Keterangan atribut:**

| Atribut | Fungsi |
|---|---|
| `password` | Menyimpan password akun. |
| `role` | Menentukan jenis akun, yaitu admin atau user. |
| `saldo` | Menyimpan saldo e-money pengguna. |

### 8.2 File `tenant.json`

File ini menyimpan data lapak induk dan tenant hasil reservasi.

Contoh lapak induk:

```json
[
    {
        "id": 1,
        "nama": "Tenant Makanan A",
        "kategori": [
            "Makanan"
        ],
        "harga": 50000,
        "stok": 20,
        "status": "Tersedia"
    }
]
```

Contoh tenant hasil reservasi:

```json
[
    {
        "id": 2,
        "nama": "Warung Budi",
        "kategori": [
            "Makanan"
        ],
        "harga": 50000,
        "stok": 2,
        "status": "Disewa",
        "induk": 1,
        "penyewa": "budi"
    }
]
```

**Keterangan atribut:**

| Atribut | Fungsi |
|---|---|
| `id` | ID unik setiap tenant. |
| `nama` | Nama tenant atau nama usaha penyewa. |
| `kategori` | Kategori tenant. |
| `harga` | Harga sewa lapak. |
| `stok` | Jumlah lapak yang tersedia atau jumlah lapak yang dipesan. |
| `status` | Status tenant, seperti Tersedia, Disewa, atau Penuh. |
| `induk` | ID lapak induk yang menjadi sumber reservasi. |
| `penyewa` | Username pengguna yang melakukan reservasi. |

Atribut `induk` dan `penyewa` digunakan pada data tenant hasil reservasi.

### 8.3 File `transaksi.json`

File ini menyimpan seluruh aktivitas transaksi.

Contoh:

```json
[
    {
        "kode": "TRX-261103201530-482",
        "waktu": "03-11-2026 20:15:30",
        "username": "budi",
        "tipe": "Reservasi",
        "tenant_id": 2,
        "tenant_nama": "Warung Budi",
        "nama_usaha": "Warung Budi",
        "kategori": "Makanan",
        "qty": 2,
        "jumlah": 100000,
        "saldo_akhir": 50000
    }
]
```

**Keterangan atribut:**

| Atribut | Fungsi |
|---|---|
| `kode` | Kode unik transaksi. |
| `waktu` | Tanggal dan waktu transaksi. |
| `username` | Akun yang melakukan transaksi. |
| `tipe` | Jenis transaksi, misalnya Reservasi, Top Up, atau Top Up Admin. |
| `tenant_id` | ID tenant yang berkaitan dengan transaksi. |
| `tenant_nama` | Nama tenant. |
| `nama_usaha` | Nama usaha yang digunakan penyewa. |
| `kategori` | Kategori tenant. |
| `qty` | Jumlah lapak dalam transaksi. |
| `jumlah` | Nominal transaksi. |
| `saldo_akhir` | Saldo setelah transaksi. |

## 9. Aturan dan Validasi Sistem

Program menerapkan beberapa aturan untuk menjaga proses pengelolaan tenant dan transaksi.

| No. | Aturan | Keterangan |
|---|---|---|
| 1 | Login maksimal tiga kali | Pengguna yang gagal login tiga kali akan menghentikan proses program. |
| 2 | Username unik | Username tidak boleh kosong, mengandung spasi, atau sama dengan akun lain. |
| 3 | Nama tenant unik | Nama tenant tidak boleh kosong atau sama dengan nama tenant yang sudah tersimpan. |
| 4 | Harga sewa | Harga sewa harus lebih besar dari nol. |
| 5 | Stok maksimal | Stok lapak induk maksimal 20. |
| 6 | Stok reservasi | Jumlah lapak yang dipesan tidak boleh melebihi stok tersedia. |
| 7 | Top up minimal | Minimal pengisian saldo Rp10.000. |
| 8 | Top up maksimal | Maksimal pengisian saldo Rp10.000.000 per transaksi. |
| 9 | Pembayaran | Reservasi hanya dapat dilakukan jika saldo mencukupi. |
| 10 | Konfirmasi | Top up dan reservasi memerlukan konfirmasi sebelum diproses. |
| 11 | Riwayat transaksi | User hanya dapat melihat riwayat miliknya sendiri. |
| 12 | Invoice | Invoice hanya tersedia untuk transaksi reservasi. |

## 10. Alur Kerja Sistem

Secara umum, alur kerja program dapat dijelaskan sebagai berikut:

```text
                 MULAI
                   |
                   v
          Memuat Data JSON
                   |
                   v
             Menu Utama
                   |
          +--------+--------+
          |        |        |
          v        v        v
         Login  Registrasi Keluar
          |
          v
    Validasi Akun
          |
     +----+----+
     |         |
     v         v
   Admin      User
     |         |
     v         v
 Menu Admin  Menu User
     |         |
     v         v
 Kelola Data  Top Up Saldo
 Tenant       Reservasi
 Laporan      Pembayaran
 Transaksi    Riwayat
     |         |
     +----+----+
          |
          v
    Simpan Data JSON
          |
          v
        Selesai
```

**Penjelasan alur:**

1. Program dimulai dengan membaca data akun, tenant, dan transaksi.
2. Pengguna memilih login, registrasi, atau keluar.
3. Jika login berhasil, sistem memeriksa role akun.
4. Admin diarahkan ke menu pengelolaan tenant dan laporan.
5. User diarahkan ke menu penyewaan dan pembayaran.
6. Setiap perubahan data dan transaksi disimpan ke file JSON.
7. Setelah pengguna logout atau memilih keluar, proses program berakhir.



## 11. 📋 Daftar Fitur per Role

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

## 12. 📸 Screenshot Output & Penjelasan

> 📝 **Petunjuk untuk tim:** Jalankan program, ambil screenshot setiap tampilan, kemudian simpan di folder `docs/screenshots/` menggunakan nama file seperti di bawah. Pastikan file gambar sudah diunggah ke repositori GitHub agar dapat ditampilkan. Hapus petunjuk ini setelah semua screenshot terpasang.

### 12.1 Menu Utama

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 22 48 38" src="https://github.com/user-attachments/assets/addc63a5-81c7-4ae8-a546-47218ebbd11f" />

**Penjelasan:**

Tampilan awal program dengan tiga pilihan, yaitu Login, Registrasi, dan Keluar. Input selain angka 1 sampai 3 akan menampilkan pesan "Pilihan tidak valid".

### 12.2 Registrasi

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 23 04 43" src="https://github.com/user-attachments/assets/2b8b9062-78ca-4390-a008-336abe8432fb" />

**Penjelasan:**

User mengisi username dan password. Program memeriksa apakah username kosong, mengandung spasi, atau sudah digunakan. Jika valid, akun disimpan ke `users.json` dengan role `user` dan saldo Rp0.

### 12.3 Login

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 23 10 29" src="https://github.com/user-attachments/assets/32361b11-2b2f-411b-b98b-9ebb3088cae2" />

**Penjelasan:**

User memasukkan username dan password. Password disamarkan saat diketik. Jika salah, program menampilkan sisa percobaan. Setelah 3 kali gagal, pengguna kembali ke menu utama.

### 12.4 Menu Admin

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/4e0ba913-1f08-488e-b350-eb8bd76f9f91" />

**Penjelasan:**

Admin memiliki 8 menu untuk mengelola tenant, melihat riwayat transaksi, mencetak ulang invoice, melihat laporan ringkas, menambah saldo user, dan logout.

### 12.5 Tampilkan Data Tenant

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 22 41 21" src="https://github.com/user-attachments/assets/d62bf2ed-2c57-4eae-af8c-8215257af411" />

**Penjelasan:**

Data tampil dalam tabel dengan kolom No, Nama Tenant, Kategori, Harga Sewa, Stok, Status, dan Penyewa. Lapak induk berstatus `Tersedia` atau `Penuh`, sedangkan tenant hasil sewa berstatus `Disewa` dan tampil di bawah lapak induknya.

### 12.6 Tambah Data Tenant

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 22 40 46" src="https://github.com/user-attachments/assets/7e9e038c-58e1-407b-8c64-2af28de3e7c6" />

**Penjelasan:**

Admin mengisi nama tenant, memilih kategori 1 sampai 5, dan menentukan harga sewa. Nama yang kosong atau sudah digunakan akan ditolak. Lapak baru otomatis memiliki stok 20.

### 12.7 Ubah Data Tenant

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 23 18 38" src="https://github.com/user-attachments/assets/3f26582c-769a-463e-9605-6b1d46bebec4" />

**Penjelasan:**

Admin memilih tenant berdasarkan nomor di tabel, kemudian mengubah data tenant. Stok tidak boleh melebihi 20.

### 12.8 Hapus Data Tenant

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 23 19 36" src="https://github.com/user-attachments/assets/abe097ff-60fd-4c79-bf22-30b5b61b75b3" />

**Penjelasan:**

Program meminta konfirmasi `y/n` sebelum menghapus tenant. Jika yang dihapus adalah lapak induk, tenant hasil sewanya juga ikut terhapus dan peringatan ditampilkan terlebih dahulu.

### 12.9 Laporan Ringkas

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 23 20 47" src="https://github.com/user-attachments/assets/bef58e65-a5a8-4fda-b191-2e6baf21d660" />

**Penjelasan:**

Laporan menampilkan total pendapatan, jumlah transaksi reservasi, tenant terlaris, dan tabel jumlah lapak yang dipesan per tenant.

### 12.10 Tambah Saldo User (Admin)

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 22 37 02 (2)" src="https://github.com/user-attachments/assets/a90d71a6-4cf9-44f3-b36f-7942a1382a7a" />

**Penjelasan:**

Admin melihat daftar user beserta saldonya, memilih username tujuan, lalu mengisi nominal saldo. Transaksi dicatat dengan tipe `Top Up Admin`.

### 12.11 Menu User

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 22 36 56" src="https://github.com/user-attachments/assets/c1bb0372-04f9-48e4-bfd6-1e868f97ae06" />

**Penjelasan:**

User memiliki 5 menu, yaitu tampilkan tenant, top up saldo, reservasi, riwayat transaksi, dan logout.

### 12.12 Top Up Saldo

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 22 36 57 (1)" src="https://github.com/user-attachments/assets/17ce7212-a893-4965-b631-24799d6ec5a1" />

**Penjelasan:**

Program menampilkan saldo saat ini serta batas minimal dan maksimal top up. Nominal di luar batas akan ditolak. Setelah dikonfirmasi, saldo bertambah dan kode transaksi ditampilkan.

### 12.13 Reservasi & Pembayaran

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 22 36 57 (2)" src="https://github.com/user-attachments/assets/7bc04bfc-d211-47a6-ac65-696e4af5a1aa" />

**Penjelasan:**

User memilih lapak, menentukan jumlah, dan memasukkan nama tenant. Program menampilkan ringkasan serta total pembayaran. Jika saldo kurang, program menampilkan selisih kekurangannya. Jika saldo cukup dan pembayaran dikonfirmasi, stok berkurang dan saldo terpotong.

### 12.14 Invoice

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 22 36 58" src="https://github.com/user-attachments/assets/9242d055-af7e-48c8-b110-bb32998683d5" />
<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 22 36 59" src="https://github.com/user-attachments/assets/5dcae8a4-0005-48c7-8fd6-566557e2a924" />


**Penjelasan:**

Setelah pembayaran reservasi berhasil, invoice ditampilkan di layar dan disimpan sebagai file `.txt` di folder `invoice`. Invoice berisi kode transaksi, waktu, pelanggan, tenant, kategori, jumlah lapak, total bayar, dan sisa saldo.

### 6.15 Riwayat Transaksi

<img width="1366" height="768" alt="WhatsApp Image 2026-11-03 at 23 24 49" src="https://github.com/user-attachments/assets/0b31247a-2218-451d-9368-d229196182eb" />

**Penjelasan:**

Tabel berisi kode, waktu, user, tipe transaksi, tenant, nama usaha, qty, jumlah, dan saldo akhir. User hanya melihat transaksinya sendiri, sedangkan admin dapat melihat semua transaksi. Invoice reservasi dapat dicetak ulang menggunakan kode transaksi.

---


<div align="center">

**Dibuat oleh Tim APASrah**

*Sistem Reservasi Tenant Bazar*

</div>
