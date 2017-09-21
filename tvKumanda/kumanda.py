import time

class tvKumanda:
    def __init__(self, tvDurum="Kapalı", tvSes=0, kanalListe=["TRT"], tvKanal="TRT"):
        self.tvDurum=tvDurum
        self.tvSes=tvSes
        self.kanalListe=kanalListe
        self.tvKanal=tvKanal

    def tvAc(self):
        if(self.tvDurum=="Açık"):
            print("Tv zaten açık")
        else:
            self.tvDurum="Açık"
            print("Tv Açıldı!")
    def tvKapat(self):
        if(self.tvDurum=="Kapalı"):
            print("Tv zaten kapalı")
        else:
            self.tvDurum="Kapalı"
            print("Tv Kapandı")

    def sesAyarlari(self):
        while True:
            dugme=input("[>]: Ses Arttır \n[<]: Ses Azalt \n[q]: Çıkış\n Düğme:")
            if(dugme=="q"):
                print("Güncel Ses: {}".format(self.tvSes))
                break
            elif(dugme==">"):
                self.tvSes+=1
                print("Ses: {}".format(self.tvSes))
            elif(dugme=="<"):
                self.tvSes-=1
                print("Ses: {}".format(self.tvSes))

    def kanalEkle(self):
        kanallar=input("Kanalları ',' ile ayırarak yazın: ")
        yeniKanal=kanallar.split(",")
        for ekleKanal in yeniKanal:
            print("{} Kanalı Eklendi".format(ekleKanal))
            self.kanalListe.append(ekleKanal)

    def kanalGez(self):
        
        while True:
            dugme=input("[+]:Sonraki Kanal \n[-]:Önceki Kanal \n[q]: Çıkış \nDüğme: ")
            kanalId=self.kanalListe.index(self.tvKanal)
            if(dugme=="q"):
                break
            elif(dugme=="+"):
                print("Sonraki kanala geçiliyor...")
                time.sleep(1)
                if(kanalId==len(self.kanalListe)-1):
                    self.tvKanal=self.kanalListe[0]
                    print("Aktif Kanal: {}".format(self.tvKanal))
                else:
                    self.tvKanal=self.kanalListe[kanalId+1]
                    print("Aktif Kanal: {}".format(self.tvKanal))
            elif(dugme=="-"):
                print("Önceki kanala geçiliyor...")
                time.sleep(1)
    
                if(kanalId==0):
                   self.tvKanal=self.kanalListe[len(self.kanalListe)-1]
                   print("Aktif Kanal: {}".format(self.tvKanal))
                else:
                    self.tvKanal=self.kanalListe[kanalId-1]
                    print("Aktif Kanal: {}".format(self.tvKanal))
                
    def __str__(self):
        return "Tv Durumu: {} \nSes Bilgisi: {} \nKanal listesi: {} \nAktif Kanal: {}".format(self.tvDurum, self.tvSes, self.kanalListe, self.tvKanal)

    def __len__(self):
        return len(self.kanalListe)