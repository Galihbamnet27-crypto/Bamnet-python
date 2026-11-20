# list kosong
daftar_kosong = []

# list dengan angka
angka = [1, 2, 3, 4, 5]
angka.append(6)
angka.append(7)
angka.append(8)
angka.append(9)
angka.remove(2)
angka.pop()
del angka[3]
print(len(angka))
print(angka)

# list dengan string
nama = ["galih", "aul", "iqbal", "titis", "maul", "jibran"]
nama.append("vito")
nama.remove("vito")
del nama[3]
print(len(nama))


# list campuran 
anggota_bamnet = [12, "jibran", 11, "aul", 10, "galih"]
print(nama)
print(anggota_bamnet)

buah1 = ["durian", "apel", "mangga"]
buah2 = ["kelengkeng", "pir", "pepaya"]
buah_doang = buah1 + buah2
print (buah_doang)

# mengunakan for lop
print("daftar buah:")
for item in buah_doang:
    print("-", item)