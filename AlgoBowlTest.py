f = open("AlgoBowlInputFile.txt")

content = f.read()
inputArr = content.split()
print(inputArr)

calcArr = []
tempArr = []
calcArr[0] = [1,1,2]
result = 0

for i in range(2, len(inputArr) - 1):
    diff = inputArr[i] - inputArr[i-1]
    if(diff not in tempArr):
        tempArr.append(diff)

tempArr.sort()


def recusionFunction(x):
    if(x == 2):
        return 2

    recursionFunction(x += x/2)


if(tempArr[0] != 2):
   

for tempElement in tempArr:
    for calcElement in calcArr:
        if calcElement[2]

        if(result not in calcElemtent[:,2]):
            calcArr.append(addend1, addend2, result)
    
for x in calcArr:
    print(x)
