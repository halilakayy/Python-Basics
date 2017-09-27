Datetime nesnesini kullanarak takvim yapma
24 saatin kaç saniye olduğunu hesaplayıp Datetime nesnesinin timestamp ve fromtimestamp 
fonksiyonlarını kullanarak ileriye veya geriye sarma yapmak için saniye ekleme ve çıkarma yapılabilir.

1 gün = 24 saat = 1440 dakika = 86400 saniye
Kullanımı:
bugun=datetime.timestamp(datetime.now)
yarin=bugun+86400
dun=bugun-86400

Kaç gün geriye veya ileriye gidilecekse saniye o kadarı ile çarpılıp toplanır veya çıkarılır.
Ardından fromtimestamp metodu ile normal tarihe çevirilir.