#w+
#menambahkan kemampuan si mode w untuk bisa membaca isi filenya itu
#tetap bakalan menghapus/menimpa isi filenya

with open("data/data_keuangan.txt", "w+") as f:
    f.write("data baru ditambahkan\n")
    f.seek(0) # menggeser pointer ke awal
    isi = f.read()


print(isi)