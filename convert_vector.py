import nltk
from nltk import word_tokenize


class ConvertVector(object):
    def exec(self, mCoupleToken):
        np1 = mCoupleToken.np1
        np2 = mCoupleToken.np2

        type1 = 1
        subject1 = 0
        job1 = 0
        gender1 = -1
        number1 = -1
        type2 = 1
        subject2 = 0
        job2 = 0
        gender2 = -1  # he => 1, she => 2, they || NE => -1
        number2 = -1
        both_subject = 0
        both_ne = 0
        both_n = 0
        both_pro = 0
        str_match = 0
        sub_str_match = 0
        gender = 0
        number = 0
        agreement = -1
        # apposittive = 0
        sen_distance = 0
        pos_in_sen_distance = -1

        # type1 job1
        if (np1.pos == 'NE'):
            type1 = 1
            job1 = 0
        elif ('PRP' in np1.pos):
            type1 = 2
            job1 = 0
        else:
            type1 = 3
            job1 = 1

        # subject1
        if np1.isSubject is True:
            subject1 = 1
        # gender1
        if ('PRP' in np1.pos and (np1.text == 'he' or np1.text == 'his')):
            gender1 = 1
        elif ('PRP' in np1.pos and (np1.text == 'she' or np1.text == 'her')):
            gender1 = 0
        else:
            gender1 = -1

        # number1
        if ('PRP' in np1.pos and (np1.text == 'we' or np1.text == 'us' or np1.text == 'they' or np1.text == 'them'
                                  or np1.text == 'thier' or np1.text == 'our')):
            number1 = 2
        elif ('PRP' in np1.pos and (np1.text == 'she' or np1.text == 'her' or np1.text == 'he'
                                    or np1.text == 'his' or np1.text == 'him'
                                    or np1.text == 'it' or np1.text == 'its' or np1.text == 'I' or np1.text == 'me')):
            number1 = 1  # so luong = 1
        else:
            number1 = 0  # khong xac dinh

    ############################################ NP2 ##############################################
        # type2 job2
        if (np2.pos == 'NE'):
            type2 = 1
            job2 = 0
        elif ('PRP' in np2.pos):
            type2 = 2
            job2 = 0
        else:
            type2 = 3
            job2 = 1

        # subject2
        if np2.isSubject is True:
            subject2 = 1

        # gender2
        if ('PRP' in np2.pos and (np2.text == 'he' or np2.text == 'his')):
            gender2 = 1
        elif ('PRP' in np2.pos and (np2.text == 'she' or np2.text == 'her')):
            gender2 = 0
        else:
            gender2 = -1

        # number
        if ('PRP' in np2.pos and (np2.text == 'we' or np2.text == 'us' or np2.text == 'they' or np2.text == 'them'
                                  or np2.text == 'thier' or np2.text == 'our')):
            number2 = 2
        elif ('PRP' in np2.pos and (np2.text == 'she' or np2.text == 'her' or np2.text == 'he'
                                    or np2.text == 'his' or np2.text == 'him'
                                    or np2.text == 'it' or np2.text == 'its' or np2.text == 'I' or np2.text == 'me')):
            number2 = 1  # so luong = 1
        else:
            number2 = 0  # khong xac dinh

        ######################################### END NP2 ##################################################
        if(np1.pos == 'NE' and np2.pos == 'NE'):
            both_ne = 1

        if('NN' in np1.pos and 'NN' in np2.pos):
            both_n = 1

        if('PRP' in np1.pos and 'PRP' in np2.pos):
            both_pro = 1

        if(np1.text == np2.text):
            str_match = 1

        if(np1.text in np2.text or np2.text in np1.text):
            sub_str_match = 1

        if(gender1 == gender2):
            gender = 1

        if subject1 == 1 and subject2 == 1:
            both_subject = 1

        if(number1 == number2):
            number = 1

        if(gender == 1 and number == 1):
            agreement = 1

        sen_distance = abs(np1.sentNum - np2.sentNum)
        if(np1.sentNum == np2.sentNum):
            pos_in_sen_distance = abs(np1.startIndex - np2.startIndex)

        return [type1, subject1, job1, gender1, number1, type2, subject2, job2, gender2, number2, both_subject, both_ne,
                both_n, both_pro, str_match, sub_str_match, gender, number, agreement, sen_distance,
                pos_in_sen_distance]
