
import random
import string

def sifre_olustur(uzunluk):
    karakterler = string.ascii_letters + string.digits + '!@#$%^&*()-_=+'
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre
def main():
    uzunluk = int(input("Şifre uzunluğunu girin: "))
    sifre = sifre_olustur(uzunluk)
    print("Oluşturulan şifre:", sifre)
main()
