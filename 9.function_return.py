# function dengan return itu adalah function yang bisa mengembalikan nilai
#return itu adalah kata kunci yang digunakan untuk mengembalikan nilai dari function
#function jika tidak memiliki return maka function itu akan mengembalikan nilai None


def luas_persegi_panjang(panjang,lebar):
    luas = panjang * lebar
    print(f"operasi selesai")
    return luas

hasil = luas_persegi_panjang(10,5)
print(hasil)