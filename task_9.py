arr=list(map(int,input("enter the arr:").split()))
sum=int(input("enter the sum:"))
i=0
j=1
s=0
y=2
len=len(arr)
while i<len:
    while j<len:
        while y<len:
            c=arr[i]
            x=arr[j]
            z=arr[y]
            s=x+c+z
            i=i+1
            j=j+1
            y=y+1
            if x==sum:
                print([x])
            elif  c==sum:
                print([c])
            elif z==sum:
                print([z])
            elif s==sum:
                print([c,x,z])

