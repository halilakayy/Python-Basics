import moduller

newModul=moduller.yeniModel(10,3)
say=newModul.sayiUret()
print(say)


while True:
    giris=input("Şifre Girin: ")
    sifre=""
    for i in newModul.sifrele(giris):
        sifre+=str(i)
    print("Şifre: {}".format(sifre))
