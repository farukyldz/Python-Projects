import random
Liste=["Taş","Kağıt","Makas"]
pc=random.choice(Liste)
player=input("[Taş,Kağıt,Makas]").capitalize()

print("Bilgisayar",pc,"üretti sen",player,"ürettin")



if pc==player:
    print("Berabere")


if pc=="Taş" and player=="Makas":
    print("Kaybettiniz..")

if pc=="Kağıt" and player=="Taş":
    print("Kaybettiniz..")

if pc=="Makas" and player=="Kağıt":
    print("Kaybettiniz..")



if pc=="Makas" and player=="Taş":
    print("Kazandınız..")

if pc=="Taş" and player=="Kağıt":
    print("Kazandınız..")

if pc=="Kağıt" and player=="Makas":
    print("Kazandınız..")    

else:
    print("Liste dışı seçim yaptınız.")