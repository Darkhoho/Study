import sys; input = sys.stdin.readline

N = int(input())
num_lst = []
num_dict = {}
for _ in range(N):
    num = int(input())
    num_lst.append(num)
num_lst.sort()
for n in num_lst:
    num_dict[n] = num_lst.count(n)
print(round(sum(num_lst) / N))
print(num_lst[N // 2])
nums = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
if nums[0][1] == nums[1][1]:
    print(nums[1][0])
else:
    print(nums[0][0])
print(num_lst[-1] - num_lst[0])