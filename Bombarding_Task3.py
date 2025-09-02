maps=[[1,0,0,0,1],[1,0,1,1,1],[1,1,0,1,1],[1,0,1,1,0],[0,1,0,1,1]]
m = int(input("Enter the radius after bo,b blasts: "))

if m%2==0 or m>len(maps):
    print("Invalid input")

mx=0
radius = m//2
x,y=0,0

for i in range(0,5):
    for j in range(0,5):
        if maps[i][j]==1:
            sum = 0
            for c in range(i-radius,i+radius+1):
                for k in range(j-radius,j+radius+1):
                    if 0 <= c < len(maps) and 0 <= k < len(maps):
                        sum+=maps[c][k]
        mx=max(mx,sum)
        if sum>mx:
            x,y=i,j

print(mx)
print(x,y)