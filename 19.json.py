import json # memanggil module json

#json
#javascript object notation


#mengubah json ke dalam bentuk dictionary

data_json = '{"nama": "daffa","umur":18}'
print(type(data_json))

data_python = json.loads(data_json) #mengubah dari tipe data json ke dictionary
print(data_json)
print(type(data_python))


# untuk mengakses,menghapus dan sebagainya sama seperti dictionary
print(data_python["nama"])
print(data_python["umur"])


#mengubah dari tipe data python ke json
#dumps(nama variabel yang mau dikonfersi)

data = {
    'nama':'daffa',
    'umur':'18',
    'matpel': ['matematika','fisika'],
    'menikah': False,
    'anak': None
}

data_json = json.dumps(data)# dumps() digunakan untuk mengubah dictionary ke dalam bentuk json
print(data_json)
print(type(data_json))

#merapikan menggunakan indent=4, sort_keys=4
data_json = json.dumps(data,indent=4, sort_keys=True)# dumps() digunakan untuk mengubah dictionary ke dalam bentuk json
print(data_json)
print(type(data_json))


#latihan json 
import json # memanggil module json

teks = '{"nama":"dafa","umur":20}'
data = json.loads(teks)# mengubah dari json ke dictionary python

data["umur"] = 18 # mengubah
data["hobi"] = ["main bola"] #menambahkan
del data["nama"] # menghapus 

print(json.dumps(data,indent=4)) # mengubah dari dictionary python ke json
