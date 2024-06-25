import sys
nums = [3,1,4,2]
nums = [1,2,3,4]
nums = [-1,3,2,0]
for j in range(1, len(nums) - 1):
    for i in range(j):
        for k in range(j + 1, len(nums)):
            if  nums[i] < nums[k] < nums[j]:
                print(True)
                sys.exit()
print(False)