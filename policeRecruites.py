size = int(input())
n = list(map(int, input().split()))
untreated =0
polices = 0
for i in range(size):
    if n[i]>=0:
        polices+=n[i]
    elif n[i]==(-1):
        if polices>0:
            polices-=1
        else:
            untreated+=1
print(untreated)