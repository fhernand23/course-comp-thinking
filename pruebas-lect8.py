import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    cant3same = 0
    for t in range(numTrials):
        # 6 balls (1 to 3 red, 4 to 6 green)
        numberList = [1,2,3,4,5,6]
        e1 = random.choice(numberList)
        numberList.remove(e1)
        # 5 balls
        e2 = random.choice(numberList)
        numberList.remove(e2)
        # 4 balls
        e3 = random.choice(numberList)
        numberList.remove(e3)
        if e1 <= 3 and e2 <=3 and e3 <= 3:
            cant3same+=1
        if e1 > 3 and e2 > 3 and e3 > 3:
            cant3same+=1

    return cant3same/numTrials

print(noReplacementSimulation(10000))