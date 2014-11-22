## Game functions

import sys
import random

def guess(num, num_to_guess):
    if num == num_to_guess:
        return "Correct!!!\n"
    elif num < num_to_guess:
        return "Too low.\n"
    else:
        return "Too high.\n"

def check_answer(num, num_to_guess):
  return num == num_to_guess

## Game logic

print """"  .oooooo.                                            
 d8P'  `Y8b                                           
888           oooo  oooo   .ooooo.   .oooo.o  .oooo.o 
888           `888  `888  d88' `88b d88(  "8 d88(  "8 
888     ooooo  888   888  888ooo888 `"Y88b.  `"Y88b.  
`88.    .88'   888   888  888    .o o.  )88b o.  )88b 
 `Y8bood8P'    `V88V"V8P' `Y8bod8P' 8""888P' 8""888P' 
                                                      
                                                      
                                                      
    .   oooo                  
  .o8   `888                  
.o888oo  888 .oo.    .ooooo.  
  888    888P"Y88b  d88' `88b 
  888    888   888  888ooo888 
  888 .  888   888  888    .o 
  "888" o888o o888o `Y8bod8P' 
                              
                              
                              
ooooo      ooo                                .o8                          
`888b.     `8'                               "888                          
 8 `88b.    8  oooo  oooo  ooo. .oo.  .oo.    888oooo.   .ooooo.  oooo d8b 
 8   `88b.  8  `888  `888  `888P"Y88bP"Y88b   d88' `88b d88' `88b `888""8P 
 8     `88b.8   888   888   888   888   888   888   888 888ooo888  888     
 8       `888   888   888   888   888   888   888   888 888    .o  888     
o8o        `8   `V88V"V8P' o888o o888o o888o  `Y8bod8P' `Y8bod8P' d888b   """

print "\nWelcome! Today we are going to play a guessing game."


# while name == "":
#     name = raw_input("Please type your name: ")

print "OK, great!"
ready = raw_input("Are you ready to start?\nPlease type yes or no: ")

if ready.strip().lower() == "no":
    sys.exit()

num_to_guess = random.randrange(0,10)

num_guessed = int(raw_input("Please guess a number between 0 and 10: "))
result = guess(num_guessed, num_to_guess)
print result

if result == "Correct!!!\n":
  print "Congrats! You beat me!"
else:
  print "Try another time sucker! The number to guess was " + str(num_to_guess) + "."

