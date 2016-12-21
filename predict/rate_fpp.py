import numpy as np
from sklearn import decomposition
from sklearn.externals import joblib
from sklearn import linear_model
from sklearn import svm
import sklearn
import argparse
import os
import generateFeatures

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file',  type=str, nargs='?', default='./15.jpg')
regr = joblib.load("test.model")
pca = joblib.load("test.pca")
#pca = decomposition.PCA()
# n_components=20)

args = parser.parse_args()

img = args.file

print img
#geneStr = "python generateFeatures.py -f" + ' ./landmarks/'+img[0:-4]+'/landmarks.txt -od ./faceResult/'+img[0:-4]
#os.system(geneStr)


def predict(picPath):
	features = pca.transform(generateFeatures.generate(picPath))
	result = regr.predict(features)
	print(picPath)
	return result[-1]

#ftpath = './faceResult/'+img[0:-4]+'/features_ALL.txt'
#features = np.loadtxt(ftpath, delimiter=',')
print(predict(img))
