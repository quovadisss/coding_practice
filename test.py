cal = "534"
last = 1000 - int(cal)
coins = [500, 100, 50, 10, 5, 1]
count = 0
for c in coins:
    count += last // c
    last %= c
print(count)
