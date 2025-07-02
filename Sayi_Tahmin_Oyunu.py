
import random

random=random.randint(1,20)
sayi=int (input("Bir sayı tahmin ediniz:"))
Skor=5
while Skor>0:
    if random==sayi:
        print("Sayıyı doğru tahmin ettiniz :)",Skor)
        break

    else:
        print("Sayıyı doğru tahmin edemediniz :(,Skorunuz:",Skor)
        Skor=Skor-1
        sayi=int (input("Bir sayı tahmin ediniz:"))
        
        

