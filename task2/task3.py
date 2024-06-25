n = 7
def check(num):
    while True:
        for i in [2,3,5]:
            if num % i == 0:
                num //= i
                break
        else:
            break
    return num == 1
cur_num = 1
nice_num = []
while len(nice_num)!=n:
    if check(cur_num):
        nice_num.append(cur_num)
    cur_num+=1
print(nice_num[-1])