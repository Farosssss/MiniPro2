Muhammad Farros anand
2409116085
Sistem Informasi C'24

APLIKASI PENYEWAAN TENDA

1. Import Library :
   from prettytable import PrettyTable

2. Variabel Global :
  tenda = []
  transaksi = []
  pengguna = {'admin': {'password': 'admin', 'level': 'admin'}}

3. Fungsi tambah_tenda :
   def tambah_tenda(nama, kapasitas, harga, jumlah):
    tenda.append({'nama': nama, 'kapasitas': kapasitas, 'harga': harga, 'jumlah': jumlah})
    print(f"Tenda {nama} berhasil ditambahkan.")

4. Fungsi hapus_tenda :
   def hapus_tenda(nama):
    for t in tenda:
        if t['nama'] == nama:
            tenda.remove(t)
            print(f"Tenda {nama} berhasil dihapus.")
            return
    print(f"Tenda {nama} tidak ditemukan.")

5. Fungsi lihat_tenda :
   def lihat_tenda():
    if not tenda:
        print("Tidak ada tenda yang tersedia.")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama Tenda", "Kapasitas", "Harga Sewa per Hari", "Jumlah Tersedia"]
        for idx, t in enumerate(tenda, 1):
            table.add_row([idx, t['nama'], t['kapasitas'], t['harga'], t['jumlah']])
        print(table)

6. Fungsi pesan_tenda :
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

7. Fungsi kembalikan_tenda :
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

8. Fungsi register : 
   def register(username, password):
    pengguna[username] = {'password': password, 'level': 'user'}
    print(f"Registrasi berhasil. Anda terdaftar sebagai user.")

9. Fungsi login :
   def login(username, password):
    if username in pengguna and pengguna[username]['password'] == password:
        return pengguna[username]['level']
    return None

10. Fungsi main() :
    def main():
    while True:
        print("\n=== Sistem Penyewaan Tenda ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilihan = input("Pilih opsi (1/2/3): ")
  a. Login
             if pilihan == '1':
            print("\n--- Login ---")
            username = input("Username: ")
            password = input("Password: ")
            level = login(username, password)
    
  b. Level Admin
                  if level == 'admin':
                while True:
                    print("\n--- Admin ---")
                    print("1. Tambah Tenda")
                    print("2. Hapus Tenda")
                    print("3. Lihat Tenda")
                    print("4. Logout")
                    admin_pilihan = input("Pilih aksi (1/2/3/4): ")

  c. Level User
              elif level == 'user':
                while True:
                    print("\n--- User ---")
                    print("1. Lihat Tenda")
                    print("2. Pesan Tenda")
                    print("3. Kembalikan Tenda")
                    print("4. Logout")
                    user_pilihan = input("Pilih aksi (1/2/3/4): ")

d. Register
          elif pilihan == '2':
            print("\n--- Register ---")
            username = input("Username: ")
            if username in pengguna:
                print("Username sudah ada, silakan coba yang lain.")
            else:
                password = input("Password: ")
                register(username, password)

e. Keluar
          elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem penyewaan tenda.")
            break


FLOWCHART
![image](https://github.com/user-attachments/assets/70514672-753d-4bdf-82ed-a9d970dc3c5a)




OUTPUT
![image](https://github.com/user-attachments/assets/02dcffe3-5d99-471c-8fc7-2652ed060c28)

![image](https://github.com/user-attachments/assets/7504e92f-4403-4335-a968-1791082dd27e)

![image](https://github.com/user-attachments/assets/df005eaf-795c-4b6c-8008-f9a408b3edac)







    










