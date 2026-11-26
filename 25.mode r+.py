#mode r+
#mode r+ menambah kemampuan mode r supaya bisa menulis juga
#pointernya bakalan ada di awal (indeks 0), dia tu bakalan nimpa teks yang ada di file


with open("data/resep_makanan.txt", "r+") as f:
    f.write("tes mode r+")
    print(f.tell())# digunakan untuk melihat posisi kusor sekarang
    f.seek(0)
    print(f.read())

