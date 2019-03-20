import csv

file = open('DataTugas2.csv', 'r')                      #lokasi file, Nama file, Inisialisasi, r = read.
reader = csv.reader(file,quoting = csv.QUOTE_NONNUMERIC)#quoting = csv.QUOTE_NONNUMERIC : data yg tidak bertanda kutip = angka

hasil = []

next(reader)                                    #digunakan agar data yang dibaca dimulai dari data 1, bukan judul kolom
for data in reader:                             #membaca tiap baris yang ada di file
#fuzzy fication :
    if data[1] < 0.9:
        pr = 1
    elif 0.9 <= data[1] <= 1.4:                 #mencari nilai pendapatan rendah(pr)
        pr = (1.4 - data[1]) / (1.4 - 0.9)
    else:
        pr = 0

    if data[1]< 0.9:                            #mencari nilai pendapatan sedang(ps)
        ps = 0
    elif 0.9 <= data[1]< 1:
        ps = (data[1]- 0.9)/(1 - 0.9)
    elif 1 <= data[1]< 1.4:
        ps = 1
    elif 1.4 <= data[1]< 1.5:
        ps = (1.5 - data[1])/(1.5 - 1.4)
    else:
        ps= 0

    if data[1]< 1.3:                            #mencari nilai pendapatan tinggi (pt)
        pt = 0
    elif 1.3 <= data[1]< 1.5:
        pt = (data[1]- 1.3) / (1.5 - 1.3)
    else:
        pt = 1

    if data[2] < 30:                            #mencari nilai hutang dikit (hd)
        hd = 1
    elif 30<= data[2] < 40:
        hd = (40 - data[2])/(40-30)
    else:
        hd = 0

    if data[2] < 40:                            #mencari nilai hutang sedang (hs)
        hs = 0
    elif 40<= data[2] < 50:
        hs = (data[2] - 40)/(50-40)
    elif 50<= data[2] < 60:
        hs = 1
    elif 60<= data[2] < 70:
        hs = (70 - data[2])/(70-60)
    else:
        hs = 0

    if data[2] < 60:                            #mencari nilai hutang banyak (hb)
        hb = 0
    elif 60 <= data[2] < 70:
        hb = (data[2] - 60)/(70-60)
    else:
        hb = 1

    #rules :
    #pr dan hd = mungkin
    #pr dan hs = ya
    #pr dan hb = ya
    #ps dan hd = tidak
    #ps dan hs = tidak
    #ps dan hb = ya
    #pt dan hd = tidak
    #pt dan hs = tidak
    #pt dan hb = mungkin

    #inference :
    r1 = min(pr,hd) #mungkin
    r2 = min(pr,hs) #ya
    r3 = min(pr,hb) #ya
    r4 = min(ps,hd) #tidak
    r5 = min(ps,hs) #tidak
    r6 = min(ps,hb) #ya
    r7 = min(pt,hd) #tidak
    r8 = min(pt,hs) #tidak
    r9 = min(pt,hb) #mungkin

    print("data ke : ", int(data[0]))
    print("pr nya adalah : ", pr)
    print("ps nya adalah : ", ps)
    print("pt nya adalah : ", pt)
    print("hd nya adalah : ", hd)
    print("hs nya adalah : ", hs)
    print("hb nya adalah : ", hb)
    print("r1 nya adalah : ", r1)
    print("r2 nya adalah : ", r2)
    print("r3 nya adalah : ", r3)
    print("r4 nya adalah : ", r4)
    print("r5 nya adalah : ", r5)
    print("r6 nya adalah : ", r6)
    print("r7 nya adalah : ", r7)
    print("r8 nya adalah : ", r8)
    print("r9 nya adalah : ", r9)

    #pencarian nilai max :
    mungkin = max(r1,r9)
    ya = max(r2,r3,r6)
    tidak = max(r4,r5,r7,r8)
    print("Nilai tidak : ", tidak)
    print("Nilai mungkin : ",mungkin )
    print("Nilai ya : ", ya)

    #defuzzification : #mencari nilai kelayakan menggunakan metode sugeno

    a = (tidak * 30 + mungkin * 50 + ya * 70)
    b = tidak + mungkin + ya
    y = a/b#nilai kelayakan
    print("Nilai layak = ",y)
    print("==========================================")

    hasil.append([data[0],y])                               #nilai kelayakan dimasukkan ke dalam list hasil(no.keluarga, nilai layak)
    #akhir dari for

hasil = sorted(hasil, key = lambda x: x[1],reverse=True)    #mensorting nilai kelayakan dengan descending
print(hasil[0:20])                                          #menampilkan 20 data yang berhak mendapatkan bantuan

#memasukkan nomor keluarga yg berhak kedalam file csv :
for i in range(0,20):
    if i is 0:
        baca = open("TebakanTugas2.csv",'w')                #membuka file dan menimpanya(w = menulis dan menghapus file lama)
        baca.write(str(hasil[i][0]))                        #menulis data pada file csv
        baca.write("\n")
        baca.close()
    elif i is not 0:
        baca = open("TebakanTugas2.csv",'a')                #mode 'a' = menambah data di akhir baris
        baca.write(str(hasil[i][0]))                        #menulis data pada file csv
        baca.write("\n")
        baca.close()                                        #menutup file agar file tersave

