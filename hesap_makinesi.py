print(""" ***************************
          Hesap Makinesi Programı
1.Toplama İşlemi

2.Çıkarma İşlemi

3.Çarpma İşlemi

4.Bölme İşlemi


************************""")

a=int(input("Birinci Sayıyı Giriniz:"))
b=int(input("İkinci Sayıyı Giriniz:"))

islem = input("İşlemi Giriniz:")

if islem== "1":
    print("{} ile {} in toplamı {} dir.".format(a,b,a+b))

elif islem == "2":
    print("{} ile {} in farkı {} dir.".format(a, b, a - b))
elif islem == "3":
    print("{} ile {} in çarpımı {} dir.".format(a, b, a * b))
elif islem == "4":
    if b==0:
        print("0'a bölünme hatası !!")

    else:
        print("{} ile {} in bölümü {} dir.".format(a, b, a / b))

else:
    print("Geçersiz işlem girdiniz,Tekrar Deneyiniz.")
