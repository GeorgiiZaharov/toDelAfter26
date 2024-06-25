def find(num, nums = []):
    need_find = num - sum(nums)
    for i in range(2, int(need_find ** 0.5) + 1):
        if sum(nums) + i ** 2 > num:
            break
        elif sum(nums) + i ** 2 == num:
            result = nums + [i ** 2]
            result = list(map(lambda x: int(x**0.5), result))
            return result
        else:
            result = nums + [i ** 2]
            res = find(num, result)
            if res!=-1:
                return res
    return -1
print(find(100))
