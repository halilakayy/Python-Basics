import sqlite3

baglanti=sqlite3.connect("kutuphane.db")
imlec=baglanti.cursor()
imlec.execute("create table if not exists kitaplik (isim text, yazar text, yayinEvi text, sayfa int)")
baglanti.commit()

def veriEkle():
    print("""
    ******************************
    Veritabanına Veri Ekle
    ******************************
    """)
    isim=input("İsim: ")
    yazar=input("Yazar: ")
    yayinEvi=input("Yayın Evi: ")
    sayfa=int(input("Sayfa Sayısı:"))
    imlec.execute("insert into kitaplik values(?, ?, ?, ?)", (isim, yazar, yayinEvi, sayfa))
    baglanti.commit()

def veriOku():
    print("""
    ******************************
    Okunan Verile
    ******************************
    """)
    imlec.execute("select * from kitaplik")
    veri=imlec.fetchall()
    for oku in veri:
        print(oku)


veriOku()
baglanti.close()