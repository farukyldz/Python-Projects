print("------------Calculating the grade point average:-----------------------")
midterm = float(input("Please enter your midterm: "))
final = float(input("Please enter your final: "))

average = (midterm * 0.4) + (final * 0.6)

if average >= 50:
    print("Pass")
else:
    print("Fail")

print(f"Your average grade: {average}")
print("--------------------------------")