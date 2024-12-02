f = open("input/day2.txt","r")
lines = f.readlines()

safe = 0

def increasing(list):
    for i in range(1,len(list)):
        if list[i] - list[i - 1] < 0:
            return False
    return True

def decreasing(list):
    for i in range(1,len(list)):
        if list[i] - list[i - 1] > 0:
            return False
    return True

for line in lines:
    report = list(map(int,line.split()))
    diff = True
    if decreasing(report) or increasing(report):
        for i in range(1,len(report)):
            if report[i] >= report[i - 1]:
                dif = report[i] - report[i - 1]
            else:
                dif = report[i - 1] - report[i]
            if dif == 0 or dif > 3:
                diff = False
                break
        if diff == True:
            safe += 1
print(safe)