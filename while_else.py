pw_benar = "123456"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    pw = input("masukkan pw")
    percobaan += 1

    if pw == pw_benar:
        print("login berhasil")
        break
    else:
        print("pw salah. sisa percobaan:", max_percobaan - percobaan)
else:
    print("wah hacker ya lu")