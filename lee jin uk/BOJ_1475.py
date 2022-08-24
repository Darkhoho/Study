N = int(input())
numbers = [0] * 10
while N > 0:
    n = N % 10
    N = N // 10
    numbers[n] += 1
six_nin = []
six_nin.append(numbers.pop(9))
six_nin.append(numbers.pop(6))
if sum(six_nin) / 2 > max(numbers):
    if sum(six_nin) % 2:
        result = sum(six_nin) // 2 + 1
    else:
        result = sum(six_nin) // 2
else:
    result = max(numbers)
print(result)