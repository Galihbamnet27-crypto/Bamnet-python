angka = 1
while angka <=5:
    print(angka)
    angka += 1

password = ""
while password != "123456":
    password = input ("masukkan password: ")
    if password != "123456":
        print("password salah, coba lagi")

print("passwod benar")