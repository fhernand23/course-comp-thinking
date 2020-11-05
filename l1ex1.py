

class Elem(object):
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return self.name + ": <" + str(self.weight) + ", " + str(self.value) + ">"


def metric1(item):
    return item.value / item.weight


def metric2(item):
    return -item.weight


def metric3(item):
    return item.value


def alg1(elements, maxw, metric):
    curw = 0
    knap = []
    elements.sort(key=metric, reverse=True)
    for el in elements:
        if (curw + el.weight <= maxw):
            knap.append(el)
            curw += el.weight
    print("alg 1 result")
    for c in knap:
        print(c.name)
    print("weight " + str(sum(c.weight for c in knap)))
    print("value " + str(sum(c.value for c in knap)))
    print("weight remain " + str(maxw - sum(c.weight for c in knap)))



e1 = elem(name="dirt", weight=4, value=0)
e2 = elem(name="computer", weight=10, value=30)
e3 = elem(name="fork", weight=5, value=10)

elements = [e1, e2, e3]
#prob_set = {"weight": 0, "value": -10}
max_weight = 14

alg1(elements, max_weight, metric1)
alg1(elements, max_weight, metric2)
alg1(elements, max_weight, metric3)
