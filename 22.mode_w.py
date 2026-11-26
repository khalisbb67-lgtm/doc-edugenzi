# mode w = write
# digunakan untuk menulis ke file tidak bisa membaca
# jika filenya belum ada maka akan dibuatkan
# jika sudah ada maka akan ditulis ulang

with open("data/resep_makanan.txt", "w") as file:
    #file.read()# error karena cuma bisa untuk menulis
    file.write("nasi goreng\n")# \n = enter
    file.write("bakso")
