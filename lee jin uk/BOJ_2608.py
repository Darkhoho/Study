dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, "M": 1000}
dict2 = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
A = input()
B = input()
sum_AB = 0
i = j = 0
while i < len(A):
    if i == len(A) - 1:
        sum_AB += dict1[A[i]]
    elif dict1[A[i]] < dict1[A[i + 1]]:
        sum_AB -= dict1[A[i]]
    else:
        sum_AB += dict1[A[i]]
    i += 1
while j < len(B):
    if j == len(B) - 1:
        sum_AB += dict1[B[j]]
    elif dict1[B[j]] < dict1[B[j + 1]]:
        sum_AB -= dict1[B[j]]
    else:
        sum_AB += dict1[B[j]]
    j += 1
print(sum_AB)
AB = ''
while sum_AB:
    AB += dict2[1000] * (sum_AB // 1000)
    sum_AB = sum_AB % 1000
    if sum_AB // 100 == 9:
        AB += dict2[100] + dict2[1000]
        sum_AB = sum_AB % 100
    elif sum_AB // 100 == 4:
        AB += dict2[100] + dict2[500]
        sum_AB = sum_AB % 100
    else:
        AB += dict2[500] * (sum_AB // 500)
        sum_AB = sum_AB % 500
        AB += dict2[100] * (sum_AB // 100)
        sum_AB = sum_AB % 100
    if sum_AB // 10 == 9:
        AB += dict2[10] + dict2[100]
        sum_AB = sum_AB % 10
    elif sum_AB // 10 == 4:
        AB += dict2[10] + dict2[50]
        sum_AB = sum_AB % 10
    else:
        AB += dict2[50] * (sum_AB // 50)
        sum_AB = sum_AB % 50
        AB += dict2[10] * (sum_AB // 10)
        sum_AB = sum_AB % 10
    if sum_AB == 9:
        AB += dict2[1] + dict2[10]
        sum_AB = sum_AB % 1
    elif sum_AB == 4:
        AB += dict2[1] + dict2[5]
        sum_AB = sum_AB % 1
    else:
        AB += dict2[5] * (sum_AB // 5)
        sum_AB = sum_AB % 5
        AB += dict2[1] * (sum_AB // 1)
        sum_AB = sum_AB % 1
print(AB)