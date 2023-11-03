def main():
    koltuklar = [False] * 10  # 10 koltuklu bir uçak

    while True:
        # Kullanıcıya seçenekleri göster
        print("Lütfen aşağıdaki seçeneklerden birini seçin:")
        print("1. Boş koltukları göster")
        print("2. Koltuk rezervasyonu yap")
        print("3. Rezervasyonu iptal et")
        print("4. Çıkış")

        secim = int(input())  # Kullanıcının seçimini al

        if secim == 1:
            bos_koltuklari_goster(koltuklar)
        elif secim == 2:
            rezervasyon_yap(koltuklar)
        elif secim == 3:
            rezervasyon_iptal_et(koltuklar)
        elif secim == 4:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

def bos_koltuklari_goster(koltuklar):
    print("Boş koltuklar:")
    for i in range(len(koltuklar)):
        if not koltuklar[i]:
            print("Koltuk " + str(i + 1))

def rezervasyon_yap(koltuklar):
    koltuk_no = int(input("Rezervasyon yapmak istediğiniz koltuğun numarasını girin: "))
    
    if koltuk_no < 1 or koltuk_no > len(koltuklar):
        print("Geçersiz koltuk numarası. Lütfen tekrar deneyin.")
    elif koltuklar[koltuk_no - 1]:
        print("Bu koltuk zaten rezerve edilmiş.")
    else:
        koltuklar[koltuk_no - 1] = True
        print("Rezervasyon tamamlandı. Koltuk " + str(koltuk_no) + " sizin.")

def rezervasyon_iptal_et(koltuklar):
    koltuk_no = int(input("Rezervasyonu iptal etmek istediğiniz koltuğun numarasını girin: "))
    
    if koltuk_no < 1 or koltuk_no > len(koltuklar):
        print("Geçersiz koltuk numarası. Lütfen tekrar deneyin.")
    elif not koltuklar[koltuk_no - 1]:
        print("Bu koltuk zaten boş.")
    else:
        koltuklar[koltuk_no - 1] = False
        print("Rezervasyon iptal edildi. Koltuk " + str(koltuk_no) + " boş.")
main()
