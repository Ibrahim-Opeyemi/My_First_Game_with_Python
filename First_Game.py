# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 03:08:10 2021

@author: Green_Phalajish
"""

print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name + ", " "you are", age, "years old.")
print("Hello {}, you are {} years old.".format(name, age))

health = 10

if age >= 18:
    print("You are old enough to play!")
    
    weapon = input("Pick a weapon (sword/knife): ").lower()
    
    if weapon == "sword":
        print("You're ready to go")
    else:
        print("Your weapon is not strong enough for the journey. Meanwhile, you ought to be careful")
    
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health")
        print("Let's play!")
        
        left_or_right = input("First choice... Left or Right (left/right)? ").lower()
        if left_or_right == "left" or weapon == "sword":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ").lower()
            
            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5
             
            ans = input("You notice a house and a river, which do you go to (river/house)? ").lower()
            if ans == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                health -=5
                
                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived... You win!")
            
            else:
                print("You fell in the river and lost...")
                
        else:
            print("You fell down and lost...")
    else:
        print("Cya...")
else:
    print("You are not old enough to play...")


'''
string "hello", 'hi', "89"
int 8, 7, -9, 10000
float 6.0, 7.5, -9.8, -100.0
bool True, False
'''