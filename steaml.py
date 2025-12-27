import random
import time


def clear():
    print("\n" * 100)
    time.sleep(0.1)


stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print("Welcome to Hangman game!\n"
      "Animals name are in thanglish(ex:singam),So think the letters in that way\n"
      "you should guess the animal name based on below letters count.\n"
      "you have 6 lives.each time whn you are guessing wrong you lose life.\n"
      "So at then end if you lose all lives you will be hanged:)")
word_list = ["singam", "puli", "anil", "paampu", "muyal", "nari", "mayil"]
singam_clue = "You have one life left,So i will give you one clue:Kattuke Raja"
puli_clue = "You have one life left,So i will give you one clue:India oda national Animal"
anil_clue = "You have one life left,So i will give you one clue:Muthugula Moonu lines irukum"
paampu_clue = "You have one life left,So i will give you one clue:paatha padaye natungum"
muyal_clue = "You have one life left,So i will give you one clue:kutty ah irukum,vegama oodum ana maan ila"
nari_clue = "You have one life left,So i will give you one clue:Thanthiramana animal"
mayil_clue = "You have one life left,So i will give you one clue:muruganin vaganam"

Game_Restart = False


def game():
    lives = 6
    chosen_word = random.choice(word_list)
    to_user = ""
    for _ in chosen_word:
        to_user += "_"
    print(f"So your Word have {len(chosen_word)} letters in it:{to_user}")

    Game_over = False
    clue_1 = False
    crc_word = ""
    while not Game_over:
        display = ""
        guess = input("please enter one letter that there in your guessing word:").lower()
        clear()
        for letter in chosen_word:
            if letter == guess:
                display += letter
                crc_word += letter
            elif letter in crc_word:
                display += letter
            else:
                display += "_"
        print(display)
        if display == chosen_word:
            Game_over = True
            print("You Won!")
        elif guess in chosen_word:
            print(f"Your letter is there in word! You have {lives} Lives reamining")
            print(stages[lives])
        elif guess not in chosen_word:
            lives -= 1
            print(f"Oh no!,You letter not there in word,So you loss one life.Remaining lives {lives}")
            print(stages[lives])
        if lives == 1:
            while not clue_1:
                if lives == 1:
                    clue_need = input("Do you need clue? Y or N:").lower()
                    if clue_need == "y":
                        if chosen_word == word_list[0]:
                            print(singam_clue)
                        elif chosen_word == word_list[1]:
                            print(puli_clue)
                        elif chosen_word == word_list[2]:
                            print(anil_clue)
                        elif chosen_word == word_list[3]:
                            print(paampu_clue)
                        elif chosen_word == word_list[4]:
                            print(muyal_clue)
                        elif chosen_word == word_list[5]:
                            print(nari_clue)
                        elif chosen_word == word_list[6]:
                            print(mayil_clue)
                        print(display)
                    clue_1 = True
        elif lives == 0:
            clear()

            print("You lost all your lives and hanged:)")
            print("Game over.")
            print(stages[lives])
            Game_over = True


while not Game_Restart:
    game()
    Replay = input('Do you want to replay the game "Y" for Yes and "N" for No:').lower()
    if Replay == "y":
        Game_Restart = False
        clear()
    elif Replay == "n":
        Game_Restart = True
        clear()
        print("Thank you for the play")
    else:
        Game_Restart = True
        clear()
        print("Thank you for the play")
