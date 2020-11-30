import random

#print(random.randint(1, 5))
#print(random.choice(['apple', 'banana', 'cat']))

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.randint(0,49)*2

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    random.seed(0)
    return random.randint(4,10)*2

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randint(5,10)*2

# for i in range(1,100):
#    print(stochasticNumber())
print(int(random.random() * 10))
print(random.randrange(0, 10))
print(random.randint(0, 10))