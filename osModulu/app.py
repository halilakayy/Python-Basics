import os

klasor=os.listdir()

for i in klasor:
    print(i)

print("""
*****************************************
Klasör ve  Dosya Listeleme
*****************************************
""")

for klasor_liste, klasor_ad, dosya_ad in os.walk("C:/Users/AKAY/PycharmProjects/gitHub/pythonProejct"):
    print(klasor_liste)
    print(klasor_ad)
    print(dosya_ad)
    print("**********************************************")