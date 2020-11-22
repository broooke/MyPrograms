import random, sys
game = True
while game==True:
    print("Hello! Welcome to my game! It's a text adventure!")
    print("Your task is to reach the end and takes a diamond cup!")
    start = int(input("Choose a number from 1 to 3. This number is responsible for which track you start from: "))
    if start == 1:
        print("You are stumped! You lose(")
        break
    elif start == 2:
        print("Your road splits in two! Where are you going? Up or down?")
        ans = input("Up or Down?:")
        if ans.lower() == "up":
            print("You are going up!")
            print("You road again splits in two!!! Where are you going? Up or down?")
            ans = input("Up or Down?:")
            if ans.lower() == "up":
                print("You in a room with the boss!")
                health_boss = random.randint(100,150)
                health_player = random.randint(50,80)
                spirit = 1
                while health_boss>=0:
                    if health_player<=0:
                        print("You lose!")
                        sys.exit(0)
                     
                    print(health_boss)
                    print(health_player)
                    print(spirit)
                    attack_boss = random.randint(1,10)
                    attack_player = random.randint(10,30)
                    print("You have two paths. Boss attack or accumulation of spirits.")
                    print("If you take an accumulation of spirits, you get a spirit, and the next attack multiplies on numbers of spirits!")
                    choose = input("Attack or accumulation?:")
                    if choose.lower() == "attack":
                        health_boss-=attack_player*spirit
                        health_player-=attack_boss
                    else:
                        spirit+=1  
                        health_player-=attack_boss
                else:
                    print("You win!!")
                print("The road again splits in two!")
                choose = input("Up or down?: ")
                if choose.lower() == "up":
                    print("YOU WIN THIS GAME!!!! YOU FIND DIAMOND CUP!!!")
                    break
                else:
                    print("You are stumped! You lose(")
        
                    break
            else:
                print("You are in a room where you need to find a programming language and IDE!")
                move = 2
                while move!=0:
                    move-=1
                    print("You have four directions.")
                    ans_1 = input("Up or down or right or left: ")
                    ans_2 = input("Up or down or right or left: ")
                    if ans_1.lower() == "up" and ans_2.lower() == "right":
                        print("You right!")
                        print("YOU WIN THIS GAME!!!! YOU FIND DIAMOND CUP!!!")
                        game = False
                        break
                    else:
                        print("You lose!")
                        game = False 
                        break 
                    break
            
        else:
            print("You were trapped in a room on the third path!")
            key = random.randint(1,3)
            print(key)
            ans_key = int(input("Enter the cell number where the key is stored: "))
            if key==ans_key:
                print("Сongratulations! You guessed number cell!")
                print("You are in a room where you need to guess a riddle!")
                print("You have three tries!") 
                print("In winter and summer in the same color?")
                tries = 3
                while tries!=0:
                    tries-=1
                    print(tries)
                    ans = input("Answer:")
                    if ans.lower() == "rabbit":
                        print("YOU GUESSED!!!!")
                        print("The road splits in two!")
                        ans = input("Up or down: ")
                        if ans.lower() == "down":
                            print("You are in a room where you need to find a programming language and IDE!")
                            move = 2
                            while move!=0:
                                move-=1
                                print("You have four directions.")
                                ans_1 = input("Up or down or right or left: ")
                                ans_2 = input("Up or down or right or left: ")
                                if ans_1.lower() == "up" and ans_2.lower() == "right":
                                    print("You right!")
                                    print("YOU WIN THIS GAME!!!! YOU FIND DIAMOND CUP!!!")
                                    game = False
                                    break
                            else:
                                print("You lose!")
                                game = False 
                                break 
                            break   

                        else:
                            print("You are stumped! You lose(")
                            game = False
                            
                        break
                else:
                    print("The attempt vanished!! You lose(")
                    break
            print("loser!")

    elif start == 3:
        print("You were trapped in a room on the third path!")
        key = random.randint(1,3)
        print(key)
        ans_key = int(input("Enter the cell number where the key is stored: "))
        if key==ans_key:
            print("Сongratulations! You guessed number cell!")
            print("You are in a room where you need to guess a riddle!")
            print("You have three tries!") 
            print("In winter and summer in the same color?")
            tries = 3
            while tries!=0:
                tries-=1
                print(tries)
                ans = input("Answer:")
                if ans.lower() == "rabbit":
                    print("YOU GUESSED!!!!")
                    print("The road splits in two!")
                    ans = input("Up or down: ")
                    if ans.lower() == "down":
                        print("You are in a room where you need to find a programming language and IDE!")
                        move = 2
                        while move!=0:
                            move-=1
                            print("You have four directions.")
                            ans_1 = input("Up or down or right or left: ")
                            ans_2 = input("Up or down or right or left: ")
                            if ans_1.lower() == "up" and ans_2.lower() == "right":
                                print("You right!")
                                print("YOU WIN THIS GAME!!!! YOU FIND DIAMOND CUP!!!")
                                game = False
                                break
                        else:
                            print("You lose!")
                            game = False 
                            break 
                        break   

                    else:
                        print("You are stumped! You lose(")
                        game = False
                    break
            else:
                print("The attempt vanished!! You lose(")
                break
        else:
            print("loser!")
            game= False
        break


    

                
                       
