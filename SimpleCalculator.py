num1=int(input("Enter the first number: "));
num2=int(input("Enter the second number: "));
transaction = input("Select an operation (+, -, *, /): ");
if transaction == "+":
    print("result:", num1 + num2);
elif transaction == "-":
    print("result:", num1 - num2);
elif transaction == "*":
    print("result:", num1 * num2);
elif transaction == "/":
    if num2 != 0:
        print("result:", num1 / num2);
    else:
        print("A number cannot be divided by zero.");
else:
    print("invalid transaction");    
    