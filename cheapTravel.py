n, m, a, b = map(int, input().split())
if m>n:
    print(b)
elif b>=a:
    mRides = int(n/m)
    nRides = n%m
    total = mRides*b + nRides*a
    print(total)
elif a>b:
    mRides = int(n/m)
    nRides = n%m
    total = mRides*b + nRides*b
    print(total)