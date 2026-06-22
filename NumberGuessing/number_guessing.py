import random

logo = ''' 

___________.__              _______               ___.                    ________                            .__                   ________                       
\__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
  |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
  |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
  |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
                \/     \/          \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
                                                                                      /____/                                
                                                                                        
 '''
def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    random_num = random.randint(1,100)

    def checking_num():
        attempts = 0
        if difficulty_level == "easy":
            attempts = 10
        else:
            attempts = 5
            
        get_num = False
        while attempts > 0 and get_num == False:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guessed_num = int(input("Make a guess: "))
            if random_num == guessed_num:
                print(f"You got it! The answer was {random_num}.")
                get_num = True
            elif random_num > guessed_num:
                print("Too low.\nGuess again.")
                attempts -= 1
            else:
                print("Too high.\nGuess again.")
                attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")
        
    checking_num()
while input("Do you want to play a number guessing game? Type 'yes' or 'no': ") == "yes":
    play_game()
