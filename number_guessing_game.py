import numpy as np
print("Welcome to the Game")
print("1.Play Game",
      "\n" "2.View rules",
      "\n" "3.Exit")
try:
       choice = int(input("Enter your choice: "))
       if(choice<0 or choice>3):
           print("Invalid.Input must be 1,2 or 3")
except ValueError:
        print("Invalid.Input must be 1,2 or 3")
score=0
while True:
    if (choice == 1):
        print("Pick 3 numbers between 1 and 10")
        while True:
            x = int(input("Enter first number:"))
            y = int(input("Enter second number:"))
            z = int(input("Enter third number:"))
            nums = [x, y, z]
            if any(num < 1 or num > 10 for num in nums):
                print("invalid input, all numbers must be between 1 and 10")
                continue
            if (len(set(nums)) < 3):
                print("duplicate inputs")
                continue
            print("valid input. Proceeding with the game")
            break
        a = np.arange(1, 11)
        b = np.random.choice(a, 3, replace=False)
        print("system drew: ", b)
        common_elements = set(nums).intersection(set(b))
        if (len(common_elements) >= 2):
            print("you have won")
            score=score+1
        else:
            print("better luck next time")
        print("a.Play again", "\n" "b.See Score","\n""c.Exit")
        i = input("choose next: ")
        if (i == "a"):
            continue
        elif(i=="b"):
            print(score)
        elif(i=="c"):
            print("Thank you, visit again")
            break
    elif (choice == 2):
        print("Pick 3 numbers between 1 and 10"
              "\n3 numbers are drawn by system"
              "\nMatch 2 or more to win prizes")
    elif (choice == 3):
        print("Thank you, visit again")
        break
