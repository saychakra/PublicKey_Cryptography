# creating the dictionary for converting the letters to number in sequence
def textTonumeric(messageText):
    messageText = messageText.upper()
    
    letterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    valList = [i for i in range(0, 26)]
    alphaDict = dict(zip(letterList, valList))

    numericValueList = list()
    for i in range(len(messageText)):
        if (messageText[i] in alphaDict):
            numericValueList.append(alphaDict.get(messageText[i]))

    numericMessage = int("".join(str(i) for i in numericValueList))
    return numericMessage

def numericTotext(numericText):
    numericText = str(numericText)
    
    letterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    valList = [i for i in range(0, 26)]
    numDict = dict(zip(valList, letterList))
   
    textValueList = list()
    for i in range(len(numericText)):
        if (int(numericText[i]) in numDict):
            textValueList.append(numDict.get(int(numericText[i])))
    
    textMessage = "".join(str(i) for i in textValueList)
    return textMessage

#### testing code
# if __name__ == "__main__":
#     print(textTonumeric("hi"))
#     print(numericTotext(23))