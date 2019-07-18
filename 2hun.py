    
u=int(input())
d=list(map(int,input().split(None,u)[:u]))
d.sort(key=None,reverse=True)
if d.count(0)==len(d):
    print(0)
else:
    print("".join(map(str,d)))
