# main

f = open("input2.txt")

content = f.read()
inputArr = content.split()
inputArr = [int(i) for i in inputArr]

calcArr = []
tempArr = []
calcArr.append([1,1,2])
result = 0

def calculateValue(x):
    if(x == 1):
        return 1
    if(x in [addition[2] for addition in calcArr]):
        return x

    if(x % 2 == 0):
        addend = calculateValue(x // 2)
        calcArr.append([addend,addend,x])
        return x
    else:
        addend2 = calculateValue(x // 2 + 1)
        addend1 = calculateValue(x // 2)
        calcArr.append([addend1,addend2,x])
        return x

for i in range(1, len(inputArr)):
    calculateValue(inputArr[i])

length = -1
while (length != len(calcArr)):
    length = len(calcArr)
    for e in reversed(calcArr):
        result = e[2]
        for f in calcArr:
            for g in calcArr:
                if f[2] + g[2] == e[2]:
                    e[0] = f[2]
                    e[1] = g[2]

    for h in calcArr:
        if (h[2] not in inputArr[1:] and h[2] not in [a[0] for a in calcArr] and h[2] not in [a[1] for a in calcArr]):
            calcArr.remove(h)

calcArr = sorted(calcArr, key=lambda x: x[2])

w = open("output.txt", "w")
w.write(str(len(calcArr)) + "\n")

for x in calcArr:
    w.write(str(x[0]) + " " + str(x[1]) + "\n")