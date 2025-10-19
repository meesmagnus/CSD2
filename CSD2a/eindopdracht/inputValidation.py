import pygame #to test if requested audio is available

def inputValidation(question, inputType, range=[]):
    initInput = input(question)
    if inputType == "integer":
        try:
            int(initInput)
        except:
            return tryAgain(question, inputType, range)
        else:
            convInput = int(initInput)
            if convInput < range[0] or convInput > range[1]:
                return tryAgain(question, inputType, range)
            else:
                return convInput
    elif inputType == "float":
        try:
            float(initInput)
        except:
            return tryAgain(question, inputType, range)
        else:
            convInput = float(initInput)
            if convInput < range[0] or convInput > range[1]:
                return tryAgain(question, inputType, range)
            else:
                return convInput
    elif inputType == "DNA":
        try:
            convInput = initInput.split(" ", 3)
            soundAmount = int(convInput[0])
            measureAmount = int(convInput[1])
            stepAmount = int(convInput[2])
            seed = convInput[3]
            pygame.init()
            test = pygame.mixer.Sound('sounds/{}.wav'.format(soundAmount - 1))
            if stepAmount <= 0:
                return tryAgain(question, inputType, range)
        except:
            return tryAgain(question, inputType, range)
        else:
            convInput = initInput.split(" ", 3)
            convToIntInput = []
            convToIntInput.append(int(convInput[0]))
            convToIntInput.append(int(convInput[1]))
            convToIntInput.append(int(convInput[2]))
            convToIntInput.append(convInput[3])
            return convToIntInput
    else:
        print("wrong type")


def tryAgain(question, inputType, range):
    print("\nWrong input, try again")

    return inputValidation(question, inputType, range)
