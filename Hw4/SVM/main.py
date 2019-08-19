import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt

def PlotSupportVectors(clf,X,Y,linestyle,label):
    index = clf.support_
    w = clf.support_vectors_
    classes = np.zeros(len(index))
    for i in range(len(index)):
        classes[i] = Y[index[i]]
    color = FormatColorVector(classes)
    #plt.legend('Supportvector')
    return w

def plot_hyperplane(clf, min_x, max_x, linestyle, label):
    # get the separating hyperplane
    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(min_x , max_x )  # make sure the line is long enough
    yy = lambda x: a * x - (clf.intercept_[0]) / w[1]
    return xx,yy

    #plt.legend('Desitionboundery')


def FormatColorVector(Y):
    cVec=[]
    for i in Y:
        if(i == -1):
            cVec.append('red')
        else:
            cVec.append('blue')
    return cVec

data = np.loadtxt('d1.txt')
X = data[:,:2]
Y = data[:,-1]

clf = SVC(kernel='linear',C=3)
clf.fit(X, Y)

min_x = np.amin(X[:,0])-1
max_x = np.amax(X[:,0])+1
linestyle = '--'
label='Classificationline'


xx,yy = plot_hyperplane(clf, min_x, max_x, linestyle, label)
w = PlotSupportVectors(clf,X,Y,'-','Support vector ')
scatter_data = plt.scatter(X[:,0],X[:,1],c=FormatColorVector(Y),label='Data')
desitionBoundary = plt.plot(xx, yy(xx), linestyle, label='Classificationline')

supportVector = plt.scatter(w[:, 0], w[:, 1], s=80, facecolor='none', edgecolor= 'k', alpha=1, label='Support vector',zorder=10)
print('Bias for the classifyer is', clf.intercept_)

first_legend= plt.legend(handles=[supportVector,scatter_data],loc=1)

# Add the legend manually to the current Axes.
ax = plt.gca().add_artist(first_legend)
plt.legend(handles = desitionBoundary,loc=2)
plt.show()