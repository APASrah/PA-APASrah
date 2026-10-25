
import os
import time
import json
import random
from datetime import datetime
from prettytable import PrettyTable
import pwinput

folder_data = r"C:\ApasProjek"
path_users = folder_data + r"\users.json"
path_tenants = folder_data + r"\tenants.json"
path_transaksi = folder_data + r"\transaksi.json"
folder_invoice = folder_data + r"\invoice"

KATEGORI = ("Makanan", "Minuman", "Fashion", "Kerajinan", "Lainnya")

MIN_TOPUP = 10000
MAX_TOPUP = 10000000

# Membaca data dari file JSON
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

# transaksi.json dibuat otomatis kalau belum ada
try:
    with open(path_transaksi, "r", encoding="utf-8") as f:
        transaksi = json.load(f)
except FileNotFoundError:
    transaksi = []
except json.JSONDecodeError:
    print("Isi transaksi.json rusak!")
    exit()

# Menyesuaikan data lama: tenant tanpa stok diberi stok 1,
# user tanpa saldo diberi saldo 0
for t in tenants:
    if "stok" not in t:
        t["stok"] = 1
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

# memilih kategori lewat nomor menu
def pilih_kategori():
    print("1. Makanan  2. Minuman  3. Fashion  4. Kerajinan  5. Lainnya")
    while True:
        nomor = input_angka("Pilih kategori (1-5) : ")
        if 1 <= nomor <= 5:
            return KATEGORI[nomor - 1]
        print("Nomor tidak ada.")

# mencari posisi tenant berdasarkan ID
# kalau tidak ketemu, program melempar error (raise)
def cari_index(id_tenant):
    index = 0
    for tenant in tenants:
        if tenant["id"] == id_tenant:
            return index
        index = index + 1
    raise ValueError("ID tidak ditemukan!")

# status otomatis mengikuti stok
def perbarui_status(tenant):
    if tenant["stok"] > 0:
        tenant["status"] = "Tersedia"
    else:
        tenant["status"] = "Penuh"

# menampilkan data
def tampilkan_data():
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Tenant", "Kategori", "Harga Sewa", "Stok", "Status"]
    for t in tenants:
        tabel.add_row([t["id"], t["nama"], t["kategori"], rupiah(t["harga"]), t["stok"], t["status"]])
    print(tabel)

# menambah data
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

    id_baru = 1
    for tenant in tenants:
        if tenant["id"] >= id_baru:
            id_baru = tenant["id"] + 1

    tenant_baru = {"id": id_baru, "nama": nama, "kategori": kategori, "harga": harga, "stok": stok, "status": "Tersedia"}
    perbarui_status(tenant_baru)
    tenants.append(tenant_baru)
    simpan_data(path_tenants, tenants)
    print("Data tenant berhasil ditambahkan!")

# mengubah data
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

# menghapus data (dengan konfirmasi y/n)
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

# ================= E-MONEY & TRANSAKSI =================

# cek saldo
def lihat_saldo(username):
    print("\nSaldo Anda :", rupiah(users[username]["saldo"]))

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

# reservasi tenant + pembayaran memakai saldo
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

# tabel riwayat transaksi; semua=True untuk admin, False untuk user tertentu
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
            print("5. Riwayat seluruh transaksi")
            print("6. Laporan ringkas")
            print("7. Cetak ulang invoice")
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

# Menu user
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