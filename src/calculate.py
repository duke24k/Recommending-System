import similarity_functions as sf
import numpy as np
import parse
import utils



# calculate mean va
def getVa(ratingMatrix):
    va = []
    for i in range(len(ratingMatrix)):
        sum = 0
        for j in range(len(ratingMatrix[i])):
            sum += ratingMatrix[i][j]
        va.append(sum / len(ratingMatrix[i]))
    # np.savetxt('va.txt', va)
    return va
    print 'va done'

# calculate sgau
def getSgau(ratingMatrix):
    nousers = np.shape(ratingMatrix)[0]
    noitems = np.shape(ratingMatrix)[1]
    sgau = np.zeros((nousers, nousers))
    for i in range(nousers):
        for j in range(i + 1, nousers):
            count = 0
            for k in range(noitems):
                if ratingMatrix[i][k] != 0 and ratingMatrix[j][k] != 0:
                    count += 1
            if count >= 50:
                sgau[i][j] = 1
                sgau[j][i] = 1
            if count < 50:
                sgau[i][j] = float(count) / 50
                sgau[j][i] = float(count) / 50
    # np.savetxt('sgau.txt', sgau)
    return sgau
    print 'sgau done'

# calculate mi
def getMi(ratingMatrix):
    nousers = np.shape(ratingMatrix)[0]
    noitems = np.shape(ratingMatrix)[1]
    mi = []
    for i in range(nousers):
        count = 0
        for j in range(noitems):
            if ratingMatrix[i][j] != 0:
                count += 1
        if count >= 50:
            mi.append(1)
        if count < 50:
            mi.append(float(count) / 50)
    np.savetxt('../output/mi.txt', mi)
    print 'mi done'
    return mi
    # for i in range(len(mi)):
    #     print mi[i]


# calculate hmij
def getHmij(ratingMatrix):
    mi = getMi(ratingMatrix)
    nousers = np.shape(ratingMatrix)[0]
    noitems = np.shape(ratingMatrix)[1]
    hmij = np.zeros((nousers, nousers))
    for i in range(nousers):
        for j in range(nousers):
            temp = float(2 * mi[i] * mi[j] / (mi[i] + mi[j]))
            hmij[i][j] = temp
            hmij[j][i] = temp
    np.savetxt('../output/hmij.txt', hmij)
    print 'hmij done'
    return hmij
    # for i in range(nousers):
    #     for j in range(nousers):
    #         print hmij[i][j]

# calculate hwau
def getHwau(ratingMatrix):
    hmij = getHmij(ratingMatrix)
    nousers = np.shape(ratingMatrix)[0]
    noitems = np.shape(ratingMatrix)[1]
    hwau = np.zeros((nousers, nousers))
    for a in range(nousers):
        for u in range(nousers):
            hwau[a][u] = hmij[a][u] + 1
    np.savetxt('../output/hwau.txt', hwau)
    print 'hwau done'
    return hwau
    # for i in range(nousers):
    #     for j in range(nousers):
    #         print hwau[i][j]


# training, test, metadata = parse.load(1)
# ratingMatrix = utils.constructRatingMatrix(training, metadata)
# np.savetxt('ratingMatrix.txt', ratingMatrix)
# cal(ratingMatrix)
