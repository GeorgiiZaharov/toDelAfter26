import sys
c = 13
for a in range(1, int(c ** 0.5) + 1):
    for b in range(1, int(c ** 0.5) + 1):
        if a*a + b*b == c:
            print(True)
            sys.exit(0)
print(False)
