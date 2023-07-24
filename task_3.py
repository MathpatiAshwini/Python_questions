a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))

if a>b:
    max=a
    sec=b
else:
    max=b
    sec=a
if max>c:
    if sec<c:
        print(c)
    else:
        print(sec)
else:
    print(max)
