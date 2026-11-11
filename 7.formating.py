#formatting :6.2f
# : menangkap format
# 6 menandakana ada 6 space yang disediakan
# .2f menandakan 2 angka dibelakang koma
# , untuk menandakan pemisah ribuan
# tipe data float = angka desimal
# 3.14159 = ingat bahasa pemogramaman pakai titik

angka = 3.14159
print(f"{angka:.2f}")
print(f"[{angka:6.2f}]")
print(f"[{angka:<6.2f}]")

uang = 1000000
print(f"uang saya sebanyak Rp.{uang:,}")

