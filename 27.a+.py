#mode a+
#menambah kemampuan si mode a untuk bisa membaca isi file itu

with open("data/catatan2.txt", "a+") as f:
    f.write("\niya iya ")
    f.seek(0)
    isi = f.read()

print(isi)