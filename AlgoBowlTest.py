f = open("input.txt")

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

for x in calcArr:
    print(x)

w = open("output.txt", "w")
w.write(str(len(calcArr)) + "\n")

for x in calcArr:
    w.write(str(x[0]) + " " + str(x[1]) + "\n")

w.close()
