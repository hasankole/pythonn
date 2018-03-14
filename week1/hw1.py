# week1

for x in range(3):
        s1=int(input("sayi gir : "))
        s2=int(input("sayi gir : "))
        a=0
        print("Toplama Islemi(+)")
        print("Cikarma Islemi(-)")
        print("Bolme   Islemi(/)")
        print("Carpma  Islemi(*)")
        islem=input("islem : ")
        if islem == "+" :
            a=s1+s2

            print("sonuc", a)
        elif islem=="-":
            a=s1-s2
            print("sonuc",a)
        elif islem=="*":
            a=s1*s2
            print("sonuc",a)
        elif islem=="/":
            a=s1/s2
            print("sonuc",a)
