import numpy as np
import parse
from time import clock;
import pandas
np.set_printoptions(threshold='nan')

def makeDic(data):
    dataDic = {}
    for i in data:
        dataDic.setdefault(i[0], {}).update({i[1]: i[2]})
    return dataDic

def makeArray(dic):
    arr = []
    for user,items in dic.iteritems():
        for k,v in items.iteritems():
            row = []
            row.append(user)
            row.append(k)
            row.append(v)
            arr.append(row)
    return arr

print "test"
training, test, metadata = parse.load(1)
start = clock()
d = makeDic(training)
for k,v in d.items():
    print "user %s" %k, v
arr = makeArray(d)
end = clock()
print "time: %s" %(end - start)
# for i in arr:
#     print i