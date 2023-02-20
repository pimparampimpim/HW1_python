a=int(input())
b=int(input())
c=int(input())
d=(b**2-4*a*c)**1/2
if d>0:
    print((-b-d), (-b+d))
elif d==0:
    print(-b)
else:
    print(' ')