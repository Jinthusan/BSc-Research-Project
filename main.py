import sys

import nltk

sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from specialbuttons import ImageButton, LabelButton, ImageButtonSelectable
from kivy.properties import DictProperty
from functools import partial
from os import walk
from datetime import datetime

import Uncommon
import kivy.utils
from kivy.utils import platform
import requests
import json
import traceback
from kivy.graphics import Color, RoundedRectangle
import helperfunctions
import kivy.uix.button as Button
import speech_recognition as sr
import wave
import struct
import numpy as np
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (300, 500)


class HomeScreen(Screen):
    pass


class AddWorkoutScreen(Screen):
    def btn(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak Anything :")

            audio = r.listen(source)
            with open("recorded.wav", "wb") as f:
                f.write(audio.get_wav_data())
            try:
                global text
                text = r.recognize_google(audio)
                print(text)
                print("You said : {}".format(text))
                self.txt1.text = format(text)


            except:
                print("Sorry could not recognize what you said")

        if __name__ == '__main__':
            data_size = 40000
            fname = "recorded.wav"
            frate = 11025.0
            wav_file = wave.open(fname, 'r')  # opening our recorded file
            data = wav_file.readframes(data_size)  # find Frams of our audio
            wav_file.close()
            data = struct.unpack('{n}h'.format(n=data_size), data)  # find time rang and other basic info of audio
            data = np.array(data)

            wavelength = w = np.fft.fft(data)
            freqs = np.fft.fftfreq(len(w))  # lfunth

            # Find the peak in the coefficients
            idx = np.argmax(np.abs(w))  # peack value
            frequency = freq = freqs[idx]

            voiceoutput = freq_in_hertz = abs(freq * frate)
        print("You said : {}".format(voiceoutput))
        self.txt2.text = format(voiceoutput)
        self.txt3.text = format(frequency)
        #self.txt4.text = "processed"


        from firebase import firebase

        firebase = firebase.FirebaseApplication('https://cdapresearchtest-9bd7c.firebaseio.com/', None)
        data = {'Pitch': freq_in_hertz}

        result = firebase.patch('/cdapresearchtest-9bd7c/Pitch/name/', data)

        ################Uncertain_terms.py
        import nltk
        from nltk.corpus import state_union
        from nltk.tokenize import PunktSentenceTokenizer

        voice_text = text
        # Lower case the text
        lowercase_voice_text = voice_text.lower()
        # print(lowercase_voice_text)

        # Tokenize the text as sentence
        # custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
        custom_sent_tokenizer = PunktSentenceTokenizer(lowercase_voice_text)
        # Tokenize the sentence into words
        tokenized = custom_sent_tokenizer.tokenize(lowercase_voice_text)
        print(voice_text)

        def get_uncertain_terms():
            # global getHappyExpression, getSadExpression, getDistinguishExpression, getSurpriseExpression, getAngerExpression
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
                            print(chunked_words)

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

                        Final_output = [
                            str(getHappyExpression()) + str(getSadExpression()) + str(getDistinguishExpression()) + str(
                                getDistinguishExpression()) + str(getSurpriseExpression()) + str(getAngerExpression())]
                        print(Final_output)

                        from firebase import firebase

                        firebase = firebase.FirebaseApplication('https://cdapresearchtest-9bd7c.firebaseio.com/', None)
                        data = {'emotionTerm': Final_output}

                        result = firebase.patch('/cdapresearchtest-9bd7c/Uncertain/emotion/', data)
                        print(result)

            except Exception as e:
                print(str(e))

        get_uncertain_terms()
        ################Uncertain_terms.py

        # ################Uncommon.py
        import nltk
        from nltk.tokenize import word_tokenize
        import string

        s = open(gotpath)
        #print(gotpath)
        a = []
        for word in word_tokenize(s.read()):
            # print(word)
            a.append(word)
            a = [word for word in a if word.isalpha()]
            totalwordcount = len(a)
        print(a)
        print(totalwordcount)

        from firebase import firebase
        firebase = firebase.FirebaseApplication('https://cdapresearchtest-9bd7c.firebaseio.com/', None)
        data = {'TotalWordCount': totalwordcount}

        result = firebase.patch('/cdapresearchtest-9bd7c/WordCount/TotCount', data)

        # In[52]:

        # d = open(r"C:\Users\JINTHUSAN\AppData\Roaming\nltk_data\corpora\state_union\output.txt")
        d = text
        b = []
        for word in word_tokenize(d):
            # print(word)
            b.append(word)
        print(b)

        # In[53]:

        def uncommon(s, d):

            uc = ''
            for i in s:
                if i not in d:
                    uc = uc + " " + i
            for j in d:
                if j not in s:
                    uc = uc + " " + j

            return uc

        print("Uncommon words are :", uncommon(a, b))

        # In[54]:

        num = uncommon(a, b).count(" ")
        print('Number of missing words :', num)

        from firebase import firebase
        firebase = firebase.FirebaseApplication('https://cdapresearchtest-9bd7c.firebaseio.com/', None)
        data = {'MissingCount': num}

        result = firebase.patch('/cdapresearchtest-9bd7c/Missing/count', data)

        # In[ ]:
        # ################Uncommon.py

        ####Get Pitch
        from firebase import firebase
        firebase = firebase.FirebaseApplication('https://cdapresearchtest-9bd7c.firebaseio.com/', None)
        result = firebase.get('/cdapresearchtest-9bd7c/Pitch/name', "")
        print(result)
        for x in result:
            pitch = result[x]
            print(pitch)

        ###Get Total word count
        from firebase import firebase
        firebase = firebase.FirebaseApplication('https://cdapresearchtest-9bd7c.firebaseio.com/', None)
        result = firebase.get('/cdapresearchtest-9bd7c/WordCount/TotCount', "")
        print(result)
        for x in result:
            TotWordCount = result[x]
            print(TotWordCount)

        ###Get Missing count
        from firebase import firebase
        firebase = firebase.FirebaseApplication('https://cdapresearchtest-9bd7c.firebaseio.com/', None)
        result = firebase.get('/cdapresearchtest-9bd7c/Missing/count', "")
        print(result)
        for x in result:
            missCount = result[x]
            print(missCount)

        ####Get Facial Out put Thesi
        from firebase import firebase
        firebase = firebase.FirebaseApplication('https://cdapresearchtest-9bd7c.firebaseio.com/', None)
        result = firebase.get('/cdapresearchtest-9bd7c/Facial/expressions', "")
        print(result)
        faceOut = []
        for x in result:
            faceOut = result[x]
            print(faceOut)

        ####Get Emotion term
        from firebase import firebase

        firebase = firebase.FirebaseApplication('https://cdapresearchtest-9bd7c.firebaseio.com/', None)
        result = firebase.get('/cdapresearchtest-9bd7c/Uncertain/emotion', "")
        print(result)
        emotionTerm = []
        for x in result:
            emotionTerm = result[x]
            print(emotionTerm)

        ####Score Part

        ####Word Count Score

        MissCountScore = (missCount / TotWordCount) * 100
        print(MissCountScore)

        ###Pitch score
        if 60 <= pitch:
            pitchScore = 80
            print(pitchScore)
        elif 30 <= pitch <= 59:
            pitchScore = 55
            print(pitchScore)
        else:
            pitchScore = 20
            print(pitchScore)

        ####Emotional Term score
        for x in range(len(emotionTerm)):
            emo_term = emotionTerm[x]
            # print(emo_term)

        scoreCount = 0
        for x in range(len(faceOut)):
            face_term = faceOut[x]
            # print(face_term)
            if face_term.count(emo_term) > 0:
                scoreCount = scoreCount + 16.6
        print(scoreCount)
        global TotalScore
        TotalScore = (pitchScore + scoreCount) - missCount
        #tscore = print("TotalScore:" + str(TotalScore))
        self.txt4.text = format(TotalScore)
    pass


class FriendWorkoutScreen(Screen):
    pass


class FileChoosePopup(Popup):
    load = ObjectProperty()


class fileupload(Screen):
    def one(self):
        file_path = StringProperty("No file chosen")

    the_popup = ObjectProperty(None)

    def open_popup(self):
        self.the_popup = FileChoosePopup(load=self.load)
        self.the_popup.open()

    def load(self, selection):
        self.file_path = str(selection[0])

        # sending selected path to second screen
        send = str(selection[0])
        s = LoginScreen()
        s.two(send)
        # check for non-empty list i.e. file selected
        if self.file_path:
            self.ids.get_file.text = self.file_path

    pass


class LoginScreen(Screen):

    def two(self, receive):
        # print(receive)

        if __name__ == '__main__':
            data_size = 40000
            global gotpath
            gotpath = receive
        # print(fname)


    def btn(self):
        self.login_email.text = "Enter your email"


pass


class rule(Screen):

    def btn(self):
        # # Web Scraping - Competition Details

        # %matplotlib inline
        from urllib.request import urlopen

        # In[498]:
        import pandas as pd
        from bs4 import BeautifulSoup


        url = "file:///" + gotpath
        html = urlopen(url)

        # In[500]:

        soup = BeautifulSoup(html, 'lxml')
        type(soup)

        # In[501]:

        # Get the title
        title1 = soup.title
        # print("Tite of the page :", title1.text)

        # In[502]:

        # Print out the text
        text = soup.get_text()
        # print(text)

        # In[503]:

        rows = soup.find_all('tr')
        print(rows[:50])

        # In[504]:

        import re

        list_rows = []
        for row in rows:
            cells = row.find_all('td')
            str_cells = str(cells)
            clean = re.compile('<.*?>')
            clean2 = (re.sub(clean, '', str_cells))
            list_rows.append(clean2)
        # print(list_rows)
        type(clean2)

        # In[505]:

        df = pd.DataFrame(list_rows)
        df.head(10)

        # In[506]:

        df1 = df[0].str.split(',', expand=True)
        df1.head(10)

        # In[507]:

        df1[0] = df1[0].str.strip('[')
        df1.head(10)

        # In[508]:

        col_labels = soup.find_all('th')

        # In[509]:

        all_header = []
        col_str = str(col_labels)
        cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
        all_header.append(cleantext2)
        # print(all_header)

        # In[510]:

        df2 = pd.DataFrame(all_header)
        df2.head()

        # In[511]:

        df3 = df2[0].str.split(',', expand=True)
        df3.head()

        # In[512]:

        frames = [df3, df1]

        df4 = pd.concat(frames)
        df4.head(10)

        # In[513]:

        df5 = df4.rename(columns=df4.iloc[0])
        df5.head()

        # In[514]:

        df5.info()
        df5.shape

        # In[515]:

        df6 = df5.dropna(axis=0, how='any')

        # In[516]:

        df7 = df6.drop(df6.index[0])
        df7.head()

        # In[517]:

        df7.rename(columns={'[Competitions': 'Competitions'}, inplace=True)
        df7.rename(columns={' Details]': 'Details'}, inplace=True)
        df7.head()

        # In[518]:

        df7['Details'] = df7['Details'].str.strip(']')
        df7.head()

        # In[519]:

        # In[520]:

        df7.to_csv('compe.csv')

        # In[ ]:

        # # Web Scraping - Marking Criteria

        # In[521]:

        self.txt1.text = format(rows[:50])

    pass

class Reachus(Screen):

    def btn(self):
        self.txt1.text = format(TotalScore)

    pass


class about(Screen):

    def btn(self):

        # # Web Scraping - Marking criteria

        # %matplotlib inline
        from urllib.request import urlopen

        # In[498]:
        import pandas as pd
        from bs4 import BeautifulSoup

        url = "file:///" + gotpath
        html = urlopen(url)

        # In[522]:

        soup = BeautifulSoup(html, 'lxml')
        type(soup)

        # In[542]:

        # Get the title
        heading = soup.title
        # print("Tite of the page is :", heading.text)

        # In[543]:

        lines = soup.find_all('tr')
        print(lines[:50])

        # In[544]:

        import re

        list_lines = []
        for row in lines:
            cells = row.find_all('td')
            str_cells = str(cells)
            clean = re.compile('<.*?>')
            clean2 = (re.sub(clean, '', str_cells))
            list_lines.append(clean2)
        # print(list_lines)
        type(clean2)

        # In[546]:

        df_a = pd.DataFrame(list_lines)
        df_a.head()

        # In[547]:

        df_a = df_a[0].str.split(',', expand=True)
        df_a.head()

        # In[548]:

        df_a[0] = df_a[0].str.strip('[')
        df_a.head()

        # In[529]:

        col_labels = soup.find_all('th')

        # In[549]:

        all_head = []
        col_str = str(col_labels)
        cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
        all_head.append(cleantext2)
        # print(all_head)

        # In[550]:

        df_b = pd.DataFrame(all_head)
        df_b.head()

        # In[552]:

        df_c = df_b[0].str.split(',', expand=True)
        df_c.head()
        # In[553]:

        frames = [df_c, df_a]

        df_d = pd.concat(frames)
        df_d.head(10)

        # In[554]:

        df_e = df_d.rename(columns=df_d.iloc[0])
        df_e.head()

        # In[556]:

        df_e.info()
        df_e.shape

        # In[557]:

        df_f = df_e.dropna(axis=0, how='any')

        # In[558]:

        df_g = df_f.drop(df_f.index[0])
        df_g.head()

        # In[559]:

        df_g.rename(columns={'[Poetry': 'Poetry'}, inplace=True)
        df_g.rename(columns={' Speech]': 'Speech'}, inplace=True)
        df_g.head()

        # In[560]:

        df_g['Speech'] = df_g['Speech'].str.strip(']')
        df_g.head()

        # In[540]:

        # In[541]:

        df_g.to_csv('criteria.csv')

        # In[ ]:

        # In[ ]:


        self.txt1.text = format(lines[:50])

    pass

class confirmation01(Screen):
    pass


class SettingsScreen(Screen):
    pass



# GUI =   # Make sure this is after all class definitions!
class MainApp(App):
    my_friend_id = ""
    workout_image = None
    option_choice = None
    workout_image_widget = ""
    previous_workout_image_widget = None

    refresh_token_file = "refresh_token.txt"


    def build(self):
        print("BEFORE")
        # self.my_firebase = MyFirebase()
        # print(self.my_firebase)
        print("AFTER")
        if platform == 'ios':
            self.refresh_token_file = App.get_running_app().user_data_dir + self.refresh_token_file
        return Builder.load_file("main.kv")  # GUI

    def sign_out_user(self):
        # User wants to log out
        with open(self.refresh_token_file, 'w') as f:
            f.write("")
        self.change_screen("login_screen", direction='down', mode='push')
        # Need to set the avatar to the default image
        avatar_image = self.root.ids['avatar_image']
        avatar_image.source = "icons/avatars/man.png"


        # Clear home screen
        self.root.ids.home_screen.ids.streak_label.text = "0 Day Streak. Go workout!"

        # Clear login screen
        self.root.ids.login_screen.ids.login_email.text = ""
        self.root.ids.login_screen.ids.login_password.text = ""

        # Clear workout screen
        workout_screen = self.root.ids.add_workout_screen
        workout_screen.ids.description_input.text = ""
        workout_screen.ids.units_input.background_color = (1, 1, 1, 1)
        now = datetime.now()

        self.workout_image = None
        self.option_choice = None
        # Clear the indication that the previous image was selected
        if self.workout_image_widget:
            self.workout_image_widget.canvas.before.clear()
        # Make sure the text color of the label above the scrollview is white (incase it was red from them earlier)
        select_workout_image_label = workout_screen.ids.select_workout_image_label
        select_workout_image_label.color = (1, 1, 1, 1)

    def change_screen(self, screen_name, direction='forward', mode=""):
        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        # print(direction, mode)
        # If going backward, change the transition. Else make it the default
        # Forward/backward between pages made more sense to me than left/right
        if direction == 'forward':
            mode = "push"
            direction = 'left'
        elif direction == 'backwards':
            direction = 'right'
            mode = 'pop'
        elif direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)

        screen_manager.current = screen_name



MainApp().run()
