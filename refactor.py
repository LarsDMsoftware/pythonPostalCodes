import re

def readFile():
    file = open('postalCodes.txt', 'r')
    lines = file.readlines()
    formattedDict = {}
    for line in lines:
        strings = line.strip().split('\t')
        if strings[0] in formattedDict.keys():
            formattedDict[strings[0]] = formattedDict[strings[0]] + "," + strings[1]
        else:
            formattedDict[strings[0]] = strings[1]
    return formattedDict

def readInput():
    while True:
        try:
            postCode = input('Give in a valid postcode: ')
            if postCode.isdigit() and len(postCode) == 4:
                return postCode
            else:
                print('Invalid input, enter a 4 digit Belgian postal code.')
        except: 
            print('Error')
        
def compareListAndInput(formattedDict, userInput):
    listOfMatchingPostCodes = []
    allowed_chars =  userInput 
    validationStrings = formattedDict.keys()
    for strings in validationStrings:
        validPostCode = all(ch in allowed_chars for ch in strings)
        if validPostCode:
            listOfMatchingPostCodes.append(formatOutput(strings, formattedDict[strings]))
    return sorted(listOfMatchingPostCodes)

def formatOutput(key, value):
    formattedString = key + " - " + value
    return formattedString

def writeOutput(outputToPrint):
    for strings in outputToPrint:
        print(strings)

if __name__ == "__main__":
    file = readFile()
    input = readInput()
    output = compareListAndInput(file, input)
    writeOutput(output)