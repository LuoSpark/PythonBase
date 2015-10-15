##ll = [1,2]
##
##def fun():
##    ll = [3,4]
##    print ll
##
##fun()
##
##print ll

##
##def count():
##    i = 0
##    fs = []
##    for i in range(1,4):
##        def f():
##            return i*i
##        fs.append(f)
##    return fs
##
##f1,f2,f3 = count()
##print f1(),f2(),f3()
##accAll = {1:"yi", 2:"er", 3:"3", 4:"4"}
person = [
    {
    "name":"luoxt",
    "firstName":"",
    "age":25,
    "sex":"male"
    },
    {
    "name":"wangjing",
    "firstName":"haha",
    "age":25,
    "sex":"female"
    },
    {
    "name":"liuxuehui",
    "firstName":"",
    "age": 24,
    "sex":"female"
    },
    {
    "name":"jiang",
    "firstName":"WW",
    "age": 26,
    "sex":"female"
    }
    ]

dictAge2Name = {}
for p in person:
    if p["firstName"] is None or p["firstName"] == "":
        listName = p["name"]
    else:
        listName = p["firstName"]

    print "listName:" , listName
    if dictAge2Name.has_key(p["age"]):
        dictAge2Name[p["age"]] += listName
##        dictAge2Name[p["age"]] = list(set(dictAge2Name[p["age"]]))
    else:
        dictAge2Name[p["age"]] = listName

    print dictAge2Name

    

    
    
