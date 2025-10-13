print("""*********************
        ARMSTRONG NUMBER FINDING
**********************
           """)

number=input("number:")
number_of_steps=len(number)
number=int(number)
total=0
step=0

temp_number=number
while temp_number>0:
    step = temp_number % 10
    total += step ** number_of_steps

    temp_number //= 10

if number==total:
    print("Armstrong number")
else:
    print("Armstrong is not a number")


