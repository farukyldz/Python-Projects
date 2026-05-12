print("""
*********************
   Factorial calculation programme
   
   Press q to exit. 
**********************   
""")

while True:
    num = input("number: ")

    if num == "q":
        print("The programme is coming to an end...")
        break
    else:
        num = int(num)
        factorial = 1
        for i in range(2, num + 1):
            factorial *= i

        print("Factorial:", factorial)
