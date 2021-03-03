# main

f = open("input1.txt")

content = f.read()
inputArr = content.split()
inputArr = [int(i) for i in inputArr]

# making two arrays
calcArr1 = []
calcArr2 = []
calcArr3 = []
calcArr4 = []

# TODO: handle case where input includes 1
# (only 1 and 1 in addition to other values)

# three arrays
calcArr1.append([1,1,2])
calcArr2.append([1,1,2])
calcArr3.append([1,1,2])
calcArr4.append([1,1,2])

# changing function to accept calc array as a parameter
def calculateValue(x, calcArr):
    if(x == 1):
        return 1
    if(x in [addition[2] for addition in calcArr]):
        return x

    if(x % 2 == 0):
        addend = calculateValue(x // 2, calcArr)
        calcArr.append([addend,addend,x])
        return x
    else:
        addend2 = calculateValue(x // 2 + 1, calcArr)
        addend1 = calculateValue(x // 2, calcArr)
        calcArr.append([addend1,addend2,x])
        return x

# original technique
for i in range(1, len(inputArr)):
    calculateValue(inputArr[i], calcArr1)

# new technique (appears to win every time)
for i in range(1, len(inputArr)):
    if i == 1:
        calculateValue(inputArr[i], calcArr2)
    else:
        difference = calculateValue(inputArr[i]-inputArr[i-1], calcArr2)
        calcArr2.append([inputArr[i-1], difference, inputArr[i]])

########################################
## Trying something new
## This seems to lose every time, but I didn't get to check
## against multiple inputs
def calculateValue2(x, calcArr):
    if(x == 1):
        return 1
    if(x in [addition[2] for addition in calcArr]):
        return x
    if (x < 3):
        calculateValue(x, calcArr)

    onethird = x // 3
    twothirds = x - onethird
    addend2 = calculateValue(onethird, calcArr)
    addend1 = calculateValue(twothirds, calcArr)
    calcArr.append([addend1,addend2,x])
    return x

for i in range(1, len(inputArr)):
    calculateValue2(inputArr[i], calcArr3)

# new technique
for i in range(1, len(inputArr)):
    if i == 1:
        calculateValue2(inputArr[i], calcArr4)
    else:
        difference = calculateValue2(inputArr[i]-inputArr[i-1], calcArr4)
        calcArr4.append([inputArr[i-1], difference, inputArr[i]])
  


##
########################################

# changed this to a function so we can call it for both calc arrays
def cleanUp(calcArr):
    length = -1
    while (length != len(calcArr)):
        length = len(calcArr)
        for e in reversed(calcArr):
            for f in calcArr:
                for g in calcArr:
                    if f[2] + g[2] == e[2]:
                        e[0] = f[2]
                        e[1] = g[2]

        for h in calcArr:
            if (h[2] not in inputArr[1:] and h[2] not in [a[0] for a in calcArr] and h[2] not in [a[1] for a in calcArr]):
                calcArr.remove(h)

# reduce number of additions if possible 
cleanUp(calcArr1)
cleanUp(calcArr2)
cleanUp(calcArr3)
cleanUp(calcArr4)

# sort arrays
calcArr1 = sorted(calcArr1, key=lambda x: x[2])
calcArr2 = sorted(calcArr2, key=lambda x: x[2])
calcArr3 = sorted(calcArr3, key=lambda x: x[2])
calcArr4 = sorted(calcArr4, key=lambda x: x[2])

# changed this to a function so we can call it for both calc arrays
def generateOutput(calcArr, filename):
    w = open(filename, "w")
    w.write(str(len(calcArr)) + "\n")

    for x in calcArr:
        w.write(str(x[0]) + " " + str(x[1]) + "\n")

# generate outputs
generateOutput(calcArr1, "output1.txt")
generateOutput(calcArr2, "output2.txt")
generateOutput(calcArr3, "output3.txt")
generateOutput(calcArr4, "output4.txt")

# I'm thinking that we can just use the better one
# but maybe you guys will come up with something better

bestArr = calcArr1
if (len(calcArr2) < len(bestArr)):
    bestArr = calcArr2
if (len(calcArr3) < len(bestArr)):
    bestArr = calcArr3
if (len(calcArr4) < len(bestArr)):
    bestArr = calcArr4

generateOutput(bestArr, "AlgoBowlOutput.txt")
