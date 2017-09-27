import random
import time

class yeniModel():
    def __init__(self, sayi, zaman):
        print("init Fonksiyonu Çağrıldı")
        self.sayi=sayi
        self.zaman=zaman

    def sayiUret(self):
        sayi=random.randint(1,40)
        return sayi

    def zamanlayici(self):
        time.sleep(3)

    
    def sifrele(self, sifre):
         self.sifre=sifre
         a=[random.randint(0,9), random.randint(0,9), random.randint(0,9)]
         b=[random.randint(10,19), random.randint(10,19), random.randint(10,19)]
         c=[random.randint(20,29), random.randint(20,29), random.randint(20,29)]
       
         sifreli=list()
         for i in self.sifre:
            if(i=="a"):
                sifreli+=a
            elif(i=="b"):
                sifreli+=b
            elif(i=="c"):
               sifreli+=c
            else:
                sifreli+=i
         return sifreli
    

    def sifreCoz(self, sifre):
        self.sifre=sifre
        