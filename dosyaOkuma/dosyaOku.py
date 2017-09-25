
with open("dosya.txt", "w", encoding="utf-8") as dosyaYaz:
    dosyaYaz.write("Python, Java, PHP, C#, C++")

with open("dosya.txt", "r", encoding="utf-8") as dosyaOku:
    metin= dosyaOku.read()
    print(dosyaOku.tell())
    dosyaOku.seek(0)
    liste=dosyaOku.readlines()

print(metin)
print(liste)
sozluk={"s1":"1", "s2":2}
for key, value in sozluk.items():
    print("Key={} -> {}".format(key,value))
