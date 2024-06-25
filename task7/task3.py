nums = [1,1,1]
k = 2
cnt = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums) + 1):
        if sum(nums[i:j]) == k:
            cnt += 1

print(cnt)
