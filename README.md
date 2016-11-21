Step 1: preprocessing input content from DB
Step 2: We have a list of mToken couple (processed) => use pair_token.py
Step 3: write to vecto.txt vecto of couples using convert_vector.py

    for script in db_scripts:
        paired_token = PairToken(script)
        for item in paired_token:
            vector = ConvertVector(item)
            f.write('vector.txt', vector)

            #value is classes, in this case is 0 (not co-ref) and 1 (co-ref)
            json = Stanford(script)


            f.write('class.txt', value)
