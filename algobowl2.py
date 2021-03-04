# main

f = open("inputs/input_group289.txt")

content = f.read()
inputArr = content.split()
inputArr = [int(i) for i in inputArr]

# initializing arrays
calcArr = []

# arrays
calcArr.append([1,1,2])

# changing function to accept calc array as a parameter
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

def findPredecessor(value):
    count = len(calcArr) - 2

    minimum = 0
    returnVal = -1
    while (count >= 0):
        if (calcArr[count][2] < value and calcArr[count][2] > value//2 and calcArr[count][2] > minimum):
            returnVal = calcArr[count][2]
            minimum = returnVal
        count = count - 1

    return returnVal

def calcVal(x):
    if(x == 1):
        return 1
    if(x in [a[2] for a in calcArr]):
        return x
    
    predecessor = findPredecessor(x)
    if (predecessor == -1):
        calculateValue(x)
        return x
    else:
        newdifference = x - predecessor
        if ((predecessor + newdifference) not in [a[2] for a in calcArr]):
            calcArr.append([predecessor, newdifference, predecessor + newdifference])
        calcVal(newdifference)
        return x

for i in range(1, len(inputArr)):
    if i == 1:
        calculateValue(inputArr[i])
    else:
        difference = inputArr[i]-inputArr[i-1]
        calcVal(difference)
        calcArr.append([inputArr[i-1], difference, inputArr[i]])
        
# sort array
calcArr = sorted(calcArr, key=lambda x: x[2])

# changed this to a function so we can call it for both calc arrays
def generateOutput(filename):
    w = open(filename, "w")
    w.write(str(len(calcArr)) + "\n")

    for x in calcArr:
        w.write(str(x[0]) + " " + str(x[1]) + "\n")

# generate output
generateOutput("AlgoBowlOutput.txt")
