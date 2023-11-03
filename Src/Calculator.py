def main():
    print("Basit Hesap Makinesi")
    islem_turu = input("İşlem seçin (+, -, *, /): ")

    if islem_turu not in ['+', '-', '*', '/']:
        print("Geçersiz işlem.")
        return

    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    sonuc = 0

    if islem_turu == '/':
        if sayi2 != 0:
            bolme = sayi1 / sayi2
            print("Sonuç:", bolme)
        else:
            print("Hata: Sıfıra bölme hatası!")
    elif islem_turu == '+':
        sonuc = sayi1 + sayi2
        print("Sonuç:", sonuc)
    elif islem_turu == '-':
        sonuc = sayi1 - sayi2
        print("Sonuç:", sonuc)
    elif islem_turu == '*':
        sonuc = sayi1 * sayi2
        print("Sonuç:", sonuc)
main()
