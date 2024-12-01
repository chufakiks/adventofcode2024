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

idx = 0
total = 0
mydict = {}
for i in range(len(l1)):
    count = 0
    if l1[i] in mydict:
        total += l1[i] * mydict[l1[i]]
    else:
        while l2[idx] <= l1[i] and idx < len(l1) - 1:
            if l2[idx] == l1[i]:
                count += 1
            idx += 1
        mydict[l1[i]] = count
        total += l1[i] * count
print(total)
    
    