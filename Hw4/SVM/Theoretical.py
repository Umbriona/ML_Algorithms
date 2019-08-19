import numpy as np
import matplotlib.pyplot as plt

def FormatColorVector(Y):
    cVec=[]
    for i in Y:
        if(i == -1):
            cVec.append('red')
        else:
            cVec.append('blue')
    return cVec

Y = np.array([1,1,1,-1,-1,-1])
X = np.array([[2,2],[4,4],[4,0],[0,0],[2,0],[0,2]])

D = plt.scatter(X[:,0],X[:,1], c = FormatColorVector(Y),label='Data')
H, = plt.plot([0,3],[3,0],'--',c='k',label='Hyperplane')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Hard margin SVM')
plt.legend(handles = [D,H] ,loc=1)
plt.show()