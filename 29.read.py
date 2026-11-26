# read() = digunakan untuk membaca seluruh isi file
# readline()= digunakan untuk membaca satu baris
# readlines()= digunakan untuk membaca seluruh baris di file dan mengmbalikan dalam bentuk list

with open("data/catatan2.txt", "r") as f:
  #  print(f.read())
  #  print(f.readline(1000))
   isi = f.readlines()
   print(isi) 
   print(isi[5])

