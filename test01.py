##ll = [1,2]
##
##def fun():
##    ll = [3,4]
##    print ll
##
##fun()
##
##print ll


def count():
    i = 0
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print f1(),f2(),f3()
