#ghep cap token
# input: list Token object
# output: list pair of Token objects

class PairToken:
    def exec(self, listToken):
        listCouple = []
        lenListToken = len(listToken)
        for i in range(0, lenListToken):
            for j in range(i+1, lenListToken):
                listCouple.append(CoupleToken(listToken[i], listToken[j]))
        return listCouple

class CoupleToken:
    def __init__(self, np1, np2):
        self.np1 = np1
        self.np2 = np2