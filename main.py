from sklearn.externals import joblib
from pair_token import PairToken
from convert_vector import ConvertVector
from preprocess import Preprocess
import re

text = "Donald John Trump (/ˈdɒnəld dʒɒn trʌmp/; born June 14, 1946) is an American businessman and the President-elect of the United States. In June 2015, Trump announced his candidacy for president as a Republican and quickly emerged as the front-runner for his party's nomination. His rivals suspended their campaigns in May 2016, and in July he was formally nominated at the party convention. Trump won the general election on November 8, 2016, by earning more Electoral College votes than Democratic nominee Hillary Clinton, who won the popular vote. As of November 2016 Trump's presidential transition is underway and he is scheduled to be inaugurated on January 20, 2017. At 70 years old, he will be the oldest person ever to assume the presidency."

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|[^a-zA-Z0-9\.\, ]')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

text = cleanhtml(text)
mPreprocess = Preprocess()
mPairedToken = PairToken()
mConvertVector = ConvertVector()
clf = joblib.load('joblib.pkl')
listVector = []

listPaired = mPairedToken.exec(mPreprocess.exec(text));
for item in listPaired:
    vector = mConvertVector.exec(item)
    listVector.append(vector)

predict = clf.predict(listVector)
for i in range(0, len(predict)):
    item = predict[i]
    print(listPaired[i].np1.text + ' ' + listPaired[i].np2.text + ' ' + item)