import sys

sys.stdout.write("Sysout ile yazdırıldı\n")

sys.stderr.write("StdErr ile Hata Yazdırıldı\n")
sys.stderr.flush()

print(sys.argv)#argv yapısını konsoldan uygulamaya parametre göndermek için kullanıyoruz.

for i in sys.argv:
    print(i)