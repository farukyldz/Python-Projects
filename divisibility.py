print("""
    Find the numbers between 1 and 100 that are only divisible by 3.
    
""")


for i in range(1,101):
    if i%3==0:
        print(i, end = " ")
