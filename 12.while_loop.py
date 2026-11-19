# loop 
# while loop = perulangan selama kondisi itu benar

hitung = 0

while hitung <= 3:
    print(hitung)
    hitung +=1 # hitung = hitung + 1

# infinite loop => perulangan tak terhingga
# hitung = 0

# while hitung <= 3:
    #print(hitung)

# contoh implementasi minta kata sandi dengan benar
 
kata_sandi = "edugenzi"
kata = ""

while kata != kata_sandi:  # akan terus melakukan perulangan selama kata sandi belum sama dengan kata yang kita masukkan
    kata = input("masukkan kata sandi:")

print("kata sandi benar")
print("login berhasil")