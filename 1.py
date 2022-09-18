import math 
h = float(input("masukkan ketinggian menara (dalam satuan vektor): "))
a = float(input("masukkan derajat sudut elevasi pengamat terhadap ujung belakang kapal: "))
b = float(input("masukkan derajat sudut elevasi pengamat terhadap ujung depan kapal: "))
#saya memakai fungsi importmath untuk mengakses nilai matematika dengan nilai float
#kemudian saya masukkan nilai "H"nya dengan parameter ketinggian menara dalam satuan vektor
#terus nilai a dan b dengan parameternya derajat sudut elevasi ujung belakang kapal dan depan kapal
belakang = h * (math.tan(math.radians(a)))
depan = h * (math.tan(math.radians(b)))
panjang = belakang-depan
#saya menggunakan math.tan untuk mengembalikan tan pada sumbu radians
#saya masukkan panjang= belakang-depan
print("panjang kapalnya adalah", panjang, "m")
#kemudian untuk printnya dengan parameter panjang kapalnya "m" karena satuannya diubah dalam meter.