strs = ["dog","doggy","dooor"]
prefix_len = 0
while all(map(lambda s: s[:prefix_len+1] == strs[0][:prefix_len + 1], strs)):
    prefix_len += 1
print(prefix_len)