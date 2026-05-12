print(""" ***************************
          Calculator Programme
1. Addition

2. Subtraction

3. Multiplication

4. Division


************************""")

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

transaction = input("İşlemi Giriniz:")

if transaction== "1":
    print("The sum of {} and {} is {}.".format(a,b,a+b))

elif transaction == "2":
    print("The difference between {} and {} is {}.".format(a, b, a - b))
elif transaction == "3":
    print("The product of {} and {} is {}.".format(a, b, a * b))
elif transaction == "4":
    if b==0:
        print("Division by zero error !!")

    else:
        print("{} ile {} in bölümü {} dir.".format(a, b, a / b))

else:
    print("You have entered an invalid transaction. Please try again..")
