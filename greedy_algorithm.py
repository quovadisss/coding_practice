# 2022.3.12
# 11047
N, K = input().split()
N = int(N)
K = int(K)
coins = sorted([int(input()) for i in range(N)][:len(str(K))*2], reverse=True)
result = 0
for i in coins:
    if K / i >= 1:
        result += K // i
        K = K % i
        if K == 0: break
            
print(result)

# 1931
N = int(input())
a = []
for i in range(N):
    start, end = map(int, input().split())
    a.append([start, end])
a = sorted(a, key=lambda x: x[0])
a = sorted(a, key=lambda x: x[1])

e = 0
count = 0
for i, j in a:
    if i >= e:
        e = j
        count += 1

print(count)