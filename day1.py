f = open("input/day1.txt","r")
lines = f.readlines()
l1 = []
l2 = []
for line in lines:
    a, b = map(int, line.split())
    l1.append(a)
    l2.append(b)
l1.sort()
l2.sort()
total = 0
for i in range(len(l1)):
    if l1[i] >= l2[i]:
        total += l1[i] - l2[i]
    else:
        total += l2[i] - l1[i]
print(total)