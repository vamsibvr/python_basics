s="Hello world"
print s
def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    return l
print f(2)
print f(3, [1,2,3])
