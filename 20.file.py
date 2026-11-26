#file 
# file adalah tempat untuk menyimpan data
# file isa dibuka dengan bantuan function
# function open() memiliki 2 parameter
# parameter pertama itu adalah nama file
# parameter ke dua adalah mode
# mode itu adalah cara membuka file

f = open("data/catatan.txt", "r") #r = read
isi = f.read() #membaca seluruh isi file
print(isi)

f.close()# menutup  file



#with
# baca file dan akan otomatis tertutup
with open("data/catatan.txt", "r") as file:
    isi = file.read()
    print(isi)

    