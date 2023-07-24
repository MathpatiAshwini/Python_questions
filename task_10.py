l=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
i=0
while i<len(l):
    if l[i]<0:
        r=l[i]
        print(r,end=" ")
    i+=1
k=0
while k<len(l):
    if l[k]>0:
        p=l[k]
        print(p,end=" ")
    k+=1