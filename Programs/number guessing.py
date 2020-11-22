import random

f_r = int(input("Enter the first range:"))
s_r = int(input("Enter the second range:"))
attempt = int(input("Enter the number of attempts:"))
rand_num = random.randint(f_r,s_r+1)
print(rand_num)
while attempt!=0:
    attempt-=1
    print(attempt)
    ans = int(input("Enter the expected number:"))
    if ans==rand_num:
        print("Good job!You win! Your number is " + str(rand_num))
        break
    else:
        if ans>rand_num:
            print("Your number is less")
            continue
        else:
            print("Your number is greater")
else:
    print("Try to win in the next game! Good luck!")

