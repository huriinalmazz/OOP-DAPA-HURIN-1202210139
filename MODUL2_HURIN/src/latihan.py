namaMakanan_1 = input("Masukkan Nama Barang1: ")
kodeMakanan_1 = int(input("Masukkan Kode Barang1: "))
hargaMakanan_1 = float(input("Masukkan Harga Barang1: "))
estimasiPembuatanMakanan_1 = int(input("Masukkan Jumlah Barang1: "))
diskonMakanan_1 = float(input("Masukkan Diskon Barang1: "))

namaMakanan_2 = input("Masukkan Nama Barang2: ")
kodeMakanan_2 = int(input("Masukkan Kode Barang2: "))
hargaMakanan_2 = float(input("Masukkan Harga Barang2: "))
estimasiPembuatanMakanan_2 = int(input("Masukkan Jumlah Barang2: "))
diskonMakanan_2 = float(input("Masukkan Diskon Barang2: "))

namaMinuman_3 = input("Masukkan Nama Barang3: ")
kodeMinuman_3 = int(input("Masukkan Kode Barang3: "))
hargaMinuman_3 = float(input("Masukkan Harga Barang3: "))
estimasiPembuatanMinuman_3 = int(input("Masukkan Jumlah Barang3: "))
diskonMinuman_3 = float(input("Masukkan Diskon Barang3: "))

#Ini adalah batas akhir jawaban day-1 !!!!

#Silahkan masukkan jawaban day-3 mulai dari bagian di bawah ini
list_menu = []
list_jumlah = []

while True: 
    pemesanan_makanan = int(input())
    if pemesanan_makanan == kodeMakanan_1:
        jmlh_pesanan = int(input())
        list_menu.append(kodeMakanan_1)
        list_jumlah.append(jmlh_pesanan)
    elif pemesanan_makanan == kodeMakanan_2:
        jmlh_pesanan = int(input())
        list_menu.append(kodeMakanan_2)
        list_jumlah.append(jmlh_pesanan)
    elif pemesanan_makanan == kodeMinuman_3:
        jmlh_pesanan = int(input())
        list_menu.append(kodeMinuman_3)
        list_jumlah.append(jmlh_pesanan)
    else:
        print("Mohon maaf, menu belum tersedia")
        continue
    
    tambah = input("Apakah anda ingin menambah pesanan lagi?(y/n)")

    if tambah.lower() == "n":
        print("\n=======================================")
        print("Nama Menu | Jml | Estimasi Waktu |")
        for i in range (len(list_menu)):
            if list_menu[i] == kodeMakanan_1:
                print(f"{namaMakanan_1} | {list_jumlah[i]} | {estimasiPembuatanMakanan_1 * list_jumlah[i]} |")
            elif list_menu[i] == kodeMakanan_2:
                print(f"{namaMakanan_2} | {list_jumlah[i]} | {estimasiPembuatanMakanan_2 * list_jumlah[i]} |")
            elif list_menu[i] == kodeMinuman_3:
                print(f"{namaMinuman_3} | {list_jumlah[i]} | {estimasiPembuatanMinuman_3 * list_jumlah[i]} |")
        print("=======================================")
        break
    elif tambah.lower() == "y":
        continue
      

