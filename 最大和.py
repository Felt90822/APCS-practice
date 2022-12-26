N, M = map(int, input().split())
n = []

for i in range(0, N):
    num = list(map(int, input().split()))
    tem = []
    for j in range(0, M):
        tem.append(int(num[j]))
    n.append(tem)

BIG = [0 for i in range(N)]

for i in range(0, N):
    BIG[i] = int(n[i][0])
    for j in range(0, M):
        if int(n[i][j]) > BIG[i]:
            BIG[i] = int(n[i][j])

total = 0
for i in range(0, N):
    total += BIG[i]
print(total)

Bool = 'N'

for i in range(0, N):
    if total % BIG[i] == 0:
        Bool = 'Y'
        print(BIG[i], end='')

if Bool == 'N':
    print("-1")
