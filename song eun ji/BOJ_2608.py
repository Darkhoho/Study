# 로마자 -> 숫자
def roma(word):
    result = 0
    check = [0] * len(word) # 2개짜리로 봤는지 check 할 것

    # 일단 2개짜리 먼저보고 있으면 더해주고 아니면 한개짜리로 해버리기
    for i in range(len(word)):
        if (word[i:i+2] in cf_num) and i + 1 < len(word): # 2개짜리 있는지 확인
            result += cf_num[word[i:i+2]]
            check[i] = check[i+1] = 1

        elif check[i] == 0: # 0인지 먼저 보고 0이면 숫자 바꿔주기
            result += num[word[i]]
            check[i] = 1

    return result

# 숫자 -> 로마자
def number(n):
    n = str(n)
    result = ''

    # 일단 값을 받자
    for i in range(len(n),0,-1): # 합이 4000이 안된다고 하니까 4자리수로 생각

        val = int(n[-i]) # 각자리수의 값 받아오기

        if i == 4: # 4자리 수라면
            result += "M"*val # M이 1000이니까

        elif i == 3: # 3번째 자리 수라면
            if val == 9: # CD랑 CM구별해주기
                result += "CM"
            elif val == 4:
                result += "CD"
            else:
                if val >= 5: # 나머지는 계산해주는데, 500이상이면 D하기 아니면 C
                    result += "D"
                result += "C"*(val%5)

        elif i == 2: # 2번째 자리 수라면
            if val == 9: # XL랑 XC구별해주기
                result += "XC"
            elif val == 4:
                result += "XL"
            else:
                if val >= 5: # 나머지는 계산해주는데, 50이상이면 L하기 아니면 X
                    result += "L"
                result += "X"*(val%5)

        elif i == 1: # 1번째 자리 수라면
            if val == 9: # IX랑 IV구별해주기
                result += "IX"
            elif val == 4:
                result += "IV"
            else:
                if val >= 5: # 나머지는 계산해주는데, 5이상이면 V하기 아니면 I
                    result += "V"
                result += "I"*(val%5)

    return result

# 조건 파악하기
num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
cf_num = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

# 입력값 받기
num1 = str(input())
num2 = str(input())
total = roma(num1) + roma(num2)
print(total)
print(number(total))