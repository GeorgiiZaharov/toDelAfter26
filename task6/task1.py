num = 100
def to_seven(num):
    res = ""
    while num >  0:
        res += str(num % 7)
        num //= 7
    if not res:
        res == '0'
    return res[::-1]
print(to_seven(num) if num >= 0 else '-' + to_seven(abs(num)))
