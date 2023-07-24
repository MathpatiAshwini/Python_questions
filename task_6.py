n=int(input("enter the number:"))
i=1
x=2
p=x
s=0
while i<=n:
    s+=p
    p=p*10+x
    i+=1
print(s)