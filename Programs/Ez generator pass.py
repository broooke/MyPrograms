import random
chars = "!@#$%^&*()-+.<>/,|';:1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
number = input("Введите количество паролей:")
lenght = input("Введите длину пароля:")
number = int(number)
lenght = int(lenght)
for j in range(1,number+1):
    password = ""
    for n in range(1,lenght+1):
        password+=random.choice(chars)
    print(password)

