import random

big = "QWERTYUIOPASDFGHJKLZXCVBNM"
low = "qwertyuiopasdfghjklzxcvbnm"
num = "1234567890"
spe = "!@#$%^&"

bi = input()
lo = input()
nu = input()
sp = input()


a = True
while a==True:
    amount = input("Введите кол-во паролей:")
    amount_pass = input("Введите длину пароля:")
    if amount.isdigit() == True and amount_pass.isdigit() == True:
        amount = int(amount)
        amount_pass = int(amount_pass)
        a=False
        print(f"Вам будет сгенерировано " + str(amount) + " паролей!")
        print(f"Вам будут сгенерированые ключи с длиной " + str(amount_pass))
    else:
        print("Некорретный вворд")
        continue

symbols = []

if bi=="True":
    symbols.extend(big)
if lo=="True":
    symbols.extend(low)
if nu=="True":
    symbols.extend(num)
if sp=="True":
    symbols.extend(spe)

random.shuffle(symbols)

file_write = []
for i in range(amount):
    file_write.append("".join([random.choice(symbols) for j in range(amount_pass)]))

file_Pass = open('password.txt', 'w')
file_Pass.write('\n'.join(file_write))
file_Pass.close()

print("\n".join(file_write))
print("\n")



    

    