a, b, c = map(int, input().split())

if a>c: t=a; a=c; c=t
if a>b: t=a; a=b; b=t
if b>c: t=b; b=c; c=t

print(a, b, c)
if a+b <= c:
    print("NO")
elif a*a + b*b < c*c:
    print("Obtuse")
elif a*a + b*b == c*c:
    print("Right")
elif a*a + b*b > c*c:
    print("Acute")
