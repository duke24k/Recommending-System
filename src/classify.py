import numpy as np
np.seterr(divide='ignore', invalid='ignore')


def loadFile(filename):
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        cur = line.strip().split('|')
        # res = cur[5:]
        res = cur[0:25]
        dataMat.append(res)
    return dataMat


def distEclud(vecA, vecB):
    c = vecA - vecB
    return np.sqrt(np.sum(np.power(c, 2)))


def randCent(dataSet, k):
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k, n)))
    for j in range(n):
        minJ = np.min(dataSet[:, j])
        maxJ = np.max(dataSet[:, j])
        rangeJ = np.float(maxJ - minJ)
        centroids[:, j] = np.mat(minJ + rangeJ * np.random.rand(k, 1))
    return centroids


def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m, 2)))  #create mat to assign data points
                                         #to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):  #for each data point assign it to the closest centroid
            minDist = np.inf
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist**2
        # print centroids
        for cent in range(k):  #recalculate centroids
            ptsInClust = dataSet[np.nonzero(clusterAssment[:, 0].A == cent)[0]]  #get all the point in this cluster
            centroids[cent, :] = np.mean(ptsInClust, axis=0)  #assign centroid to mean
    return centroids, clusterAssment


def run():
    filename = '../dataset/source.txt'
    datas = loadFile(filename)
    row = np.shape(datas)[0]
    col = np.shape(datas)[1]
    dataMat = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            if j <= 5:
                dataMat[i][j] = float(datas[i][j]) / 10.0
            elif 6 <= j <= 18:
                dataMat[i][j] = float(datas[i][j])
            else:
                dataMat[i][j] = float(datas[i][j]) / 30.0
    minC = np.inf
    minK = 0
    minClust = np.mat(np.zeros((col, 2)))
    minCenter = None
    for k in range(1, 35):
        centroids, clusterAssment = kMeans(dataMat, k, distEclud, randCent)
        print k
        c = np.sum(clusterAssment[:, 1]) / row + 0.05 * k
        print c
        if minC > c:
            minK = k
            minClust = clusterAssment
            minCenter = centroids
            minC = c
    print "result:"
    print minK
    for item in minClust:
        print '%d\t%f' % (item[:, 0], item[:, 1])


if __name__ == '__main__':
    run()