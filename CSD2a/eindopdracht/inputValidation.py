import pygame #to test if requested audio is available

def inputValidation(question, type, range=[]):
    initInput = input(question)
    if type == "integer":
        try:
            int(initInput)
        except:
            return tryAgain(question, type, range)
        else:
            convInput = int(initInput)
            if convInput < range[0] or convInput > range[1]:
                return tryAgain(question, type, range)
            else:
                return convInput
    elif type == "float":
        try:
            float(initInput)
        except:
            return tryAgain(question, type, range)
        else:
            convInput = float(initInput)
            if convInput < range[0] or convInput > range[1]:
                return tryAgain(question, type, range)
            else:
                return convInput
    elif type == "DNA":
        try:
            convInput = initInput.split(" ", 2)
            soundAmount = int(convInput[0])
            stepAmount = int(convInput[1])
            seed = convInput[2]
            pygame.init()
            test = pygame.mixer.Sound('sounds/{}.wav'.format(soundAmount - 1))
            if stepAmount <= 0:
                return tryAgain(question, type, range)
        except:
            return tryAgain(question, type, range)
        else:
            convInput = initInput.split(" ", 2)
            convToIntInput = []
            convToIntInput.append(int(convInput[0]))
            convToIntInput.append(int(convInput[1]))
            convToIntInput.append(convInput[2])
            return convToIntInput


def tryAgain(question, type, range):
    print("\nWrong input, try again")
    inputValidation(question, type, range)
