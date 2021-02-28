# Verification

foutput = open("output.txt")
finput = open("input2.txt")

content = foutput.read()
elements = content.splitlines()
content = finput.read()
inputs = content.split()
calculated = [1]

foutput.close()
finput.close()

while "" in elements:
    elements.remove("")

error = 0

if (len(elements[0].split()) != 1):
    error = 1
elif (int(elements[0]) != len(elements)-1):
    error = 2
else:
    for i in range(1, len(elements)):
        addends = elements[i].split()
        if (len(addends) != 2):
            error = 3
            break

        if (int(addends[0]) in calculated and int(addends[1]) in calculated):
            calculated.append(int(addends[0])+int(addends[1]))
        else:
            error = 4
            break

    for i in range(1, len(inputs)):
        if int(inputs[i]) not in calculated:
            error = 5
            break

print(error)