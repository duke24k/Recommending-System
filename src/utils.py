import numpy as np
import parse
np.set_printoptions(threshold='nan')


def constructRatingMatrix(data, metadata):
    user = int(metadata['users'])
    item = int(metadata['items'])
    # ratingMatrix = np.zeros((metadata['users'], metadata['items']))
    ratingMatrix = np.zeros((user, item))
    for i in data:
    	ratingMatrix[int(i[0])-1][int(i[1])-1] = i[2] 
    return ratingMatrix


def predictRating(similarity, ratingMatrix):
    prediction = np.copy(ratingMatrix)
    nousers = np.shape(ratingMatrix)[0]
    noitems = np.shape(ratingMatrix)[1]
    for item in xrange(noitems):
        s = np.copy(similarity[item])
        for userid in xrange(nousers):
            if prediction[userid][item]: continue
            p = s * ratingMatrix[userid]
            c = p / ratingMatrix[userid]
            c[np.isnan(c)] = 0
            SUM = np.sum(c)
            prediction[userid][item] = np.dot(ratingMatrix[userid], c)
            prediction[userid][item] = 0 if SUM == 0 else prediction[userid][item] / SUM
        # print item
    return prediction

def contentBoostPred(similarity, ratingMatrix, hw, sw, v):
    nousers = np.shape(ratingMatrix)[0]
    noitems = np.shape(ratingMatrix)[1]
    prediction = np.copy(ratingMatrix)
    user_mean = np.zeros((nousers))
    for i in xrange(nousers):
        user_mean = np.mean(v[i, :])
    for item in xrange(noitems):
        s = np.copy(similarity[item])
        for userid in xrange(nousers):
            if ratingMatrix[userid][item]: continue
            p = s * ratingMatrix[userid]
            c = p / ratingMatrix[userid]
            c[np.isnan(c)] = 0
            tmp = np.zeros((nousers))
            for i in xrange(nousers):
                tmp[i] = c[i] * hw[i]
            vv = np.zeros((nousers))
            for i in xrange(nousers):
                vv[i] = tmp[i] * (v[i][item] - user_mean[i])
            denominator = sw[userid] + np.sum(tmp)
            numerator = sw[userid] * (v[userid][item] - user_mean[userid]) + np.sum(vv)
            if denominator == 0:
                prediction[userid][item] = user_mean[userid]
            else:
                prediction[userid][item] = user_mean[userid] + numerator / denominator
    return prediction

# calculate SW factor, return a swMatrix
def calculateSW(ratingMatrix):
   nousers = np.shape(ratingMatrix)[0]
   noitems = np.shape(ratingMatrix)[1]
   swMatrix = np.zeros(nousers)
   maxValue = 2
   for item in xrange(noitems):
       for userid in xrange(nousers):
           if ratingMatrix[userid][item]:
               swMatrix[userid] += 1
   for userid in xrange(nousers):
       if swMatrix[userid] < 50:
           swMatrix[userid] = swMatrix[userid] * maxValue /50
       else:
           swMatrix[userid] = maxValue
   
   return swMatrix


