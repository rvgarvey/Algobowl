# main

f = open("inputs/input_group272.txt")

content = f.read()
inputArr = content.split()
inputArr = [int(i) for i in inputArr]

# initializing arrays
calcArr1 = []
calcArr2 = []

# arrays
calcArr1.append([1,1,2])
calcArr2.append([1,1,2])

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

# new technique (appears to win every time)
for i in range(1, len(inputArr)):
    if i == 1:
        calculateValue(inputArr[i], calcArr1)
    else:
        difference = calculateValue(inputArr[i]-inputArr[i-1], calcArr1)
        calcArr1.append([inputArr[i-1], difference, inputArr[i]])

# new new technique
def findPredecessor(value):
    count = len(calcArr2) - 2
    
    minimum = 0
    returnVal = -1
    while (count >= 0):
        if (calcArr2[count][2] < value and calcArr2[count][2] > value//2 and calcArr2[count][2] > minimum):
            returnVal = calcArr2[count][2]
            minimum = returnVal
        count = count - 1

    return returnVal

for i in range(1, len(inputArr)):
    if i == 1:
        calculateValue(inputArr[i], calcArr2)
    else:
        difference = inputArr[i]-inputArr[i-1]

        predecessor = findPredecessor(difference)
        if (predecessor > -1):
            newdifference = difference - predecessor
            calculateValue(newdifference, calcArr2)
            if ((predecessor + newdifference) not in [a[2] for a in calcArr2]):
                calcArr2.append([predecessor, newdifference, predecessor + newdifference])
            calcArr2.append([inputArr[i-1], difference, inputArr[i]])
        else:
            calculateValue(difference, calcArr2)
            calcArr2.append([inputArr[i-1], difference, inputArr[i]])

# sort arrays
calcArr1 = sorted(calcArr1, key=lambda x: x[2])
calcArr2 = sorted(calcArr2, key=lambda x: x[2])

# changed this to a function so we can call it for both calc arrays
def generateOutput(calcArr, filename):
    w = open(filename, "w")
    w.write(str(len(calcArr)) + "\n")

    for x in calcArr:
        w.write(str(x[0]) + " " + str(x[1]) + "\n")

# generate outputs
generateOutput(calcArr1, "output1.txt")
generateOutput(calcArr2, "output2.txt")

bestArr = calcArr1
if (len(calcArr2) < len(bestArr)):
    bestArr = calcArr2

# generateOutput(bestArr, "AlgoBowlOutput.txt")
