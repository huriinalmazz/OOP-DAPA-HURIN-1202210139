namaMakanan_1 = input()
kodeMakanan_1 = int(input())
hargaMakanan_1 = float(input())
estimasiPembuatanMakanan_1 = int(input())
diskonMakanan_1 = float(input())

namaMakanan_2 = input()
kodeMakanan_2 = int(input())
hargaMakanan_2 = float(input())
estimasiPembuatanMakanan_2 = int(input())
diskonMakanan_2 = float(input())

namaMinuman_3 = input()
kodeMinuman_3 = int(input())
hargaMinuman_3 = float(input())
estimasiPembuatanMinuman_3 = int(input())
diskonMinuman_3 = float(input())

#Ini adalah batas akhir jawaban day-1 !!!!
#Silahkan masukkan jawaban day-4 mulai dari bagian di bawah ini
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
    

now = time.ctime().split()
current_time = now[3].split(":")
tempat_menit = int(current_time[1])
tambah_menit = 0
tambah_jam = 0


for p in range(0,len(list_makanan)) :
    sementara = str(kodetambahan[p])
    if("11" in sementara) :

        if (jumlah_nya[p] <= 5) :
            tambah_menit = int(tambah_menit + perkiraantambahan[p])

        else :
            tambah_menit = int(tambah_menit + perkiraantambahan[p] + (jumlah_nya[p]*0.5))
            khusustambahan = tambah_menit
            
    else :
        tambah_menit = int(tambah_menit + perkiraantambahan[p])

result = tempat_menit + tambah_menit
perkalian = int(result / 60)
result_jam = int(current_time[0])

for dahla in range (1,perkalian+2) :

    if (result >= 60) :
        tambah_jam = tambah_jam + 1
        result = result - 60

    else :
        result_jam = int(result_jam + tambah_jam)
        break

print("\n=======================================\nNama Menu | Jml | Estimasi Waktu |")
for j in range (0,len(list_makanan)) :
    sementara_aja = str(kodetambahan[j])
    if ("11" in sementara_aja) :
        if (jumlah_nya[j] > 5) :
            print(list_makanan[j],"|",jumlah_nya[j],"|","11","|")
        else :
            print(list_makanan[j],"|",jumlah_nya[j],"|",perkiraantambahan[j],"|")
    else :
        print(list_makanan[j],"|",jumlah_nya[j],"|",perkiraantambahan[j],"|")

print("=======================================")
print("Pesanan anda diperkirakan selesai pukul  {}:{}".format(12,result))