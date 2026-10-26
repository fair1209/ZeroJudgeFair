#a5
t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    if a[1] - a[0] == a[2] - a[1]:
        # 等差數列
        fifth = a[3] + (a[1] - a[0])
    else:
        # 等比數列
        fifth = a[3] * (a[1] // a[0])
    a.append(fifth)
#     print(*a)