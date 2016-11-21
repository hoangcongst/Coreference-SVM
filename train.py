from preprocess import Preprocess
from sklearn import svm
from sklearn.externals import joblib

mPreprocess = Preprocess()

fmodel = open('model.txt', 'w')
file = open('vector.txt', 'r')
lines  = file.readlines()

X = []
for line in lines:
    X.append(eval(line.replace("\n", "")))

fileResults = open('result.txt', 'r')
lines  = fileResults.readlines()

Y = []
for line in lines:
    Y.append(line.replace("\n", ""))
clf = svm.LinearSVC(C=1.0)

clf.fit(X, Y)

filename = 'joblib.pkl'
_ = joblib.dump(clf, filename, compress=9)
    # model = gensim.models.Word2Vec.load_word2vec_format('~/PycharmProjects/GoogleNews-vectors-negative300.bin', binary=True)
# model.init_sims(replace=True)
# print(model.most_similar(positive=['woman', 'king'], negative=['man']))
# print(model['Lincoln'])