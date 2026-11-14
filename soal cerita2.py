harga_kopi = 15000
saldo_Vito = int(input("saldo"))
mesin_rusak = False

# Logika
if saldo_Vito >= harga_kopi and  (not mesin_rusak):
    print ('Kopi Keluar')
    saldo_Vito = saldo_Vito - harga_kopi
elif saldo_Vito <= harga_kopi or mesin_rusak:
    print ("maaf, mesin rusak,saldo tidak di potong")
elif saldo_Vito >= 0 and saldo_Vito < harga_kopi:
    kurang = hargakopi - saldo_Vito
    print ("saldo kurang Rp",kurang)
else:
    print("EROR MAS")