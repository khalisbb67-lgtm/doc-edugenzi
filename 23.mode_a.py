# mode a = append
# mode a digunakan untuk menambahkan data baru di akhir file
# jila filenya belum ada maka akan dibuatkan
#jika filenya sudah ada maka akan ditambahkan data baru di akhir file

with open("data/catatan2.txt", "a") as f:
    f.write("\ndata baru ditambahkan sekali")
    f.write("\ndata baru ditambahkan dua kali")


