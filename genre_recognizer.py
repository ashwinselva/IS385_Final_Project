from python_speech_features import mfcc
import scipy.io.wavfile as wav
import numpy as np
import os
import operator
import numpy as np
from sklearn.model_selection import train_test_split
import librosa.display



def dis(A , B , k ):
    dis =0
    dis = np.trace(np.dot(np.linalg.inv(B[1]), A[1]))
    dis+=(np.dot(np.dot((B[0]-A[0]).transpose() , np.linalg.inv(B[1])) , B[0]-A[0] ))
    dis+= np.log(np.linalg.det(A[1])) - np.log(np.linalg.det(B[1]))
    dis-= k
    return dis


def getNeighbors(X,read_data,  k):
    diss = []
    for x in range (len(X)):
        dist = dis(X[x],read_data, k )+ dis(read_data,X[x], k)
        diss.append((X[x][2],dist))
    diss.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(diss[x][0])
    return neighbors



def findNeighbours(neighbors):
    temp = {}
    for x in range(len(neighbors)):
        real = neighbors[x]
        if real in temp:
            temp[real]+=1
        else:
            temp[real]=1

    sorter = sorted(temp.items(), key = operator.itemgetter(1),reverse=True)
    return sorter[0][0]


def calc_acc(Y, pred):
    correct = 0
    for x in range (len(Y)):
        if Y[x][-1]==pred[x]:
            correct+=1
    return 1.0*correct/len(Y)


d=[]
directory = "./genres"
i=0
fol=[]
for root, dir, files in os.walk("./genres"):
    fol=dir
    i+=1
    if(i>=1):
        break
j=0
k=0
for folder in fol:
    k+=1
    for file in os.listdir(directory+'/'+folder):
        (rate,sig) =wav.read(directory+"/"+folder+"/"+file)
        feature_vector = mfcc(sig,rate,winlen=0.020, appendEnergy = False)
        cov_matrix = np.cov(np.matrix.transpose(feature_vector))
        mean_matrix = mfcc_feat.mean(0)
        feature = (mean_matrix, cov_matrix , folder)
        j+=1
        d.append(feature)


dataset = []
def loadDataset(d):
    X,Y = train_test_split(d, test_size=0.3, train_size=0.7)
    return X, Y

X,Y = loadDataset(d)

pred = []
for x in range (len(Y)):
    pred.append(findNeighbours(getNeighbors(X,Y[x] , 5)))
accuracy1 = calc_acc(Y, pred)
print("accuracy of the dataset=",accuracy1)
(rate,sig)=wav.read("test1.wav")
feature_vector=mfcc(sig,rate,winlen=0.04,appendEnergy=False)
cov_matrix = np.cov(np.matrix.transpose(mfcc_feat))
mean_matrix = feature_vector.mean(0)
feature=(mean_matrix,covariance,0)
genre=findNeighbours(getNeighbors(d ,feature , 3))
print("\n\nPredicted Genre:",genre)


librosa.display.specshow(feature_vector, sr=rate, x_axis='time')


import IPython.display as ipd
ipd.Audio('test1.wav') # load a local WAV file



