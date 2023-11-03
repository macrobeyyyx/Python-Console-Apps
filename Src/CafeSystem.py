def main():
    # Ürün bilgilerini ve siparişleri saklamak için sözlükleri tanımla
    urunler = {
        "Çay": 2.0,
        "Kahve": 3.0,
        "Sandviç": 5.0,
        "Meyve Suyu": 4.0,
    }
    siparisler = {}

    # Sonsuz bir döngü oluştur ve kullanıcının işlemlerini seçmesini sağla
    devam_et = True
    while devam_et:
        # Kullanıcıya mevcut ürünleri göster
        print("Kantin Ürünleri:")
        for urun, fiyat in urunler.items():
            print(f"{urun} - {fiyat} TL")

        # Kullanıcıya işlem seçeneklerini göster
        print("Lütfen bir işlem seçin:")
        print("1. Ürün Satın Alma")
        print("2. Sipariş Geçmişi Görüntüle")
        print("3. Çıkış")

        # Kullanıcının seçimini al
        secim = input()
        if secim.isdigit():
            secim = int(secim)
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")
            continue

        # Kullanıcının seçimine göre işlem yap
        if secim == 1:
            urun_satin_al(urunler, siparisler)
        elif secim == 2:
            siparis_gecmisi_goruntule(siparisler)
        elif secim == 3:
            print("Çıkış yapılıyor...")
            devam_et = False
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

def urun_satin_al(urunler, siparisler):
    urun = input("Satın almak istediğiniz ürünü seçin: ")

    if urun in urunler:
        adet = int(input("Kaç adet almak istiyorsunuz: "))

        toplam_fiyat = urunler[urun] * adet

        if urun in siparisler:
            siparisler[urun] += adet
        else:
            siparisler[urun] = adet

        print(f"Siparişiniz alındı. Toplam Tutar: {toplam_fiyat} TL")
    else:
        print("Geçersiz ürün seçimi.")

def siparis_gecmisi_goruntule(siparisler):
    print("Sipariş Geçmişi:")
    for urun, adet in siparisler.items():
        print(f"{urun} - {adet} adet")
main()
