import os
import time
import json
import random
from datetime import datetime
from prettytable import PrettyTable
import pwinput

folder_data = r"C:\ApasProjek"
path_users = folder_data + r"\users.json"
path_tenants = folder_data + r"\tenant.json"
path_transaksi = folder_data + r"\transaksi.json"
folder_invoice = folder_data + r"\invoice"

KATEGORI = ("Makanan", "Minuman", "Fashion", "Kerajinan", "Lainnya")
MAX_STOK = 20
MIN_TOPUP = 10000
MAX_TOPUP = 10000000

# Membaca data dari file JSON
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

# transaksi.json dibuat otomatis kalau belum ada
try:
    with open(path_transaksi, "r", encoding="utf-8") as f:
        transaksi = json.load(f)
except FileNotFoundError:
    transaksi = []
except json.JSONDecodeError:
    print("Isi transaksi.json rusak!")
    exit()

# Menyesuaikan data lama:
# lapak induk tanpa stok dianggap punya kuota penuh (MAX_STOK)
for t in tenants:
    if "kategori" not in t:
        t["kategori"] = []
    if "induk" not in t and t.get("stok") is None:
        t["stok"] = MAX_STOK
    if "status" not in t:
        t["status"] = "Tersedia"

# data lama: baris hasil sewa (status Disewa, belum punya "induk")
# dihubungkan ke lapak induk yang kategorinya sama, supaya tidak dianggap lapak biasa
for t in tenants:
    if "induk" not in t and t["status"] == "Disewa":
        for p in tenants:
            if p is not t and "induk" not in p and p["status"] != "Disewa" and p["kategori"] == t["kategori"]:
                t["induk"] = p["id"]
                break

# data lama: isi penyewa dari riwayat transaksi
for t in tenants:
    if "induk" in t and "penyewa" not in t:
        for trx in transaksi:
            if trx["tipe"] == "Reservasi" and trx["tenant_id"] == t["id"]:
                t["penyewa"] = trx["username"]

for nama_user in users:
    if "saldo" not in users[nama_user]:
        users[nama_user]["saldo"] = 0

# membersihkan layar
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

# jeda supaya pesan sempat terbaca
def jeda():
    time.sleep(1.5)

# format rupiah, contoh 15000 -> Rp 15.000
def rupiah(angka):
    return "Rp " + format(angka, ",").replace(",", ".")

# meminta input angka, diulang sampai benar (tidak boleh di bawah minimal)
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

# konfirmasi y/n, diulang sampai jawaban benar
def konfirmasi(pesan):
    while True:
        jawab = input(pesan + " (y/n) : ").lower()
        if jawab == "y":
            return True
        if jawab == "n":
            return False
        print("Jawab dengan y atau n saja!")

