import random


def hangman():

    word_list = ["python", "robot", "coding", "bookshelf", "pirate"]

    word = random.choice(word_list)

    answer = ["-" for i in range(len(word))]

    
    

    print('-' * len(word))

    
    while True:
        check = ""
        guess(word, answer)
        for x in answer:
            check += x

        print('\n', check)

        if check == word:
            print('-' * 50, "\n\nyou won\n\n")
            break
            
        
    

def guess(word, answer):

    guess = input("Guess a letter.\n").lower()
      

    for i in range(len(word)):
        if guess == word[i] and len(guess) < 2:
            answer[i] = guess
    
    

    



hangman()