counter = {}
for x in input().lower().split():
    if x not in counter:
        counter[x] = 1
    else:
        counter[x] += 1

for key, value in counter.items():
    print(f"{key} {value}")