# menyimpan data ke file JSON
def simpan_data(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# membuat kode transaksi unik, contoh TRX-261025153200-482
def buat_kode():
    while True:
        kode = "TRX-" + datetime.now().strftime("%y%m%d%H%M%S") + "-" + str(random.randint(100, 999))
        ada = False
        for t in transaksi:
            if t["kode"] == kode:
                ada = True
        if not ada:
            return kode

# mencatat transaksi baru dan menyimpannya
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

# Login (maksimal 3 kali percobaan)
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

# Registrasi (validasi format minimal akun)
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

# memilih kategori lewat nomor menu
def pilih_kategori():
    print("1. Makanan  2. Minuman  3. Fashion  4. Kerajinan  5. Lainnya")
    while True:
        nomor = input_angka("Pilih kategori (1-5) : ")
        if 1 <= nomor <= 5:
            return KATEGORI[nomor - 1]
        print("Nomor tidak ada.")

# mengubah kategori (list atau teks lama) jadi teks untuk ditampilkan
def format_kategori(kategori):
    if isinstance(kategori, list):
        return ", ".join(kategori) if kategori else "-"
    return kategori if kategori else "-"

# membuat ID baru (paling besar + 1), ID dipakai internal di JSON
def buat_id_baru():
    id_baru = 1
    for tenant in tenants:
        if tenant["id"] >= id_baru:
            id_baru = tenant["id"] + 1
    return id_baru

# cek apakah nama tenant sudah dipakai
def nama_sudah_ada(nama):
    for t in tenants:
        if t["nama"].lower() == nama.lower():
            return True
    return False

# status lapak induk mengikuti stok, tenant hasil sewa selalu "Disewa"
def perbarui_status(tenant):
    if "induk" in tenant:
        tenant["status"] = "Disewa"
    elif tenant["stok"] is None or tenant["stok"] > 0:
        tenant["status"] = "Tersedia"
    else:
        tenant["status"] = "Penuh"

# urutan tampil: per kategori, lapak induk dulu lalu tenant hasil sewanya di bawahnya
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

# menampilkan data dengan nomor urut, mengembalikan daftar yang sudah terurut
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

# memilih tenant dari nomor yang tampil di tabel
# kalau nomor tidak ada, program melempar error (raise)
def pilih_tenant(daftar):
    nomor = input_angka("Masukkan No tenant : ", 1)
    if nomor > len(daftar):
        raise ValueError("Nomor tidak ditemukan!")
    return daftar[nomor - 1]

# menambah data (admin menambah lapak per kategori)
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

    # lapak baru langsung punya kuota penuh
    tenant_baru = {"id": buat_id_baru(), "nama": nama, "kategori": [kategori],
                "harga": harga, "stok": MAX_STOK, "status": "Tersedia"}
    perbarui_status(tenant_baru)
    tenants.append(tenant_baru)
    simpan_data(path_tenants, tenants)
    print("Data tenant berhasil ditambahkan!")

# mengubah data
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

    # tenant hasil sewa hanya boleh diubah namanya
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

# menghapus data (dengan konfirmasi y/n)
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

# ================= E-MONEY & TRANSAKSI =================
# top up saldo
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

# admin menambah saldo user
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

# mencetak invoice ke layar dan menyimpannya sebagai file .txt
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
    for b in baris:
        print(b)

    try:
        os.makedirs(folder_invoice, exist_ok=True)
        nama_file = folder_invoice + "\\" + trx["kode"] + ".txt"
        with open(nama_file, "w", encoding="utf-8") as f:
            f.write("\n".join(baris))
        print("Invoice tersimpan di :", nama_file)
    except OSError:
        print("Invoice gagal disimpan ke file, tetapi transaksi tetap tercatat.")

# reservasi: stok lapak induk berkurang, tenant baru muncul di bawah lapak asalnya
def reservasi_tenant(username):
    print("\n=== RESERVASI & PEMBAYARAN TENANT ===")
    daftar = tampilkan_data()
    print("Saldo Anda :", rupiah(users[username]["saldo"]))
    try:
        lapak = pilih_tenant(daftar)
    except ValueError as e:
        print(e)
        return

    if "induk" in lapak or lapak["stok"] is None or lapak["stok"] <= 0:
        print("Lapak ini tidak bisa dipesan (sudah disewa / stok habis)!")
        return

    kategori = lapak["kategori"]
    print("Kategori lapak :", format_kategori(kategori))

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

    total = lapak["harga"] * qty
    print("Penyewa     :", username)
    print("Nama tenant :", nama_baru)
    print("Kategori    :", format_kategori(kategori))
    print("Stok lapak  :", qty)
    print("Total bayar :", rupiah(total))

    if users[username]["saldo"] < total:
        kurang = total - users[username]["saldo"]
        print("Saldo tidak cukup! Kurang", rupiah(kurang), "- silakan top up dulu.")
        return

    if not konfirmasi("Bayar " + rupiah(total) + " dengan saldo?"):
        print("Pembayaran dibatalkan.")
        return

    # kurangi stok lapak induk
    lapak["stok"] -= qty
    perbarui_status(lapak)

    # baris baru hasil sewa, ditandai dengan field "induk"
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

    users[username]["saldo"] -= total
    simpan_data(path_users, users)
    simpan_data(path_tenants, tenants)

    trx = catat_transaksi(username, "Reservasi", tenant_baru, total, qty,
                        users[username]["saldo"], nama_baru, format_kategori(kategori))
    print("\nPembayaran berhasil!\n")
    cetak_invoice(trx)

# tabel riwayat transaksi; semua=True untuk admin, False untuk user tertentu
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

# cetak ulang invoice berdasarkan kode (hanya milik sendiri untuk user)
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

# riwayat + cetak ulang invoice digabung jadi satu menu
def riwayat_dan_invoice(username, semua):
    print("\n=== RIWAYAT TRANSAKSI ===")
    ada = tampilkan_riwayat(username, semua)
    if ada and konfirmasi("\nCetak ulang invoice?"):
        cetak_ulang_invoice(username, semua)

# laporan ringkas admin
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

# Menu admin
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
                riwayat_dan_invoice(username, True)
                input("\nTekan ENTER untuk kembali...")
            elif pilihan == "6":
                laporan_admin()
                input("\nTekan ENTER untuk kembali...")
            elif pilihan == "7":
                tambah_saldo_user()
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

# Menu user
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
                riwayat_dan_invoice(username, False)
                input("\nTekan ENTER untuk kembali...")
            elif pilihan == "5":
                print("Logout berhasil")
                jeda()
                break
            else:
                print("Pilihan tidak valid")
                jeda()
    except KeyboardInterrupt:
        print("dilarang mengisi memakai Ctrl")

# Program utama
def main():
    try:
        while True:
            bersihkan_layar()
            print("\n=== SISTEM RESERVASI TENANT BAZAR ===")
            print("1. Login")
            print("2. Registrasi")
            print("3. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                username = login()
                if username == "":
                    print("Login gagal 3 kali. Program berhenti.")
                    break
                if users[username]["role"] == "admin":
                    menu_admin(username)
                else:
                    menu_user(username)
            elif pilihan == "2":
                registrasi()
                jeda()
            elif pilihan == "3":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid")
                jeda()
    except KeyboardInterrupt:
        print("\nProgram dihentikan (dilarang mengisi memakai Ctrl+C)")

main()