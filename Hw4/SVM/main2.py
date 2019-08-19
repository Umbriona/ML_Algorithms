import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm


def FindWrongClass(clf,y,X):
    listOfMissClassificationsX = []
    listOfMissClassificationsY = []
    test = clf.predict(X)
    for i in range(len(X[:,0])):
        if(test[i] != y[i]):
            listOfMissClassificationsX.append(X[i, 0])
            listOfMissClassificationsY.append(X[i, 1])
    return [listOfMissClassificationsX,listOfMissClassificationsY]

def FormatColorVector(Y):
    cVec=[]
    for i in Y:
        if(i == -1):
            cVec.append('red')
        else:
            cVec.append('blue')
    return cVec

data = np.loadtxt('d2.txt')
X = data[:,:2]
y = data[:,-1]
n_sample = len(X)



# fit the model
for fig_num, kernel in enumerate(('linear', 'rbf', 'poly')):
    clf = svm.SVC(kernel=kernel, gamma=5,degree=2)
    clf.fit(X, y)

    plt.figure(fig_num)
    plt.clf()
    plt.scatter(X[:, 0], X[:, 1], zorder=10, c=FormatColorVector(y), s=20)
    plt.axis('tight')
    x_min = X[:, 0].min()
    x_max = X[:, 0].max()
    y_min = X[:, 1].min()
    y_max = X[:, 1].max()

    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(XX.shape)
    plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.cool)
    mX,mY = FindWrongClass(clf,y,X)

    miss = plt.scatter(mX, mY, s=80, facecolor='none', edgecolor='k', alpha=1,label='Miss classification', zorder=10)
    plt.legend(handles=[miss], loc=1)
    plt.title(kernel)
plt.show()