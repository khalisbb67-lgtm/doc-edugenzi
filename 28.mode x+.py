# mode x+
# menambah kemampuan untuk bisa membaca

with open("data/catatan3.txt", "x+") as f:
    f.write("\niya iya ")
    f.seek(0)
    isi = f.read()

print(isi)