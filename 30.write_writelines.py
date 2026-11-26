#write()= digunakan untuk menulis ke file
#writelines()= digunakan untuk menulis beberapa data ke file

with open("data/catatan2.txt", "w") as f:
    f.write("data terbaru\n")
    f.writelines(["data terbaru lagi\n","data paling baru\n"])

    