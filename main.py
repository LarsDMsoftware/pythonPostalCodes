def readFile():
    file = open('postalCodes.txt', 'r')
    lines = file.readlines()
    formattedDict = {}
    for line in lines:
        s = line.strip().split('\t')
        if s[0] in formattedDict.keys():
            formattedDict[s[0]] = formattedDict[s[0]] + "," + s[1]
        else:
            formattedDict[s[0]] = s[1]
    return formattedDict

def readInput():
    validInput = False
    postCode = 0
    while not validInput:
        try:
            postCode = input('Give in a valid postcode: \n')
            if postCode.isdigit() and len(postCode) == 4:
                validInput = True
            else:
                validInput = False
                print('Invalid input, enter a 4 digit Belgian postal code.')
        except: 
            print('Error')
    return postCode

def compareListAndInput(file, input):
    listOfMatchingPostCodes = []
    allowed_chars =  input 
    validationStrings = file.keys()
    for s in validationStrings:
        x = all(ch in allowed_chars for ch in s)
        if x:
            listOfMatchingPostCodes.append(formatOutput(s, file[s]))
        else:
            continue
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