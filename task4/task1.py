nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5, 4, -1, 7, 8]
nums = [-42]
res, cur_sum, min_zona = 0, 0, 0
for i in nums:
    cur_sum += i
    min_zona = min(min_zona, cur_sum)
    res = max(res, cur_sum - min_zona)
print(res)