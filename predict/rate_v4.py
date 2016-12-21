import numpy as np

from sklearn import decomposition
from sklearn.externals import joblib
from sklearn import linear_model
from sklearn import svm
import sklearn
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file',  type=str, nargs='?', default='./*.jpg')
regr = joblib.load("test.model")
pca = joblib.load("test.pca")
#pca = decomposition.PCA()
# n_components=20)

args = parser.parse_args()

img = args.file

comStr = "./CLM-framework/bin/SimpleCLMImg -f " + img + " -ofdir faceResult/"+ img[0:-4]
os.system(comStr)
mkdirStr = "mkdir ./landmarks/"+img[0:-4]
os.system(mkdirStr)
des_file = open("./landmarks/"+img[0:-4]+"/landmarks.txt","a+")
file_list = os.listdir('./faceResult/'+img[0:-4])
filePath = './faceResult/'+img[0:-4]+'/'+file_list[0]
try:
    file = open(filePath, "r+")
except:
    print("no file")
lines = file.readlines()
newStr = ''
for line in lines:
    if lines.index(line) < 3 or lines.index(line) == len(lines)-1:
        continue

    line = line.strip() + " "
    newStr += line
newStr = newStr.replace(' ', ', ')
data = newStr.split(',')
des_file.write(newStr+'\n')
file.close()
des_file.close()

geneStr = "python generateFeatures.py -f" + ' ./landmarks/'+img[0:-4]+'/landmarks.txt -od ./faceResult/'+img[0:-4]
os.system(geneStr)


def predict(feature_list):
	result = regr.predict(feature_list)
	return result

#print(predict(features))
ftpath = './faceResult/'+img[0:-4]+'/features_ALL.txt'
features = np.loadtxt(ftpath, delimiter=',')
print(features.shape)
#pca.fit(features)
print(features.shape)
features = pca.transform(features)
print(features.shape)
print(predict(features))
