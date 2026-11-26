#mode r
#digunakan untuk membaca isi file,tidak bisa menulis
#mode r itu wajib filenya sudah ada,jika tidak ada maka akan error

with open("data/catatan2.txt", "r") as f:
    print(f.read())

