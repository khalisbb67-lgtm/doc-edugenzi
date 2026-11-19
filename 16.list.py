# list adalah tipe data yang bisa menampung banyak data
# list dibuat  dengan = [data1,data1,data3]
# list itu bisa menampung banyak data

teman = ["a","b","c","d"]
print(teman)
print(type([teman]))

#type ( untuk menegcek tipe data)
#list menampung tipe data apa saja
angka = [1,3,4]
teks = ["a","b","c"]
campuran = [1,"a",2,"b"]

#mengakses data pada list
#bisa diakses menggunakan indeks
#index itu urutan yang dimulai dari 0

teman = ["a","B","c","d"]
print(teman[0])
print(teman[3])
#print(teman[20])#error karena tidak ada dalam data


#index negatif
teman = ["a","B","c","d"]
print(teman[-2])
print(teman[-3])

#mengubah data dalam list
teman = ["a","b","c","d"]
teman[2] = "z"
print(teman)

#menambah data dalam list
#menggunakan append

buah = ['apel','jeruk,']
buah.append('mangga')
print(buah)

# insert(index,data)
#digunakan untuk menyissip data tertentu

hewan = ["kucing","harimau","kelinci"]
print(hewan)
hewan.insert(2,"kura kura")
print(hewan)

# extend(list)
#digunakan untuk menggabungkan 2 list

merk_mobil = ["toyota","mazda","honda"]

print(merk_mobil)
merk_mobil_high_class = ["ferrari","mercedes","bmw"]
print(merk_mobil_high_class)

merk_mobil.extend(merk_mobil_high_class) #digabung menjadi 2 buah list
print(merk_mobil)

# remove data
# digunakan untuk menghapus data yang pertama ketemu di dalam list

merk_mobil = ["toyota","mazda","honda","mazda"]
print(merk_mobil)
merk_mobil.remove("mazda")
print(merk_mobil)

# pop(index)
# akan menghapus data yang paling akhir di list
# pop akan mengembalikan data yang dihapus

merk_mobil = ["toyota","mazda","honda"]

print(merk_mobil)
yang_dihapus = merk_mobil.pop()
print(f"data yang dihapus : {yang_dihapus}")
print(merk_mobil)

yang_dihapus2 = merk_mobil.pop(0)
print(merk_mobil)
print(f"data yang dihapus : {yang_dihapus2}")


# del list[index]
# bakalan menghapus data pada index tertentu

merk_mobil = ["toyota","mazda","honda","mazda"]
print(merk_mobil)

del merk_mobil[2]
print(merk_mobil)

#clear digunkana untuk menghapus seluruh isi pada list

merk_mobil = ["toyota","mazda","honda","mazda"]
print(merk_mobil)

merk_mobil.clear()
print(merk_mobil)

# for list
# perulangan untuk tiap data pada list

merk_mobil = ["toyota","mazda","honda","mazda"]
for i in merk_mobil:
    print(i)

    # len
    # len digunakan untuk menghitung jumlah data pada list
merk_mobil = ["toyota","mazda","honda","mazda"]
print(len(merk_mobil)) # len() = menghitung jumlah data di dalam list

for i in range(len(merk_mobil)):
    print(i)
    print(merk_mobil[i])


# function di dalam list
# len = digunakan menghitung jumlah data di dalam list
# max = digunakan untuk menghitung nilai terbesar di salam list
# min = digunakan untuk menghitung nilai terkecil di dalam list
# sum = digunakan untuk menjumlahkan seluruh data di dalam list


angka = [1,2,3,4,5,6,7,8,9,1,10]
print(len(angka))
print(max(angka))
print(min(angka))
print(sum(angka))
angka.sort(reverse = True)
print(f'ini angka yang sudah di sort{angka}')


huruf = ["a", "b" ,"c","d" ,"e" ,"f"]
print(len(huruf))
print(max(huruf))
print(min(huruf))
# print(sum(huruf))

#reverse 
# digunnakan untuk membalik data  list

angka = [30,10,20,40]
angka.reverse()
print(angka)





