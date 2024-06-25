import sys
s1 = "ab"
s2 = "eidbaooo"
for i in range(len(s2) - len(s1) + 1):
    if sorted(s1) == sorted(s2[i:i+len(s1)]):
        print(True)
        sys.exit()
print(False)