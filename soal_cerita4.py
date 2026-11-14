ban_berjalan = ("kertas","batu","plastil","bom","plastik","kertas")
sampah_terproses = 0

for barang in ban_berjalan:
    if barang == "batu":
        print("mendeteksi batu,lewati")
    elif barang == "bom":
        print("awas woi")

    print ("memproses", barang)
    sampah_terproses += 1
print("total sampah di proses: ", sampah_terproses) # isi total sampah yang di proses oleh robot