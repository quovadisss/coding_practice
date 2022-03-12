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

