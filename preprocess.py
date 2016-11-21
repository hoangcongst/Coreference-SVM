import nltk
from nltk import word_tokenize


class Preprocess(object):
    def exec(self, input):
        sentences = input.split(".")
        toReturn = []

        for posSen in range(0, len(sentences)):
            sentence = sentences[posSen]
            text = word_tokenize(sentence)
            sent2 = nltk.pos_tag(text)

            parse_tree = nltk.ne_chunk(sent2, binary=True)
            # for item in parse_tree.subtrees():
            #     if item.label() == 'NE':
            #         toReturn.append(item.leaves())


            index = 1
            posInTree = 0
            for item in parse_tree:
                isSubject = False
                if posInTree + 1 < len(parse_tree) and type(parse_tree[posInTree + 1]) is not nltk.Tree:
                    if 'V' in parse_tree[posInTree + 1][1]:
                        isSubject = True
                if type(item) is not nltk.Tree:
                    # if 'PRP' in item[1] or 'NN' in item[1]:
                    if 'PRP' in item[1]:
                        # if item[1] == 'PRP' or item[1] == 'NN' or item[1] == 'NNP' or item[1] == 'JJ':
                        # if item[1] == 'PRP' or item[1] == 'NN' or item[1] == 'JJ':
                        mToken = Token(index, index + 1, item[0], item[1], isSubject, posSen + 1)
                        toReturn.append(mToken)
                    index += 1
                else:
                    text = ''
                    for leaf in item.leaves():
                        text += leaf[0] + ' '
                    mToken = Token(index, index + len(item.leaves()), text, item.label(), isSubject, posSen + 1)
                    toReturn.append(mToken)
                    index += len(item.leaves())
                posInTree+=1

                    #################### Analyze sentence structure ######################

        return toReturn


class Token:
    def __init__(self, startIndex, endIndex, text, pos, isSubject, sentNum):
        self.sentNum = sentNum  # sentence index
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.text = text
        self.pos = pos
        self.isSubject = isSubject
