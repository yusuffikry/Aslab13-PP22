print ("program konversi waktu dari jumlah detik ke Jam/menit/detik")
#saya ingin mengonversi dari jumlah detik yang ingin saya masukkan,berubah menjadi jam/menit/detik
jumlah_detik = int(input("masukkan jumlah detik : "))
#saya menggunakan int agar dapat mengubah bilangan yang diinginkan,seperti yang saya masukkan parameternya masukkan jumlah detik
jam = jumlah_detik//3600
sisa_detik=jumlah_detik-3600*jam 
menit=sisa_detik//60
detik=sisa_detik-(60*menit)
#rumus yang saya gunakan, saya belajar dari youtube
print ("%02d:%02d:%02d "%(jam,menit,detik))
#saya masukkan parameter %02d:%02d:%02d "%" untuk menjadikan tampilan menjadi contoh seperti 2 jam menjadi 02