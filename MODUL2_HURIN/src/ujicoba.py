# # namaMakanan_1 = input("Masukkan Nama Barang1: ")
# # kodeMakanan_1 = int(input("Masukkan Kode Barang1: "))
# # hargaMakanan_1 = float(input("Masukkan Harga Barang1: "))
# # estimasiPembuatanMakanan_1 = int(input("Masukkan Jumlah Barang1: "))
# # diskonMakanan_1 = float(input("Masukkan Diskon Barang1: "))

# # namaMakanan_2 = input("Masukkan Nama Barang2: ")
# # kodeMakanan_2 = int(input("Masukkan Kode Barang2: "))
# # hargaMakanan_2 = float(input("Masukkan Harga Barang2: "))
# # estimasiPembuatanMakanan_2 = int(input("Masukkan Jumlah Barang2: "))
# # diskonMakanan_2 = float(input("Masukkan Diskon Barang2: "))

# # namaMinuman_3 = input("Masukkan Nama Barang3: ")
# # kodeMinuman_3 = int(input("Masukkan Kode Barang3: "))
# # hargaMinuman_3 = float(input("Masukkan Harga Barang3: "))
# # estimasiPembuatanMinuman_3 = int(input("Masukkan Jumlah Barang3: "))
# # diskonMinuman_3 = float(input("Masukkan Diskon Barang3: "))

# # #Ini adalah batas akhir jawaban day-1 !!!!

# # #Silahkan masukkan jawaban day-4 mulai dari bagian di bawah ini
# # import time

# # list_menu = []
# # list_jumlah = []
# # newcode = []
# # add = []

# # while True: 
# #     pemesanan_makanan = int(input())
# #     if pemesanan_makanan == kodeMakanan_1:
# #         jmlh_pesanan = int(input())
# #         list_menu.append(kodeMakanan_1)
# #         list_jumlah.append(jmlh_pesanan)
# #         newcode.append(kodeMakanan_1)
# #         add.append(estimasiPembuatanMakanan_1)

# #     elif pemesanan_makanan == kodeMakanan_2:
# #         jmlh_pesanan = int(input())
# #         list_menu.append(kodeMakanan_2)
# #         list_jumlah.append(jmlh_pesanan)
# #         newcode.append(kodeMakanan_2)
# #         add.append(estimasiPembuatanMakanan_2)

# #     elif pemesanan_makanan == kodeMinuman_3:
# #         jmlh_pesanan = int(input())
# #         list_menu.append(kodeMinuman_3)
# #         list_jumlah.append(jmlh_pesanan)
# #         newcode.append(kodeMinuman_3)
# #         add.append(estimasiPembuatanMinuman_3)

# #     else:
# #         print("Mohon maaf, menu belum tersedia")
# #         continue
    
# #     tambah = input("Apakah anda ingin menambah pesanan lagi?(y/n)")

# #     if tambah.lower() == "n":
# #         print("\n=======================================")
# #         print("Nama Menu | Jml | Estimasi Waktu |")
# #         for i in range (len(list_menu)):
# #             if list_menu[i] == kodeMakanan_1:
# #                 print(f"{namaMakanan_1} | {list_jumlah[i]} | {estimasiPembuatanMakanan_1} |")
# #             elif list_menu[i] == kodeMakanan_2:
# #                 print(f"{namaMakanan_2} | {list_jumlah[i]} | {estimasiPembuatanMakanan_2} |")
# #             elif list_menu[i] == kodeMinuman_3:
# #                 print(f"{namaMinuman_3} | {list_jumlah[i]} | {estimasiPembuatanMinuman_3} |")
# #         print("=======================================")
# #         break
# #     elif tambah.lower() == "y":
# #         continue

# # totalEstimasi = 
# # waktu = time.ctime().split()
# # currentTime = waktu[3].split(":")
# # minute = int(currentTime[1])
# # extraMinute = 0

# # for k in range(len(list_menu)):
# #     a = str(newcode[k])
# #     if("11" in a):
# #         if(list_jumlah[k] <= 5):
# #             extraMinute = int(extraMinute + add[k])
# #         else:
# #             extraMinute = int(extraMinute + add[k] + (list_jumlah[k] * 0.5))
    
# #     else:
# #         extraMinute = int(extraMinute + add[k])

# # print("Pesanan anda diperkirakan selesai pukul {}:{}".format(currentTime[0], minute + extraMinute))

# while True:
#     try:
#         a = int(input('Masukkan nilai awal: '))
#     except ValueError:
#         print('Nilai awal harus angka dan coba kembali')
#         continue

#     try:
#         b = int(input('Masukkan Nilai akhir: '))
#         perkalian = a*b
#         if perkalian >= 0:
#             print(f'Hasil {perkalian}')
#         else:
#             print('Nilai harus positif')
#         break
#     except ValueError:
#         print('Coba kembali')
        
try:
    a = int(input('Masukkan nilai awal: '))
    if a % 2 == 0:
        print('Habis dibagi 2')
except:
    print('Tidak Habis dibagi 2')

while True:
    try:
        a = int(input('Masukkan nilai awal: '))
    except ValueError:
        print('Nilai awal harus angka silahkan coba kembali')
        continue
    try:
        b = int(input('Masukkan nilai akhir: '))
        print(f'Hasil Awal * Akhir: {float(a*b)}')
    except ValueError:
        print('Nilai akhir harus angka silahkan coba kembali')
        continue
