# Verification

#4
#2 3 4 5

#4
#1 1
#1 2
#1 3
#1 4

foutput = open("output.txt")
finput = open("input.txt")

content = foutput.read()
elements = content.splitlines()
content = finput.read()
inputs = content.split()
calculated = [1]

foutput.close()
finput.close()

if (len(elements[0].split()) != 1):
    print('Error in output file: Wrong first line format')
elif (int(elements[0]) != len(elements)-1):
    print('Error in output file: wrong number of additions')
else:
    for i in range(1, len(elements)):
        addends = elements[i].split()
        if (len(addends) != 2):
            print('Error in output file: Wrong addition format')
            break

        if (int(addends[0]) in calculated and int(addends[1]) in calculated):
            calculated.append(int(addends[0])+int(addends[1]))
        else:
            print('Error in output file: Num not calculated')
            break

    for i in range(1, len(inputs)):
        if int(inputs[i]) not in calculated:
            print('Error in output file: doesnt calculate inputs')
            break

