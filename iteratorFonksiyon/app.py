class iteratorFonk():
    def __init__(self, max=0):
        self.max=max
        self.kuvvet=0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.kuvvet<=self.max):
            sonuc=3**self.kuvvet
            self.kuvvet+=1
            return sonuc
        else:
            self.kuvvet=0
            raise StopIteration


kuvvet=iteratorFonk(5)
iterator=iter(kuvvet)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

kuvvet2=iteratorFonk(5)
print("""
*** 1. for döngsü ile ***
""")
for i in kuvvet2:
    print(i)

print("""
*** 2. for döngsü ile ***
""")
for i in kuvvet2:
    print(i)
