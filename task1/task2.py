nums = [4,-1,7,0,1,2,-1,5]
S = 3
for i in range(len(nums)):
    for j in range(i + 1):
        if sum(nums[j : i]) == S:
            print(nums[j : i])