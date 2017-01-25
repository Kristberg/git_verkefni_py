#Kristberg Rúnar Pálsson
#25.1.2017
#Dæmi 1
tala1 = int(input("Sláðu inn tölu "))
tala2 = int(input("Sláðu inn aðra tölu "))
summa = tala1 + tala2
margf = tala1 * tala2
print("Tölurnar lagðar saman eru:", summa)
print("Tölurnar margfaldaðar saman eru:", margf)

fornafn = input("Sláðu inn fornafn")
eftirnafn = input("Sláðu inn eftirnafn")
print("Halló",fornafn, eftirnafn)

texti=input("Sláðu inn texta: ")
hastafur=0
lagstafur=0
for e in texti:
    if e.isalpha():
        if e.isupper():
            hastafur=hastafur+1
        if not e.isupper():
            lagstafur=lagstafur+1
print("Í þessum texta eru",hastafur,"hástafir og",lagstafur,"lágstafir")