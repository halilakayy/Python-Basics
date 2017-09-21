import kumanda

kumanda=kumanda.tvKumanda()
print("""
    **********************************
    1. Tv Aç
    2. Tv Kapat
    3. Ses Ayarla
    4. Kanal Değiştir
    5. Genel Bilgi
    6. Kanal Sayısı
    7. Kanal Ekle
    8. Çıkış
    **********************************
    """)
while True:
    
    dugme=input("Seçim Yapın: ")
    if(dugme=="8"):
        break
    elif(dugme=="1"):
        kumanda.tvAc()
    elif(dugme=="2"):
        kumanda.tvKapat()
    elif(dugme=="3"):
        kumanda.sesAyarlari()
    elif(dugme=="4"):
        kumanda.kanalGez()
    elif(dugme=="5"):
        print(kumanda)
    elif(dugme=="6"):
        len(kumanda)
    elif(dugme=="7"):
        kumanda.kanalEkle()
    else:
        print("Geçersiz Seçim!")