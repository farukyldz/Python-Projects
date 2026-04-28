import random;
target_number=random.randint(1, 100);
target_count=0;

while True:
    target=int(input("Please enter a number between 1 and 100: "));
    target_count+=1;
    if target==target_number:
        print(f"Well done, {target_count} you got it right  times");
        break;
    elif target<target_number:
        print("Try to guess a larger number");
    else:
        print("Try to guess a smaller number");
        