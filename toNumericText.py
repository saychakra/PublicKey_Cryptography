# creating the dictionary for converting the letters to number in sequence
def textTonumeric(messageText):
    messageText = messageText.upper()
    
    letterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    valList = [i for i in range(1, 27)]
    alphaDict = dict(zip(letterList, valList))

    numericValueList = list()
    for i in range(len(messageText)):
        if (messageText[i] in alphaDict):
            numericValueList.append(alphaDict.get(messageText[i]))

    numericMessage = int("".join(str(i) for i in numericValueList))
    return numericMessage
