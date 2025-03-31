import random
from random_word import RandomWords

word = RandomWords()

word = word.get_random_word()


#guess_words = ['Miami','New','City','Adventure']                            #just previous iteraction words getting to try and understand how to do this




chances = 5

print("Welcome to Hang man, you have four chances to guess the right word, or....YOU WILL BE HUNG,DANG,DANG,DANG!")
print("You may only get four chances and can only enter two letters.")
#word = random.choice(guess_words).lower()

print("The word you have to guess is: ")
for char in word:
    print('_',end ='')

correct = []                #where we are going to appended the users guessed letters to
    


def progress(word,guess_user):
    result = ''
    for char in word:
        if char in guess_user:
            result += char 
        else:
                result += '_'
    return result

guess_leters = set()

while chances > 0:
    print('')
    print('')
    guess_user = input("Enter what you think the word is: ").lower()
    if guess_user == word:
        print("Congrats, you have won the game!")
        break

    elif len(guess_user) != 2 and len(guess_user) != 1:                             #Checks for if the user input is less then or equal to 2
        print("Invalid input, you may only guess two letters per try!")
        print(progress(word,correct))

    elif guess_user in guess_leters:                                            #This checks for if the user repeats a word
        print("You have already guessed that/those letters.")
        print(progress(word,correct))

    elif guess_user != word:
        guess_leters.add(guess_user)                                  #Adds the guessed letters to the set
        for char in guess_user:                           #for each character in what the user input, add it to the set correct
            correct.append(char)
        print(progress(word,correct)) 
        chances = chances - 1
        print('')
       
        if chances == 0:
            print("You have been hung!")
            print(f"The word you had to guess was: {word}")
            break

        elif all(char in correct for char in word):                             #if all characters in correct are in the word, then they win!
            print(f"Congrats, you won it with {chances} left !")
            break

        print("Guesses left: " + str(chances))                        #shows the guesses left

   

                                                 
       

        
 

