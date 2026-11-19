# loop
# for loop = perulangan dengan jumlah yang jelas


for i in range(100):  #akan melakukan pengulangan 100 kali
   print("haiii")


for i in range(10):  # dimulai dari 0
    print(i)
 
# mengatur range
# range start stop step
# start = dimulai dari angka mana
# stop = berhhenti sebelum angka stop
# step = berapa langkah yang dilakukan



# start
for i in range(5):
    print(i)

# start stop
for i in range(5,15): # akan melakukan perulangan dari angka 5 sampai sebelum 15
    print(i)

# start stop step
for i in range(1, 10, 2): # akan melakukan perulangan dari angka 1 sampai sebelum angka 10 dengan step 2
    print(i)

# implementasi for untuk tabel perkalian
for i in range(1,11):
    print(f"5 x {i} = {5*i}")

#contoh implementasi for untuk perhitungan 
# ver 1
total = 0

for i in range(1,6):
    total = total + i

print(total)

# ver 2 (augmented assigment)
total = 0

for i in range(1,6):
    total += i



print(total)


# for string

for huruf in "edugenzi":
    print(huruf)



# for string
jumlah = 0
kata = "edugenziiiiiii"
for huruf in kata :
    jumlah +=1
    print(huruf)

print("jumlah kata",jumlah)

print(len(kata)) # len digunakan untuk menghitung jumlah karakter