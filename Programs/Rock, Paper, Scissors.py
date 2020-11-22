import random

res = [[],[]]
sum1 = 0
sum2 = 0
game = True
while game:
    user_input = input("Player choice: [R,S,P]: ").lower()

    if user_input not in ["r","s","p"]:
        print("Incorrect input. Try again.")
        continue

    gen = {1:'p',2:'s',3:'r'}
    copm_input = gen[random.randint(1,3)]
    print("Comp choice: " +copm_input)

    win_comb = [('r','s'),('s','p'),('p','r')]

    if user_input==copm_input:
        print("A draw!")
        res[0].append("1")
        res[1].append("1")
        sum1+=1
        sum2+=1
    elif (user_input,copm_input) in win_comb:
        print("Player win!")
        res[0].append("3")
        res[1].append("0")
        sum1+=3
    else:
        print("Comp win!")
        res[0].append("0")
        res[1].append("3")
        sum2+=3

    print("Player    Computer")
    for j in range(0,len(res[0])):
        print(res[0][j] + "         " + res[1][j])

    game=input('If you want a continue the game, enter "y" else "n": ').lower()=="y"

if sum1>sum2:
    print("YOU WIN THIS GAME!!!")
elif sum1==sum2:
    print("A DRAW!")
else:
    print("LOSER!")


    

    