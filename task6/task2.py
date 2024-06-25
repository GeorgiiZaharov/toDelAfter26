amount = 5
nums = sorted([1,2,5])
def rec(cur_sum=0, ind=0):
    if cur_sum == amount:
        return 1
    if cur_sum > amount:
        return 0
    return sum(rec(cur_sum + nums[i], i) for i in range(ind, len(nums)))
print(rec())

    
