k=int(input())
m=int(input())
n=int(input())
if n % k == 0:
    print ((n//k)*m*2 )
else:
    print ((m*2)+((n//k)*m*2))