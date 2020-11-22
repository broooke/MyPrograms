import random

word = random.choice(open('word.txt', 'r', encoding='utf-8').read().splitlines())
print(word)


letterGuessed = ""
lg = ""
Game = True
chances = len(word)+2
print()

while Game==True and chances>0:
    for i in word:
        if i in letterGuessed:
            print(i, end=" ")
        else:
            print("-", end=" ")
    print()
    if set(lg)==set(word):
        print("WIN!!!")
        break

    letter = input("Enter the suggested letter: ")
    letterGuessed+=letter
    chances-=1

    if letter in word:
        print("This letter have in word!")
        lg+=letter
    print("Chances: " + str(chances))
        
    

else:
    print("LOSE!!!!")



