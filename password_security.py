password=input("Please enter your password:");
capital_letter=False;
lowercase=False;
special_character=False;
number=False;    


for character in password:
        if character.isupper():
            capital_letter=True;
        elif character.islower():
            lowercase=True;
        elif character.isdigit():
            number=True;
        elif character in "!@#$%^&*()_+":
            special_character=True;


if len(password)>=8:
     if capital_letter and lowercase and special_character and number:
        print("The password is strong");
     else:
        print("The password is not strong")
        
        
        
        
        
        
        
        
        