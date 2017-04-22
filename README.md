# Recommendation system

## Overview
This system generates recommended work positions that is suitable for this user. The results are based on the similarity of the users and other users. Due to the reason of limited data source of user features, our research of the algorithms mainly focused on an open source project, movie recommendation system, which supplies sufficient data for training and test. From an comprehensive view we conclude that our theory and algorithms are feasible while at the same time there are still some aspects expected to improve.

## Theories
The algorithm we used is based on [Collaborative Filtering](https://en.wikipedia.org/wiki/Collaborative_filtering) algorithm. The CF algorithm contains following steps:

1. Collect users’ preferences
2. Find similar users or items
3. Make recommendation

The flaw of CF algorithm is that, when users have few preferences, the preference matrix would become sparse, which will affect the accuracy of similarity. To improve the accuracy, we introduce an algorithm called [Content Boosted Collaborative Filtering](http://www.aaai.org/Papers/AAAI/2002/AAAI02-029.pdf). 

We create a pseudo user-ratings vector for every user u in database, which consists of the item ratings provided by the user u, where available, and those predicted by the content-based predictor otherwise.

To incorporate our confidence in our correlations, we weight users using the Harmonic Mean Weighting factor. In our approach, we also add the pseudo active user to the neighborhood.  However,  we  may  want  to  give  the  pseudo  active user more importance than the other neighbors. In other words, we would like to increase the confidence we place in the pure-content predictions for the active user.  We do this by incorporating a Self Weighting factor in the final prediction. Combining the above two weighting schemes, we get the final CBCF prediction.

## Functions
1. [calculate.py](https://github.com/John443/Recommending-System/blob/master/src/calculate.py) -- calculate factors like Harmonic hybrid correlation weight, Harmonic Mean weighting factor,etc.
2. [classfy.py](https://github.com/John443/Recommending-System/blob/master/src/classify.py) -- Load user data from file then cluster data with k-means, output the result.
3. [item_pred.py](https://github.com/John443/Recommending-System/blob/master/src/item_pred.py) -- Load user test data, construct rating matrix and implement Content-Boosted Collaborative Filtering method. Compare the calculation result with  dataset and output error.
4. [main.py](https://github.com/John443/Recommending-System/blob/master/src/main.py) -- Boot up the program.
5. [parse.py](https://github.com/John443/Recommending-System/blob/master/src/parse.py) -- Load data and generate proper data format
6. [similarity_functions.py](https://github.com/John443/Recommending-System/blob/master/src/similarity_functions.py) -- Implement three methods to generate matrix and find similar vectors: pearson correlation,cosine similarity and adjusted cosine similarity.
7. [utils.py](https://github.com/John443/Recommending-System/blob/master/src/utils.py) -- Construct rating matrix and predict rating matrix and apply content boosted prediction algorithm. 

## Instruction
First, call classify.py to divide the users’ samples into different systemalizations. Second, check the sparseness of the samples and decide the algorithm will be used. If the sample is sparse, then call item_pred.py to use CBCF to get recommendation, otherwise use main.py to use CB to recommend jobs.

## Dataset
We use dataset from [the MovieLens web site](https://movielens.org/) during the seven-month period from September 19th, 1997 through April 22nd, 1998.