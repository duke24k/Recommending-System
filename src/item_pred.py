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


def content_boosted(setno=0):
    training, test, metadata = parse.load(setno)
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

    np.savetxt('../output/ratingMatrix.txt', ratingMatrix)
    hw = cal.getHwau(ratingMatrix.transpose())
    sw = utils.calculateSW(ratingMatrix.transpose())
    simMat = sf.cosineMatrix(ratingMatrix)
    np.savetxt('../output/similar.txt', simMat)
    print 'sim done!'

    prediction = utils.contentBoostPred(simMat, ratingMatrix, hw, sw, v)
    np.savetxt('../output/predict.txt', prediction)
    print 'prediction done!'

    predictionOnTest = prediction[test[:, 0].astype(int) - 1, test[:, 1].astype(int) - 1]
    error = predictionOnTest - test[:, 2]
    return np.abs(error).mean()



if __name__ == '__main__':
    for i in xrange(1, 6):
        file = open('../output/result.txt', 'a+')
        mean = content_boosted(setno=i)
        print mean
        file.write('%s\n' % mean)
        file.close()