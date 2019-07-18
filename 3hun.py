o=int(input())
p=list(map(int,input().split(None,o)[:o]))
o=[]
for i in range(len(p)):
    if p[i]==i:
        
        o.append(p[i])
if len(o)==0:
    print(-1)
else:
    print(" ".join(map(str,o)))
