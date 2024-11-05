import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

def runUncertain():
    # CC	coordinating conjunction
    # CD	cardinal digit
    # DT	determiner
    # EX	existential there (like: "there is" ... think of it like "there exists")
    # FW	foreign word
    # IN	preposition/subordinating conjunction
    # JJ	adjective	'big'
    # JJR	adjective, comparative	'bigger'
    # JJS	adjective, superlative	'biggest'
    # LS	list marker	1)
    # MD	modal	could, will
    # NN	noun, singular 'desk'
    # NNS	noun plural	'desks'
    # NNP	proper noun, singular	'Harrison'
    # NNPS	proper noun, plural	'Americans'
    # PDT	predeterminer	'all the kids'
    # POS	possessive ending	parent\'s
    # PRP	personal pronoun	I, he, she
    # PRP$	possessive pronoun	my, his, hers
    # RB	adverb	very, silently,
    # RBR	adverb, comparative	better
    # RBS	adverb, superlative	best
    # RP	particle	give up
    # TO	to	go 'to' the store.
    # UH	interjection	errrrrrrrm
    # VB	verb, base form	take
    # VBD	verb, past tense	took
    # VBG	verb, gerund/present participle	taking
    # VBN	verb, past participle	taken
    # VBP	verb, sing. present, non-3d	take
    # VBZ	verb, 3rd person sing. present	takes
    # WDT	wh-determiner	which
    # WP	wh-pronoun	who, what
    # WP$	possessive wh-pronoun	whose
    # WRB	wh-abverb	where, when

    # assign text file to variable
    # train_text = state_union.raw("TrainPoem.txt")

    # assign actual voice_text to variable
    # voice_text = state_union.raw("output.txt")


    voice_text = "I am Happy"
    # Lower case the text
    lowercase_voice_text = voice_text.lower()
    # print(lowercase_voice_text)

    # Tokenize the text as sentence
    # custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    custom_sent_tokenizer = PunktSentenceTokenizer(lowercase_voice_text)
    # Tokenize the sentence into words
    tokenized = custom_sent_tokenizer.tokenize(lowercase_voice_text)

    def get_uncertain_terms():
        global getHappyExpression, getSadExpression, getDistinguishExpression, getSurpriseExpression, getAngerExpression
        try:
            Final_output = []

            for i in tokenized:
                # word tokenization
                words = nltk.word_tokenize(i)
                # POS tagging
                tagged = nltk.pos_tag(words)
                # Definie a grammer using regex
                chunkGram = r"""Chunk: {<JJ.?>*<RB.?>*}"""
                chunkParser = nltk.RegexpParser(chunkGram)
                chunked = chunkParser.parse(tagged)
                # display chunked uncertain terms as a tree structure
                # chunked.draw()
                # print(chunked)

                ##Filter chenked with label chunk, term, POS tag using label 'Chunk'
                for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                    chunked_words = ""
                    ##Getting only the chunked term
                    for y in subtree:
                        chunked_words = y[0]
                        # print(chunked_words)

                        ##Check Happy term
                        def getHappyExpression():
                            try:
                                from firebase import firebase
                                firebase = firebase.FirebaseApplication(
                                    'https://cdapresearchtest-9bd7c.firebaseio.com/', None)
                                # result = firebase.get('/cdapresearchtest-9bd7c/Expressionterm/', '')
                                result = firebase.get('/cdapresearchtest-9bd7c/Expressionterm/-MHWhGZFhVR8FSvkdhpT',
                                                      'Happy')
                                # print(result)
                                for x in range(len(result)):
                                    exp_term = result[x]
                                    # print(exp_term)
                                    ###Check chunked expression term exist in database
                                    if exp_term.count(chunked_words) > 0:
                                        ###Getting condition satisfying exp term into one array
                                        exist_chunked_terms1 = "Happy"
                                        # print(exist_chunked_terms1)
                                        return exist_chunked_terms1
                                    else:
                                        return ""
                            except Exception as e:
                                print(str(e))

                        getHappyExpression()

                        ##Check Sad term
                        def getSadExpression():
                            try:
                                from firebase import firebase
                                firebase = firebase.FirebaseApplication(
                                    'https://cdapresearchtest-9bd7c.firebaseio.com/', None)
                                # result = firebase.get('/cdapresearchtest-9bd7c/Expressionterm/', '')
                                result = firebase.get('/cdapresearchtest-9bd7c/Expressionterm/-MHWpOyENoIVsPzqF101',
                                                      'Sad')
                                # print(result)
                                for x in range(len(result)):
                                    exp_term = result[x]
                                    # print(exp_term)
                                    ###Check chunked expression term exist in database
                                    if exp_term.count(chunked_words) > 0:
                                        ###Getting condition satisfying exp term into one array
                                        exist_chunked_terms2 = "Sad"
                                        # print(exist_chunked_terms2)
                                        return exist_chunked_terms2
                                    else:
                                        return ""
                            except Exception as e:
                                print(str(e))

                        getSadExpression()

                        ##Check Fear term
                        def getFearExpression():
                            try:
                                from firebase import firebase
                                firebase = firebase.FirebaseApplication(
                                    'https://cdapresearchtest-9bd7c.firebaseio.com/', None)
                                # result = firebase.get('/cdapresearchtest-9bd7c/Expressionterm/', '')
                                result = firebase.get('/cdapresearchtest-9bd7c/Expressionterm/-MHWzudPEKKpataiNE0r',
                                                      'Fear')
                                # print(result)
                                for x in range(len(result)):
                                    exp_term = result[x]
                                    # print(exp_term)
                                    ###Check chunked expression term exist in database
                                    if exp_term.count(chunked_words) > 0:
                                        ###Getting condition satisfying exp term into one array
                                        exist_chunked_terms3 = "Fear"
                                        # print(exist_chunked_terms3)
                                        return exist_chunked_terms3
                                    else:
                                        return ""
                            except Exception as e:
                                print(str(e))

                        getFearExpression()

                        ##Check Anger term
                        def getAngerExpression():
                            try:
                                from firebase import firebase
                                firebase = firebase.FirebaseApplication(
                                    'https://cdapresearchtest-9bd7c.firebaseio.com/', None)
                                # result = firebase.get('/cdapresearchtest-9bd7c/Expressionterm/', '')
                                result = firebase.get('/cdapresearchtest-9bd7c/Expressionterm/-MHWu07AHlB0dAHsVrKQ',
                                                      'Anger')
                                # print(result)
                                for x in range(len(result)):
                                    exp_term = result[x]
                                    # print(exp_term)
                                    ###Check chunked expression term exist in database
                                    if exp_term.count(chunked_words) > 0:
                                        ###Getting condition satisfying exp term into one array
                                        exist_chunked_terms4 = "Anger"
                                        # print(exist_chunked_terms4)
                                        return exist_chunked_terms4
                                    else:
                                        return ""

                            except Exception as e:
                                print(str(e))

                        getAngerExpression()

                        ##Check Surprise term
                        def getSurpriseExpression():
                            try:
                                from firebase import firebase
                                firebase = firebase.FirebaseApplication(
                                    'https://cdapresearchtest-9bd7c.firebaseio.com/', None)
                                # result = firebase.get('/cdapresearchtest-9bd7c/Expressionterm/', '')
                                result = firebase.get('/cdapresearchtest-9bd7c/Expressionterm/-MHWwyErQcoy0oXk16r8',
                                                      'Surprise')
                                # print(result)
                                for x in range(len(result)):
                                    exp_term = result[x]
                                    # print(exp_term)
                                    ###Check chunked expression term exist in database
                                    if exp_term.count(chunked_words) > 0:
                                        ###Getting condition satisfying exp term into one array
                                        exist_chunked_terms5 = "Surprise"
                                        # print(exist_chunked_terms5)
                                        return exist_chunked_terms5
                                    else:
                                        return ""
                            except Exception as e:
                                print(str(e))

                        getSurpriseExpression()

                        ##Check Distinguish term
                        def getDistinguishExpression():
                            try:
                                from firebase import firebase
                                firebase = firebase.FirebaseApplication(
                                    'https://cdapresearchtest-9bd7c.firebaseio.com/', None)
                                # result = firebase.get('/cdapresearchtest-9bd7c/Expressionterm/', '')
                                result = firebase.get('/cdapresearchtest-9bd7c/Expressionterm/-MHX0XJQ04jUMt_KXrKR',
                                                      'Distinguish')
                                # print(result)
                                for x in range(len(result)):
                                    exp_term = result[x]
                                    # print(exp_term)
                                    ###Check chunked expression term exist in database
                                    if exp_term.count(chunked_words) > 0:
                                        ###Getting condition satisfying exp term into one array
                                        exist_chunked_terms6 = "Distinguish"
                                        # print(exist_chunked_terms6)
                                        return exist_chunked_terms6
                                    else:
                                        return ""
                            except Exception as e:
                                print(str(e))

                        getDistinguishExpression()

            Final_output = [str(getHappyExpression()) + str(getSadExpression()) + str(getDistinguishExpression()) + str(getDistinguishExpression()) + str(getSurpriseExpression()) + str(getAngerExpression())]
            print(Final_output)

            from firebase import firebase

            firebase = firebase.FirebaseApplication('https://cdapresearchtest-9bd7c.firebaseio.com/', None)
            data = {'emotionTerm': Final_output}

            result = firebase.patch('/cdapresearchtest-9bd7c/Uncertain/emotion/', data)
            print(result)

        except Exception as e:
            print(str(e))

    get_uncertain_terms()

# runUncertain()
