import time, HumanTime

def mainH(initialPercentage, capacity, inc):
    initialTime = time.time()
    UI = True
    while UI:
        tmp = input('Enter done when finished:\t')
        if tmp.lower() == 'done':
           UI = False
    finalTime = time.time()
    tmp = input('What is the new percentage?\t')
    UI = True
    lastWasNumeric = False
    while UI:
        try:
            finalPercentage = eval(tmp)
            lastWasNumeric = True
            while finalPercentage > initialPercentage:
                if lastWasNumeric:
                    tmp = input("Your final percentage was lower than your initial percentage.\nWhat is the new percentage?\t")
                else:
                    tmp = input("Your input cannot be understood.\nWhat is the new percentage?\t")
                try:
                    finalPercentage = eval(tmp)
                    lastWasNumeric = True
                except:
                    lastWasNumeric = False
            UI = False
        except:
            tmp = input('Your value was non-numerical.\nWhat is the new percentage?\t')
    totalTimeElapsed = finalTime - initialTime
    deltaPerc = initialPercentage - finalPercentage 
    totalTime = (totalTimeElapsed)/((deltaPerc)/100)
    totalTimeElapsedStr = HumanTime.TimeAutoShort(finalTime - initialTime, 2)
    majorityTotalTime = .7*totalTime
    error = totalTime/(initialPercentage - finalPercentage) * inc
    majorityError = totalTime/((initialPercentage - finalPercentage)*10/7)
    totalTimeStr = HumanTime.TimeAutoShort(totalTime, 2)
    majorityTimeStr = HumanTime.TimeAutoShort(majorityTotalTime, 2)
    errorStr = HumanTime.TimeAutoShort(error, 2)
    majorityErrorStr = HumanTime.TimeAutoShort(majorityError, 2)
    bestCase = HumanTime.TimeAutoShort(totalTime - error, 2)
    worseCase = HumanTime.TimeAutoShort(totalTime + error, 2)
    majorityBestCase = HumanTime.TimeAutoShort(majorityTotalTime - majorityError, 2)
    majorityWorseCase = HumanTime.TimeAutoShort(majorityTotalTime + majorityError, 2)
    lowerCurrentEstimate = (capacity / 1000) / ((totalTime + error) / 3600)
    upperCurrentEstimate = (capacity / 1000) / ((totalTime - error) / 3600)
    print(100 * "-" + f'\nTotal time elapsed:  {totalTimeElapsedStr}\nAt this rate, a full charge should deplete in {totalTimeStr} +/- {errorStr}.\nIt should go from 70% to 0% in {majorityTimeStr} +/- {majorityErrorStr}.\nFrom a full charge, it will take between {bestCase} and {worseCase}.\nFrom 70% - 0% it will take between {majorityBestCase} and {majorityWorseCase}\nIt will loose 1% every {HumanTime.TimeAutoShort(totalTime/100, 2)}.\nIt will loose 1 mAh every {HumanTime.TimeAutoShort(totalTime/capacity, 2)}.\nBetween {lowerCurrentEstimate:.2f} and {upperCurrentEstimate:.2f} Amps were pulled from the battery.\n' + 100 * "-")
def main(capacity): # capacity is in mAh and is the size of the battery
    "This function takes as a paramater the capacity of your battery in mAh"
    UI = True
    while UI:
        try:
            inc = eval(input('How much does your percentage incriment by?\t'))
            UI = False
        except:
            pass
    UI = True
    while UI:
        try:
            tmp = eval(input('What is the current percentage?\t'))
            UI = False
        except:
            pass
    mainH(tmp, capacity, inc)
def mainHelper():
    while True:
        ui = input("How much does your battery store in mAh?\t")
        try:
            ui = eval(ui)
            break
        except:
            print("Your input cannot be recognized as a number")
    main(ui)
#main(2815) # For iPhone 12
#main(1700) # For Puffco Peak Pro
mainHelper() 
