# add = lambda x, y : x + y

def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
doubled = map(double, sequence)
doubled = list(map(lambda x: x * 2, sequence))

print(doubled)
