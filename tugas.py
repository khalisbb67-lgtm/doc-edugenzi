def perkenalan(nama,umur):
    print(f"nama saya {nama},saya berumur {umur}")


perkenalan("daffa khalis","18")  

def luas_persegi_panjang(p,l):
    luas = p * l
    print(f"{luas}")
    return luas

luas = luas_persegi_panjang(4,5)

nilai = 100

def cek_nilai(nilai):
    if nilai >= 80:
        return "lulus"
    
    elif nilai <= 70:
        return "belum lulus"

hasil = cek_nilai(80)
print(hasil)
