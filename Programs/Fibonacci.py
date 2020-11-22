a = [0,1,1]
b = int(input("Size: "))
while len(a)!=b:
    a.append(a[-1]+a[-2])
print(a)
k = int(input())
if k in a:
    print("You right!")
else:
    print("false")
