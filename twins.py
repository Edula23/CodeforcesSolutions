games = int(input())
winners = input()
anton =0
danik =0
for i in range(games):
    if winners[i]=='A':
        anton+=1
    else:
        danik+=1
if anton>danik:
    print("Anton")
elif anton==danik:
    print("Friendship")
else:
    print("Danik")