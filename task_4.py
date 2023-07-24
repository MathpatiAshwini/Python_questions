n = int(input("enter the number:"))
s = 0
while n > 0:
    r = n % 10
    s += r
    n //= 10
    if  s > 9:
        s = s % 10 + s // 10
print(s)

