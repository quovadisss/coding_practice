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

# 1026번
N = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

result = 0
for i in range(N):
    result += min(a) * max(b)
    a.remove(min(a))
    b.remove(max(b))

print(result)

# 1541번
cal = input()
num = [sum(c.split("+")) for c in cal.split("-")]
print(num[0] - sum(num[1:]))

# 5585번