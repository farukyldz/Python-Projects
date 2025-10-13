print("""
  Listing the even numbers between 1 and 100.
  
""")

list=[]

for i in range(1,101):
    if i%2==0:
       list.append(i)

print(list)