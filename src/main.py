import numpy as np
import parse
import utils
from time import clock
import similarity_functions as sf
np.set_printoptions(threshold='nan')


def main(load=True, setno=0):
    training, test, metadata = parse.load(setno)
    if not load:
        ratingMatrix = utils.constructRatingMatrix(training, metadata)
        start = clock()
        # similarity = sf.pearsonMatrix(ratingMatrix)
        similarity = sf.pearsonMatrix(ratingMatrix)
        end = clock()
        print 'run time: %d' % (end - start)
        np.savetxt('../output/siml/similarity%s.txt' % (setno), similarity)
        print "similarity done"
        prediction = utils.predictRating(similarity, ratingMatrix)
        testUserId = 0
        testArray = np.copy(prediction[testUserId])
        utils.quicksort(testArray,0,testArray.size-1)
        numOfRecommend = 3
        topKResults = np.zeros(numOfRecommend)
        for i in range(numOfRecommend):
            topKResults[i] = testArray[testArray.size-1-i]
        for index in range(testArray.size):
            for result in topKResults:
                if prediction[testUserId][index] == result:
                    print index
        np.savetxt('../output/pred/prediction%s.txt' % (setno), prediction)
        print "prediction done"
    else:
        with open('../dataset/similarity.txt') as f:
            similarity = np.loadtxt(f)
        with open('../dataset/prediction.txt') as f:
            prediction = np.loadtxt(f)
    
    # import pdb; pdb.set_trace()
    predictionOnTest = prediction[test[:, 0].astype(int) - 1, test[:, 1].astype(int)-1]
    error = predictionOnTest - test[:, 2]
    return np.abs(error).mean()

if __name__ == '__main__':
    for i in xrange(1, 6):
        file = open('../output/result.txt', 'a+')
        mean = main(False, setno=i)
        print mean
        file.write('%s\n' % mean)
        file.close()
