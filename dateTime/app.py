from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")
print(datetime.now().strftime("%D"))
print(datetime.now().strftime("%d %B %Y"))
print(locale.setlocale(locale.LC_ALL, ""))

tarih=datetime.now()

saniye=datetime.timestamp(tarih)
normal=datetime.fromtimestamp(saniye)

print("""
*********************************************
Zaman İşlemleri
*********************************************
""")

sonrakiGun=saniye+(24*60*60)
oncekiGun=saniye-(24*60*60)
print("Önceki Gün: {} \nSonraki Gün: {}".format(datetime.fromtimestamp(oncekiGun).strftime("%d %B %Y"), datetime.fromtimestamp(sonrakiGun).strftime("%d %B %Y")))









