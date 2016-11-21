from sklearn.externals import joblib

file = open('vector-test.txt', 'r')
lines  = file.readlines()

fileResult = open('result-test.txt', 'r')
lineResults = fileResult.readlines()

clf = joblib.load('joblib.pkl')

X = []
for line in lines:
    X.append(eval(line.replace("\n", "")))

predict = clf.predict(X)

result = 0
for i in range(0, len(predict)):
    item = predict[i]
    if item == lineResults[i].replace("\n", ""):
        result+=1

print(result)

