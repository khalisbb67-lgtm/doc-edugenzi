#methode string adalah function function yang bisa digunakan pada data dengan tipe data string
nama = "daffa KHALIS"
# upper() = mengubah semua huruf menjadi huruf kapital
print(nama.upper())

#lower() = mengubah semua huruf menjadi huruf kecil
print(nama.lower())

#capitalize()= mengubah kata pertama menjadihuruf kapital
print(nama.capitalize())

#title() = mengubah huruf pertama setiap kata menjadi huruf besar
print("menggambar bangunan sipil".title())

#strip = menghapus karakter di awal dan akhir
kata = "        khalis      "
print(f"[{kata}]")
print(f"[{kata.strip()}]")

kata_2 = "!!@@@$$$$ daffa !!!@@@$$$"
print(f"[{kata_2.strip(" !@$")}]")

#lstrip = menghapus karakter di kiri

kata_3 ="!!!! daffa !!!!"
print(f"[{kata_3.lstrip("!")}]")

#rstip = menghapus karakter di sebelah kanan

kata_4 = "!!!! daffa !!!!"
print(f"[{kata_4.rstrip("!")}]")

#find() = mencari kata di dalam string, jika tidak ditemukan maka akan mengembalikan nilai -1
kata_5 = "daffa khalis"

print(kata_5.find("k"))
print(kata_5.find("z"))
print(kata_5.find("d"))

#count() = menghitung jumlah kata di dalam string
#perameter count()itu wajib jika kita tidak memasukkan parameter maka akan error
kata_6 = "labubu"
print(kata_6.count("b"))
print(kata_6.count("u"))
print(kata_6.count("o"))
print(kata_6.count("l"))

inputan_pengguna = input("masukkan kata apa aja : ")
print(f"jumlah huruf a di dalam kata {inputan_pengguna} adalah {inputan_pengguna.count('a')}") 
