from prettytable import PrettyTable

tenda = []
transaksi = []
pengguna = {'admin': {'password': 'admin', 'level': 'admin'}}

def tambah_tenda(nama, kapasitas, harga, jumlah):
    tenda.append({'nama': nama, 'kapasitas': kapasitas, 'harga': harga, 'jumlah': jumlah})
    print(f"Tenda {nama} berhasil ditambahkan.")

def hapus_tenda(nama):
    for t in tenda:
        if t['nama'] == nama:
            tenda.remove(t)
            print(f"Tenda {nama} berhasil dihapus.")
            return
    print(f"Tenda {nama} tidak ditemukan.")

def lihat_tenda():
    if not tenda:
        print("Tidak ada tenda yang tersedia.")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama Tenda", "Kapasitas", "Harga Sewa per Hari", "Jumlah Tersedia"]
        for idx, t in enumerate(tenda, 1):
            table.add_row([idx, t['nama'], t['kapasitas'], t['harga'], t['jumlah']])
        print(table)

def pesan_tenda(nama, jumlah_hari):
    for t in tenda:
        if t['nama'] == nama:
            if t['jumlah'] > 0:
                total_harga = t['harga'] * jumlah_hari
                transaksi.append({'nama': t['nama'], 'hari': jumlah_hari, 'total': total_harga})
                t['jumlah'] -= 1  
                print(f"Tenda {nama} berhasil dipesan selama {jumlah_hari} hari. Total harga: {total_harga}")
                return
            else:
                print(f"Tenda {nama} tidak tersedia saat ini.")
                return
    print(f"Tenda {nama} tidak ditemukan.")

def kembalikan_tenda(nama):
    for t in transaksi:
        if t['nama'] == nama:
            transaksi.remove(t)
            for tenda_item in tenda:
                if tenda_item['nama'] == nama:
                    tenda_item['jumlah'] += 1 
                    print(f"Tenda {nama} berhasil dikembalikan.")
                    return
    print(f"Tenda {nama} tidak ditemukan dalam transaksi.")

def register(username, password):
    pengguna[username] = {'password': password, 'level': 'user'}
    print(f"Registrasi berhasil. Anda terdaftar sebagai user.")

def login(username, password):
    if username in pengguna and pengguna[username]['password'] == password:
        return pengguna[username]['level']
    return None

def main():
    while True:
        print("\n=== Sistem Penyewaan Tenda ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            print("\n--- Login ---")
            username = input("Username: ")
            password = input("Password: ")

            level = login(username, password)

            if level == 'admin':
                while True:
                    print("\n--- Admin ---")
                    print("1. Tambah Tenda")
                    print("2. Hapus Tenda")
                    print("3. Lihat Tenda")
                    print("4. Logout")
                    admin_pilihan = input("Pilih aksi (1/2/3/4): ")

                    if admin_pilihan == '1':
                        nama = input("Nama tenda: ")
                        kapasitas = int(input("Kapasitas tenda: "))
                        harga = float(input("Harga sewa per hari: "))
                        jumlah = int(input("Jumlah tenda: "))
                        tambah_tenda(nama, kapasitas, harga, jumlah)

                    elif admin_pilihan == '2':
                        nama = input("Nama tenda yang ingin dihapus: ")
                        hapus_tenda(nama)

                    elif admin_pilihan == '3':
                        lihat_tenda()

                    elif admin_pilihan == '4':
                        break

                    else:
                        print("Pilihan tidak valid.")

            elif level == 'user':
                while True:
                    print("\n--- User ---")
                    print("1. Lihat Tenda")
                    print("2. Pesan Tenda")
                    print("3. Kembalikan Tenda")
                    print("4. Logout")
                    user_pilihan = input("Pilih aksi (1/2/3/4): ")

                    if user_pilihan == '1':
                        lihat_tenda()

                    elif user_pilihan == '2':
                        nama = input("Nama tenda yang ingin dipesan: ")
                        jumlah_hari = int(input("Jumlah hari sewa: "))
                        pesan_tenda(nama, jumlah_hari)

                    elif user_pilihan == '3':
                        nama = input("Nama tenda yang ingin dikembalikan: ")
                        kembalikan_tenda(nama)

                    elif user_pilihan == '4':
                        break

                    else:
                        print("Pilihan tidak valid.")

            else:
                print("Username atau password salah.")

        elif pilihan == '2':
            print("\n--- Register ---")
            username = input("Username: ")
            if username in pengguna:
                print("Username sudah ada, silakan coba yang lain.")
            else:
                password = input("Password: ")
                register(username, password)

        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem penyewaan tenda.")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
