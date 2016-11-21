from pycorenlp import StanfordCoreNLP
from preprocess import Preprocess
from dbconfig import cursor
from dbconfig import connection
from pair_token import PairToken
from convert_vector import ConvertVector

class CreatTranning:
    def __init__(self):
        cursor.execute("SELECT content FROM data")
        scripts = cursor.fetchall()

        fw = open('vector.txt', 'w')
        fresult = open('result.txt', 'w')
        mPreprocess = Preprocess()
        mPairedToken = PairToken()
        mConvertVector = ConvertVector()
        stanford = StanfordCoreNLP('http://localhost:9000')
        for script in scripts:
            # if type(script) is tuple:
            listToken = mPreprocess.exec(script[0])
            # else:
            #     listToken = mPreprocess.exec(script)

            listCouple = mPairedToken.exec(listToken)

            output = stanford.annotate(script[0], properties={'annotators': 'coref', 'outputFormat': 'json'})

            for mCoupleToken in listCouple:
                if self.checkCoreF(output['corefs'], mCoupleToken):
                    # fresult.write(str(1) + ' ' + mCoupleToken.np1.text + '  ' + mCoupleToken.np2.text)
                    fresult.write(str(1))
                    fresult.write('\n')
                else:
                    # fresult.write(str(-1) + ' ' + mCoupleToken.np1.text + '  ' + mCoupleToken.np2.text)
                    fresult.write(str(-1))
                    fresult.write('\n')

                vector = mConvertVector.exec(mCoupleToken)

                fw.write(str(vector))
                fw.write('\n')

    def checkInCoreF(self, coreF, np):
        for item in coreF:
            if item['startIndex'] <= np.startIndex and item['endIndex'] >= np.endIndex and item['sentNum'] == np.sentNum:
                return True
            if  np.startIndex <= item['startIndex'] and np.endIndex >= item['endIndex'] and item['sentNum'] == np.sentNum:
                return True
        return False

    def checkCoreF(self, listCoreF, mCoupleToken):
        np1 = mCoupleToken.np1
        np2 = mCoupleToken.np2
        for item in listCoreF:
            mCoreF = listCoreF[str(item)]
            if self.checkInCoreF(mCoreF, np1) and self.checkInCoreF(mCoreF, np2):
                return True
        return False


demo = CreatTranning()