nums = [4,-1,7,0,1,2,-1,5]
res = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            temp = sorted([nums[i], nums[j], nums[k]])
            if sum(temp) == 0 and temp not in res:
                res.append(temp) 
print(res)
