# dictionary 
# adalah tipe data dengan key-value/berpasangan
# key cuma sting dan integer
# value bisa tipe data apa saja

mahasiswa = {
    "nama" : "daffa",
    "npm"  : "045406484",
    2:"khalis",
    "mk": ["mkpk","mku"]


}
print(mahasiswa)

#mengakses data pada dictionary

print(mahasiswa["npm"])
print(mahasiswa["nama"])
print(mahasiswa[2])
#print(mahasiswa["tidak ada"]) # bakalan error karena tidak ada di dictionary


# mengakses data menggunakan get()

print(mahasiswa.get("npm"))
print(mahasiswa.get("negara"))
print(mahasiswa.get("kota","tidak ada kota"))
print("kota" in mahasiswa)

# mengubah data pada dictionary
mahasiswa = {
    "nama":"daffa",
    "umur": 10

}
mahasiswa["umur"] = 18
print(mahasiswa)

# menambah data pada dictionary
kucing = {
    "nama": "meong"
}

# cara pertama
print(kucing)
kucing["warna"] = "hitam"
print(kucing)

# cara dua
kucing.update({"kaki":4,"umur":3})


#menghapus data pada dictionary
kucing = {
    "nama": "meong",
    "umur":4
}
print(kucing)
dihapus = kucing.pop("umur")
print(dihapus)
print(kucing)


#menghapus data pada dictionary menggunakan del dan clear
kucing = {
    "nama": "meong",
    "umur":4
}
print(kucing)
del kucing["nama"]
print(kucing)

kucing.clear()
print(kucing)

# for loop dictionary
# yang dikembalikan itu adalah key nya

mahasiswa = {
     "nama" : "daffa",
     "npm"  : "045406484",
     "umur" : 18,
     "alamat": "sigli"

    
}

for kunci in mahasiswa:
    print(kunci,mahasiswa[kunci])

#for-loop dictionary 2

mahasiswa = {
     "nama" : "daffa",
     "npm"  : "045406484",
     "umur" : 18,
     "alamat": "sigli"}

for kunci,nilai in mahasiswa.items():
    print(kunci,nilai)

print(list(mahasiswa.items()))
print(list(mahasiswa.keys()))
print(list(mahasiswa.values()))



# latihan
harga_barang = {
    "mesin cuci":2000000,
    "laptop":10000000

}

total = 0
for kunci,nilai in harga_barang.items():
    total = total + nilai # memperbaharui nilai total dengan cara ditambah dengan nilai

print(f"total:{total:,}") #:, untuk memberi tanda pada angka yang dimasukkan 