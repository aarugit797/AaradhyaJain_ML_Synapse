runes=str(input("Enter a string: "))
runes=runes.upper()
k=0
step=-1
p,q,r,s,t='a','b','c','d','e'
z=0
for i in runes:
    z+=1
    if i=='L' and p!=i:
        k+=1
        p=i
    elif i=='U' and q!=i:
        k+=1
        q=i
    elif i=='M' and r!=i:
        k+=1
        r=i
    elif i=='O' and s!=i:
        k+=1
        s=i
    elif i=='S' and t!=i:
        k+=1
        t=i
    if(k==5):
        step=z
        break
print(step)