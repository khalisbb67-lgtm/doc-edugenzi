# mode x
# mode x digunakan untuk membuat file yang harus belum ada
# jika filenya sudah aa maka filenya akan error


with open("data/data_keuangan.txt", "x") as f:
    f.write("data uang")
