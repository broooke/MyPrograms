import random

print("Welcome to my game!")
rounds = int(input("Enter the number of rounds"))
res = [[], []]
sum_1 = 0
sum_2 = 0
for i in range(1,rounds+1):
    a = random.randint(1,6)
    b = random.randint(1,6)
    print("Your number " + str(a))
    print("Computer number " +str(b))
    sum_1+=a
    sum_2+=b
    res[0].append(str(a))
    res[1].append(str(b))
print("Player    Computer")
for j in range(0,len(res[0])):
    print(res[0][j] + "         " + res[1][j])

if sum_1>sum_2:
    print("Player win!")
else:
    print("Computer win!")






