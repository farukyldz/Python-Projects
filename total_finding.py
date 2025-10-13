print("""
*************************
      Find the total number entered until the user exits the programme
      Press q to exit
*************************      
""")
total=0

while True:
    number=input("number:")
    if number=="q":
        print("Logging out..")
        break

    else:
        number=int(number)
        total +=number

print("The sum of the numbers you entered:",total)
