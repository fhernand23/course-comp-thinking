
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L)==0:
        return float('NaN')
    tot = 0
    for x in L:
        tot += len(x)
    mean = tot/float(len(L))
    tot = 0.0
    for x in L:
        tot += (len(x) - mean)**2
    std = (tot/len(L))**0.5
    return std

print(stdDevOfLengths(['a', 'z', 'p']))
print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))
print(stdDevOfLengths([]))