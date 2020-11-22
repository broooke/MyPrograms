import random
a = []
for i in range(10):
    a.append(random.randint(1,10))
print(a)

low = 0
high = len(a)-1
mid = int(high/2)
ans = int(input("number: "))
while a[mid]!=ans and low<high:
    if ans>a[mid]:
        low = mid+1
    else:
        high = mid-1
    mid = int((high+low)/2)

if low>high:
    print("GG")
else:
    print(mid)