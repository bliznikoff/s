try:
    inputN = int(input("inputN ="))  #5
    inputN2 = int(input("inputN2 =")) #25
except:
    pass

try:
    if inputN2 == inputN**2:
        print(f"{inputN} == {inputN2}^2")
    else:
        print(f"{inputN} != {inputN2}^2")
except:
    pass

inputList = list()

try:
    for i in range(5):
        inputList.append(int(input(f"i{i}=")))
    maxN = inputList[0]
except:
    pass

for i in inputList:
    print(i)


try:
    for n in range(len(inputList)):
        if (inputList[n] > maxN):
            maxN = inputList[n]
            print(f"{inputList[n]} > {maxN}")
except:
    pass

print(maxN)
print(maxN)
