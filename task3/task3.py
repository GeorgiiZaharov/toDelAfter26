strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["a"]
dictionary = dict()
for str in strs:
    sorted_str = ''.join(sorted(str)) 
    if ''.join(sorted(str)) not in dictionary:
        dictionary[sorted_str] = [str]
    else:
        dictionary[sorted_str].append(str)
list(map(print, dictionary.values()))