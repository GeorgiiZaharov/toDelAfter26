string = "25525511135"
def check_good_ip(s):
    return all(map(lambda x: int(x) <= 255, s.split('.')))
def rec(cur_string):
    if cur_string.count('.') == 3:
        if check_good_ip(cur_string):
            print(cur_string)
        return
    if '.' in cur_string:
        start_index = cur_string.rindex('.') + 1
    else:
        start_index = 0
    for i in range( start_index + 1, len(cur_string)):
        rec(cur_string[:i] + '.' + cur_string[i:])
rec(string)
