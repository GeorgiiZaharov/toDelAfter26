pairs = [[1,2],[2,3],[3,4]]
pairs = [[1,2],[7,8],[4,5]]
pairs.sort()
good_durations = [pairs[0]]
for pair in pairs:
    if pair[0]>good_durations[-1][1]:# конец первого меньше начала второго
        good_durations.append(pair)
print(len(good_durations))