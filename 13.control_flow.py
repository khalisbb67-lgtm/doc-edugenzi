# control flow adalah alur program 
#if,else,elif
#for dan while


# program untuk mengecek apakah bilangan itu ganjil atau genap

for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} adalah bilangan genap")

    else:
        print(f"{i} adalah bilangan ganjil")

# ver 2 

inputan = input("masukkan angka: ")
inputan = int(inputan) # mengubah tipe data string menjadi integer

if inputan % 2 == 0:
    print(f"{inputan} adalah bilangan genap")
else:
    print(f"{inputan} adalah bilangan ganjil")    