'''input: 3 5 4 3 6 7 1 2 4 3 3 7 6 8 8
output:
    3 - 4
    5-1
    4-2
    6-2
    7-2
    1-1
    2-1
    8-2'''
numbers =list(map(int,input().split()))
counts = {}
i = 0
length = len(numbers)
while i < length:
    num = numbers[i]
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
    i += 1
for num, count in counts.items():
    print(f"{num} - {count}")
