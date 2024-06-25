nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [5, 4, -1, 7, 8]
# nums = [-42]
res = 0
# перебираем все подотрезки
for i in range(len(nums)):
    for j in range(i, len(nums) + 1):
        res = max(sum(nums[i: j]), res)
print(res)