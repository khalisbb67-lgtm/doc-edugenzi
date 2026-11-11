# if else adalah percabangan di bahasa pemrograman python
# kondisi if jika memenuhi syarat maka akan menjalankan perintah di dalam if
# kondisi else jika tidak memenuhi syarat maka akan menjalankan perintah di dalam else

# untuk pengecekan kita bisa pakai
# == untuk sama dengan 
# != untuk tidak sama dengan
# > untuk lebih besar dari
# < untuk lebih kecil dari
# >= untuk lebih besar dari atau sama dengan
# <= untuk lebih kecil dari atau sama dengan

nilai = 80
def ujian_akhir(nilai):
    
    if nilai >= 75:
        return "Anda lulus"
    elif nilai >=70:
        return "Anda lulus dengan baik"
    elif nilai <=50:
        return "Anda tidak lulus dengan baik"
    else:
        return "Anda tidak lulus"

hasil = ujian_akhir(80)
print(hasil)

