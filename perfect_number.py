print("""
****************************
    If the sum of a number's divisors (excluding the number itself) equals the number itself,
     it is called a ‘perfect number’. For example, 6 is a perfect number. (1 + 2 + 3 = 6)
****************************     
""")

sayi=int(input("Please enter a number:"))
toplam=0
for i in range(1,sayi):
    if sayi%i ==0:
        toplam=toplam+i
if toplam==sayi:
    print("Perfect Number")
else:
    print("Not a perfect number")