# 숫자 크기대로 딕셔너리에 할당
dct = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50,
       'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

# 숫자로 치환
def num(x, dct):
    i = 0
    result = 0
    while i < len(x):
        # 두자리 로마 숫자일 경우
        if i != len(x) - 1 and x[i] + x[i + 1] in dct:
            result += dct.get(x[i] + x[i + 1])
            i += 2
        # 한자리일 경우
        else:
            result += dct.get(x[i])
            i += 1
    return result


x = num(input(), dct)
y = num(input(), dct)
sol = x + y
# 숫자를 다시 로마 숫자로 변경
rome_sol = ''
for k, v in dct.items():
    while v <= sol:
        sol -= v
        rome_sol += k

print(x + y)
print(rome_sol)