def main():
    # Kullanıcıdan veri almak için bir input kullan
    okul_turu = input("Lise mi (L) yoksa Üniversite mi (Ü) okuyorsunuz? (L/Ü): ")

    # Toplam ders sayısını öğren
    toplam_ders_sayisi = int(input("Toplam ders sayısını girin: "))

    # Sınıf geçme notunu öğren
    sinif_gecme_notu = float(input("Sınıf geçme notunu girin: "))

    # Toplam not değerini saklamak için bir değişken tanımla (float) ve kalan ders sayısını saklamak için bir değişken tanımla (int)
    toplam_not = 0
    kalan_ders_sayisi = 0

    # Girilen ders sayısına göre ders notlarını al ve toplam nota ekle
    for i in range(1, toplam_ders_sayisi + 1):
        ders_notu = float(input(f"Ders {i} notunu girin: "))
        toplam_not += ders_notu

        # Ders notu sınıf geçme notundan düşükse, kalan ders sayısını artır
        if ders_notu < sinif_gecme_notu:
            kalan_ders_sayisi += 1

    # Ortalama notu hesapla
    ortalama_not = toplam_not / toplam_ders_sayisi
    print("Ortalama Not:", ortalama_not)
    print("Başarılı Ders Sayısı:", toplam_ders_sayisi - kalan_ders_sayisi)
    print("Kalan Ders Sayısı:", kalan_ders_sayisi)

    # Mantıksal işlem: Kullanıcının okul türüne ve başarı durumuna göre mesaj ver
    if okul_turu.upper() == "L":  # Lise
        if kalan_ders_sayisi > 3 or ortalama_not < 55:
            print("Sınıfta kaldınız!")
        else:
            print("Sınıfı geçtiniz!")
    elif okul_turu.upper() == "Ü":  # Üniversite
        if kalan_ders_sayisi > 2 or ortalama_not < 60:
            print("Sınıfta kaldınız!")
        else:
            print("Sınıfı geçtiniz!")
    else:
        print("Geçersiz okul türü seçimi.")
main()
