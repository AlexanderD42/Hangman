import random


def hangman():

    word_list = ["python", "robot", "coding"]

    word = random.choice(word_list)

    answer = '-' * len(word)

    print(answer)

    
    while answer != word:
        guess(word, answer)
        
    

    

        


def guess(word, answer):

    guess = input("Guess a letter.\n")
      
    for i in range(len(word)):
        if guess == word[i]:
            answer = answer[:i] + guess + answer[i:]

    print(answer)



hangman()