import numpy as np
import utils
import parse
import similarity_functions as sf
import calculate as cal
import math
import copy


def constructMatrix(data, metadata):
    user = int(metadata['users'])
    item = int(metadata['items'])
    ratingMatrix = np.zeros((item, user))
    for i in data:
        ratingMatrix[int(i[1]) - 1][int(i[0]) - 1] = i[2]
    return ratingMatrix


def itemsimMatrix():
    training, test, metadata = parse.load(1)
    ratingMatrix = constructMatrix(training, metadata)
    simMat = sf.cosineMatrix(ratingMatrix)
    np.savetxt('../output/siml.txt', simMat)
    predict = utils.predictRating(simMat, ratingMatrix)
    np.savetxt('../output/pred.txt', predict)

    userRating = utils.constructRatingMatrix(training, metadata)
    v = np.copy(userRating)
    user = int(metadata['users'])
    item = int(metadata['items'])
    for i in range(user):
        for j in range(item):
            if v[i][j] == 0:
                v[i][j] = predict[j][i]
    np.savetxt('../output/virt.txt', v)


if __name__ == '__main__':
    # itemsimMatrix()
    with open('../output/virt.txt') as f:
        v = np.loadtxt(f)
    print 'v done!'
    training, test, metadata = parse.load(1)
    ratingMatrix = constructMatrix(training, metadata)
    np.savetxt('../output/ratingMatrix.txt', ratingMatrix)
    hw = cal.getHwau(ratingMatrix.transpose())
    sw = utils.calculateSW(ratingMatrix.transpose())
    similarity = sf.cosineMatrix(v)
    simMat = sf.cosineMatrix(v.transpose())
    np.savetxt('../output/similar.txt', simMat)
    print 'sim done!'
    # with open('../output/hwau.txt') as f:
    #     hw = np.loadtxt(f)
    # with open('../output/sw.txt') as f:
    #     sw = np.loadtxt(f)
    # with open('../output/siml.txt') as f:
    #     simMat = np.loadtxt(f)
    # prediction = utils.contentBoostPred(simMat, ratingMatrix, hw, sw, v)
    # print 'prediction done!'
    # np.savetxt('../output/pred.txt', prediction)
    # print 'prediction done'