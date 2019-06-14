n1,k1=map(int,input().split())
lis1=list(map(int,input().split()))
li1=[]
for i in lis1:
    if i%2!=0:
        li1.append(i)
print(li1[k1-1])
