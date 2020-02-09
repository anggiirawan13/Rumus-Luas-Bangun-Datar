while True:

    def luasPersegi(s1, s2):
        return float(s1 * s2)

    def luasPersegiPanjang(p, l):
        return float(p * l)

    def luasSegitiga(a, t):
        return float(a * t / 2)

    def luasLingkaran(r):
        return float(3.14 * r * r)


    print(" ")
    print("   ________           ww      ww            _________                  ")
    print("  /  _____/          /  \    /  \          /   _____/   ____    ____   ")
    print(" /   \  ___   ______ \   \/\/   /  ______  \_____  \  _/ __ \ _/ ___\  ")
    print(" \    \g\  \ /_____/  \        /  /_____/  /        \ \  ___/ \  \___  ")
    print("  \______  /           \  /\  /           /_______  /  \___  e \___  c ")
    print("         \/             \/  \/                    ss       \/      \/  ")
    print(" ")

    print('=' * 100)
    print('PILIHAN RUMUS LUAS BANGUN DATAR')
    print('\t 1. Luas Persegi')
    print('\t 2. Luas Persegi Panjang')
    print('\t 3. Luas Segitiga')
    print('\t 4. Luas Lingkaran')
    print('=' * 100)

    userInput = input('Masukan Pilihan Anda (1/2/3/4) : ')

    if userInput == '1':
        nilai1 = float(input('Masukan Nilai Sisi Pertama : '))
        nilai2 = float(input('Masukan Nilai Sisi Kedua : '))
        print('Luas Persegi',nilai1,'x',nilai2,'=',luasPersegi(nilai1, nilai2))

    elif userInput == '2':
        nilai1 = float(input('Masukan Nilai Panjang : '))
        nilai2 = float(input('Masukan Nilai Lebar : '))
        print('Luas Persegi Panjang',nilai1,'x',nilai2,'=',luasPersegiPanjang(nilai1, nilai2))

    elif userInput == '3':
        nilai1 = float(input('Masukan Nilai Alas : '))
        nilai2 = float(input('Masukan Nilai Tinggi : '))
        print('Luas Segitiga 1/2 x',nilai1,'x',nilai2,'=',luasSegitiga(nilai1, nilai2))

    elif userInput == '4':
        nilaiR = float(input('Masukan Nilai Jari-Jari : '))
        print('Luas Lingkaran 3,14 x',nilaiR,'x',nilaiR,'=',luasLingkaran(nilaiR))

    else:
        print('=' * 100)
        print('Kata Kunci Yang Anda Masukan Salah.')
        break

    print('=' * 100)
    userAgain = input('Apakah Anda Ingin Menghitung Lagi ? ( y / n ) : ')
    if userAgain == 'y':
        continue
    elif userAgain == 'n':
        break
    else:
        print('=' * 100)
        print('Kata Kunci Yang Anda Masukan Salah.')
        break
print('=' * 100)
print('TERIMA KASIH')