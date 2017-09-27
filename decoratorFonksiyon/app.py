import time
def zamanHesapla(func):
    def uygula(sayilar):
        baslama=time.time()
        sonuc=func(sayilar)
        bitis=time.time()

        print(func.__name__+" fonksiyonunun çalışması "+str(bitis-baslama)+" saniye sürdü")
        return sonuc
    return uygula

@zamanHesapla
def kareHesapla(sayilar):
    sonuc=list()
    for i in sayilar:
        sonuc.append(i**2)
    return sonuc

kareHesapla(range(1,1000000))

#raise "Hata Fırlatıldı mı?"