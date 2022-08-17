import re

def readFile():
    # Using readlines()
    file = open('postalCodes.txt', 'r')
    lines = file.readlines()
    linesList = []
    for line in lines:
        linesList.append(line.strip())
    formattedDict = {}
    for line in linesList:
        s = line.split('\t')
        if s[0] in formattedDict.keys():
            formattedDict[s[0]] = formattedDict[s[0]] + " " + s[1]
        else:
            formattedDict[s[0]] = s[1]
    return formattedDict

def readInput():
    toContinue = True
    postCode = 0
    while toContinue:
        try:
            postCode = input('Give in a valid postcode: \n')
            if postCode.isdigit() and len(postCode) == 4:
                toContinue = False
            else:
                toContinue = True
                print('Invalid input, enter a 4 digit Belgian postal code.')
        except: 
            print('Error')
    return postCode

def compareListAndInput(file, input):
    listOfMatchingPostCodes = []
    allowed_chars =  input #ListOfNumbers(input)
    validationStrings = file.keys()
    for s in validationStrings:
        x = all(ch in allowed_chars for ch in s)
        if x:
            listOfMatchingPostCodes.append(s + ":" + file[s])
        else:
            continue
    
    return sorted(listOfMatchingPostCodes)

def writeOutput(outputToPrint):
    for strings in outputToPrint:
        x = strings.split(':')
        print(x[0] + " - "+ x[1].replace(' ', ','))

def ListOfNumbers(input):
    listing = []
    for i in input:
        listing.append(i)  
    return listing

if __name__ == "__main__":
    file = readFile()
    input = readInput()
    output = compareListAndInput(file, input)
    writeOutput(output)