
import time

text = "speed typing test"
while str(input("'Enter' if you ready yo start")):
    t1 = time.time()
    ans = input('Write this text:"%s" '%(text))
    t2 = time.time()
    timeTaken = t2-t1
    accuracy = len(set(text.split()) & set(ans.split()))
    accuracy = accuracy / len(text.split())
    print(round(timeTaken, 2))
    print(accuracy)



