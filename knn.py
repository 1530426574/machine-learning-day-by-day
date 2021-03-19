from numpy import array,tile
import  operator


def create_data_set():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group ,labels

def classfy0(imput_x, dataset, labels, k):
    datasetsize = dataset.shape[0]
    diffmat = tile(imput_x, (datasetsize, 1)) - dataset
    sqdiffmat = diffmat**2
    sqdistances = sqdiffmat.sum(axis=1)
    distances = sqdiffmat**0.5
    sorteddistindicies = distances.argsort()
    classcount = {}
    for i in range(k):
        voteIlabel = labels[sorteddistindicies[i]]
        classcount[voteIlabel] = classcount.get(voteIlabel,0)+1
        sortedclasscount = sorted(classcount.iteritems(),key = operator.itemgetter(1),reverse=True)
    return sortedclasscount[0][0]







group,lables = create_data_set()
print(group)
print(lables)

