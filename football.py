team = input()
counter=1
for i in range(1, len(team)):    
    if team[i] == team[i-1]:
        counter+=1
        if counter==7:
            print("YES")
            break
        elif i==len(team)-1:
            print("NO")
            break
    else:
        counter=1
        if i==len(team)-1:
            print("NO")
            break
        
