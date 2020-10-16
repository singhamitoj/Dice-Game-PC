# Dice Game Demo v1.0
import time
import random

numlist = [1, 2, 3, 4, 5, 6]

def roll(int):
    for x in range(1, int):
        random.choice(numlist)

print("Welcome to Dice Game PC Edition Demo Version!")

# intro = input("Do you want to read the introduction? (Type y or n)")
# if intro == "y":
#    print("Okay!")
#    time.sleep(1)
#    print("Error: nothing stored.")

time.sleep(1)
rollind = input("How many times do you want to roll the dice? (1-3)")
if rollind == "1":
    print(roll(1))

elif rollind == "2":
    print(roll(2))

elif rollind == "3":
    print(roll(3))

    
print("Successfully outputted!")
time.sleep(1.5)
print("Please look at our original Sololearn Edition, and stay tuned for the full version of the PC edition of Dice game!")
time.sleep(8.5)
print("Bye!")
time.sleep(0.3)
exit()
