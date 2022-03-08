#Lists and dictionaries

def method1():
    l = []
    for n in range(10000):
        l = l + [n]
    print(l)

def method2():
    l = []
    for n in range(10000):
        l.append(n)
    print(l)

def method3():
    l = [n for n in range(10000)]
    print(l)

def method4():
    l = list(range(10000))    
    print(l)


