# import datetime
# import pytz

# tz_ID = pytz.timezone('Asia/Jakarta')
# datetime_ID = datetime.datetime.now(tz_ID)

# datetime_ID += datetime.timedelta(minutes = totalEstimasi)
# estimated_time = datetime_ID.strftime("%H:%M")

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

import time
pemesanan_makanan = int(input())

list_makanan = []
jumlah_nya = []
totaluda = []
kodetambahan = []
perkiraantambahan = []
i = 0
x = 0

while(i!= 1) :
    if(pemesanan_makanan == kodeMakanan_1) :
        list_makanan.append(namaMakanan_1)
        jmlh_pesanan = int(input())
        jumlah_nya.append(jmlh_pesanan) 
        perkiraan = estimasiPembuatanMakanan_1
        totaluda.append(perkiraan*jmlh_pesanan)
        kodetambahan.append(kodeMakanan_1)
        perkiraantambahan.append(perkiraan)
       
    elif(pemesanan_makanan == kodeMakanan_2) :
        list_makanan.append(namaMakanan_2)
        jmlh_pesanan = int(input()) 
        jumlah_nya.append(jmlh_pesanan)
        perkiraan = estimasiPembuatanMakanan_2
        totaluda.append(perkiraan*jmlh_pesanan)
        kodetambahan.append(kodeMakanan_2)
        perkiraantambahan.append(perkiraan)

    elif(pemesanan_makanan == kodeMinuman_3) :
        list_makanan.append(namaMinuman_3)
        jmlh_pesanan = int(input()) 
        jumlah_nya.append(jmlh_pesanan) 
        perkiraan = estimasiPembuatanMinuman_3
        totaluda.append(perkiraan*jmlh_pesanan)
        kodetambahan.append(kodeMinuman_3)
        perkiraantambahan.append(perkiraan)

    else : 
        while(x != 1) :
            print("Mohon maaf, menu belum tersedia")
            pemesanan_makanan = int(input())

            if(pemesanan_makanan == kodeMakanan_1) :
                list_makanan.append(namaMakanan_1)
                jmlh_pesanan = int(input())
                jumlah_nya.append(jmlh_pesanan) 
                perkiraan = estimasiPembuatanMakanan_1
                totaluda.append(perkiraan*jmlh_pesanan)
                kodetambahan.append(kodeMakanan_1)
                perkiraantambahan.append(perkiraan)
                x = 1
       
            elif(pemesanan_makanan == kodeMakanan_2) :
                list_makanan.append(namaMakanan_2)
                jmlh_pesanan = int(input()) 
                jumlah_nya.append(jmlh_pesanan)
                perkiraan = estimasiPembuatanMakanan_2
                totaluda.append(perkiraan*jmlh_pesanan)
                kodetambahan.append(kodeMakanan_2)
                perkiraantambahan.append(perkiraan)
                x = 1

            elif(pemesanan_makanan == kodeMinuman_3) :
                list_makanan.append(namaMinuman_3)
                jmlh_pesanan = int(input()) 
                jumlah_nya.append(jmlh_pesanan) 
                perkiraan = estimasiPembuatanMinuman_3
                totaluda.append(perkiraan*jmlh_pesanan)
                kodetambahan.append(kodeMinuman_3)
                perkiraantambahan.append(perkiraan)
                x = 1
    

    pesan_lagi = input("Apakah anda ingin menambah pesanan lagi?(y/n)")

    if(pesan_lagi == "n") :
        i = 1
    
    else :
        pemesanan_makanan = int(input())

hehe = time.ctime().split()
waktu_sekarang = hehe[3].split(":")
tempat_menit = int(waktu_sekarang[1])
menit_tambahan = 0

    
print("\n=======================================\nNama Menu | Jml | Estimasi Waktu |")
for j in range (0,len(list_makanan)) :
    print(list_makanan[j],"|",jumlah_nya[j],"|",totaluda[j],"|")
print("=======================================")

for p in range (0,len(list_makanan)):
    sementara_aja = str(kodetambahan[p])
    if("11" in sementara_aja):
        if (jumlah_nya[p] <= 5):
            menit_tambahan = int(menit_tambahan + perkiraantambahan[p])

        else:
            menit_tambahan = int(menit_tambahan + perkiraantambahan[p] + (jumlah_nya[p]*0.5))
        
    else:
         menit_tambahan = int(menit_tambahan + perkiraantambahan[p])

print("Pesanan anda diperkirakan selesai pukul {}:{}".format(waktu_sekarang[0], tempat_menit + menit_tambahan, waktu_sekarang[2]))
