class GuessingGame(object):
    def __init__(self, player_name):
        self.num_to_guess = random.randrange(0,10)
        self.player_name = player_name
        self.winner = False

    def player_name(self):
        return self.player_name

    def num_to_guess(self):
        return self.num_to_guess

    def guess(self, num):
        '''Tells the player the result of their guess'''
        if num == self.num_to_guess:
            self.winner = True
            return "Correct!!!\n"
        elif num < self.num_to_guess:
            return "Too low.\n"
        else:
            return "Too high.\n"

    def is_there_a_winner(self):
        '''Ends the game if there is a winner'''
        return self.winner

    def quit(self, input):
        '''Checks to see if a player wants to leave the game'''
        return input.strip().lower() == "quit"

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
print "But first I need your name!\n"
name = raw_input("Please type your name: ")

while name == "":
    name = raw_input("Please type your name: ")

my_game = GuessingGame(name)

print "OK, great!"
ready = raw_input("Are you ready to start playing %s?\nPlease type yes or no: " % name)

if ready.strip().lower() == "yes":
    my_game = GuessingGame(name)
else:
    sys.exit()

num_guessed = int(raw_input("Please guess a number between 0 and 100: "))
result = my_game.guess(num_guessed)
print result
game_over = my_game.is_there_a_winner()

while not game_over:
    num_guessed = raw_input("What's your next guess? ") 
    if my_game.quit(num_guessed):
        print my_game.player_name
        print "Thanks for playing %s. WE ARE SO SAD TO SEE YOU GO." % my_game.player_name
        print "BY THE WAY The number you had to guess was %s!" % my_game.num_to_guess
        sys.exit()
    correct_guess = my_game.guess(int(num_guessed))
    print correct_guess
    game_over = my_game.is_there_a_winner()


