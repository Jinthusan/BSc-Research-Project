import self
import speech_recognition as sr
import wave
import struct
import numpy as np



def runMain():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")

        audio = r.listen(source)
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
        try:
            text = r.recognize_google(audio)
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
        global voiceoutput
        voiceoutput = freq_in_hertz = abs(freq * frate)

    print("You said : {}".format(voiceoutput))

    self.txt2.text = format(voiceoutput)
    self.txt3.text = format(frequency)
    self.txt4.text = "processed"

    from firebase import firebase

    firebase = firebase.FirebaseApplication('https://cdapresearchtest-9bd7c.firebaseio.com/', None)
    data = {'Pitch': freq_in_hertz}

    result = firebase.patch('/cdapresearchtest-9bd7c/Pitch/name/', data)
    print(result)
 # runMain()