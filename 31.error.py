#syntax error 
#adalah jenis error yang disebabkan karena kesalahan penulisan syntax
#runtimme error
#adalah jenis error yang terjadi ketika program bekerja

#contoh syntax error

#lupa titik dua di if
#if 7 > 6
#    print("benar")
#kutip tidak ditutup


#identasi salah

#if 7>6:
#print("benar")


#runtime error
#name error
#adalah error yang disebabkan karena variabel tidak dideklarasikan

#nama = "daffa"
#print(nma)


#type error
#adalah error yang disebabkan karema tipe data tidak sesuai

#angka = 10
#print("angka"+angka)

#value error
#adalah error yang disebabkan karena nilai yang dimasukkan tidak sesuai 
#angka = int("dua")
#print(angka)

#index error
#index error adalah error yang disebabkan karena index yang dimasukkan diluar batas index
#angka = [1,2,3,4]
#print(angka[5])

#key error 
#key error adalah error yang disebabkan karena key yang dimasukkan tidak ada

#siswa = {
#    "nama" = "daffa"
#}

#print(siswa["umur"])
#print(siswa.get("umur"))


#zero division error
# zero division error adalah error yang disebabkan karena pembagian dengan nol

#print(10/0)
 
#cara menangani error
#cara pertama

a = int(input("masukkan angka pembagi:"))
b = int(input("masukkan angka yang dibagi:"))
if b !=0:
    print(a/b)
else:
    print("tidak boleh dibagi dengan nol")

