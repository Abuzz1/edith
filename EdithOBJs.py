#TTS LIRBRAIES
from gtts import gTTS
import os

#TTS
class tts:
    def run(outBeta):
        vOut = gTTS(text = outBeta, lang = "en", slow = False)
        vOut.save(".voice.mp3")
        os.system("afplay " + ".voice.mp3")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# GOOGLE SEARCH LIRBRAIES
import requests
from bs4 import BeautifulSoup
#GTTS
class ggs():
    def answer_search():
        result = ''
        user_query = input('Enter your query: ')

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        ni = True

        if ni == True: # Answer 1
            try:
                result = soup.find(class_='Z0LcW').get_text()
                ni = False
            except:
                pass

        if ni == True: # Answer 2
            try:
                result = soup.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
                ni = False
            except:
                pass

        if result == '':
            print("Restate the question")
            tts.run("Restate the question")
        else:
            print(result)
            tts.run(result)

    def disc_search():
        result = ''
        user_query = input('Enter your query: ')

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        ni = True
        if ni == True:  # Description 1
            try:
                result = soup.find(class_='kno-rdesc').get_text()
                ni = False
            except:
                pass
        if ni == True:  # Description 2
            try:
                result = soup.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
                ni = False
            except:
                pass

        if ni == True:  # Description 3
            try:
                result = soup.find(class_='LGOjhe').get_text()
                ni = False
            except:
                pass
        if result == '':
            print("Restate the question")
            tts.run("Restate the question")
        else:
            print(result)
            tts.run(result)
    def answer_searchSTT(user_query):
        result = ''

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        ni = True

        if ni == True: # Answer 1
            try:
                result = soup.find(class_='Z0LcW').get_text()
                ni = False
            except:
                pass

        if ni == True: # Answer 2
            try:
                result = soup.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
                ni = False
            except:
                pass

        if result == '':
            print("Restate the question")
            tts.run("Restate the question")
        else:
            print(result)
            tts.run(result)

    def disc_searchSTT(user_query):
        result = ''

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        ni = True
        if ni == True:  # Description 1
            try:
                result = soup.find(class_='kno-rdesc').get_text()
                ni = False
            except:
                pass
        if ni == True:  # Description 2
            try:
                result = soup.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
                ni = False
            except:
                pass

        if ni == True:  # Description 3
            try:
                result = soup.find(class_='LGOjhe').get_text()
                ni = False
            except:
                pass
        if result == '':
            print("Restate the question")
            tts.run("Restate the question")
        else:
            print(result)
            tts.run(result)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# GOOGLE SEARCH LIRBRAIES
import requests
from bs4 import BeautifulSoup
#GTTS
class ggsGUI():
    def answer_search(user_query):
        result = ''

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        ni = True

        if ni == True: # Answer 1
            try:
                result = soup.find(class_='Z0LcW').get_text()
                ni = False
            except:
                pass

        if ni == True: # Answer 2
            try:
                result = soup.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
                ni = False
            except:
                pass

        if result == '':
            return "Restate the question!"
        else:
            return result

    def disc_search(user_query):
        result = ''


        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        ni = True
        if ni == True:  # Description 1
            try:
                result = soup.find(class_='kno-rdesc').get_text()
                ni = False
            except:
                pass
        if ni == True:  # Description 2
            try:
                result = soup.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
                ni = False
            except:
                pass

        if ni == True:  # Description 3
            try:
                result = soup.find(class_='LGOjhe').get_text()
                ni = False
            except:
                pass
        if result == '':
            return "Restate the question"

        else:
            return result

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


#WOLFRAMAI LIRBRAIES
import wolframalpha as wl
# wolframalpha api key
client = wl.Client("G8X7XT-LH93TX486J")

#WOLFRAMAI
class wolframAi():
    def run():
        while True:
            print("EDITH - wolframalpha")
            z = input("Query: ")
            if z == "exit" or z == "ex":
                break
            else:
                try:
                    wolfram_res = next(client.query(z).results).text
                    print("Wolfram Result:")
                    print()
                    print(wolfram_res)
                    tts.run(wolfram_res)
                except:
                    print("Wolfram can't find anything for this... try again or try the Wiki")
                    print()
                    break


#WOLFRAMAI version for speech to text
class wolframAiSTT():
    def run(z):
        print("EDITH - wolframalpha")
        try:
            wolfram_res = next(client.query(z).results).text
            print("Wolfram Result:")
            print()
            print(wolfram_res)
            tts.run(wolfram_res)
        except:
            print("Wolfram can't find anything for this... try again or try the Wiki")
            print()


# gui
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

# GUI INTERFACE
class WrappedLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))

class edithGUI(App):
    txtBox = TextInput(multiline = True, padding_y = (20, 20), size_hint = (1, 0.5))
    out = WrappedLabel(text = "Output: ", font_size="15dp", color="#00FFCE", halign = "center")

    def build(self):
        # LAYOUTS
        mainLayout = BoxLayout(orientation="vertical")
        hboxLayout = BoxLayout(orientation="horizontal")

        img = Image(source="image-resources/edith-abuzz.png")

        ans = Button(text="Answer", background_color="#6FB1FC")
        ed = Button(text="edith.ai", background_color="#6FB1FC")
        desc = Button(text="description", background_color="#6FB1FC")
        wol = Button(text="wolframAi", background_color="6FB1FC")
        mainLayout.add_widget(img)

        ans.bind(on_press=self.answer)
        hboxLayout.add_widget(ans)

        ed.bind(on_press=self.edi)
        hboxLayout.add_widget(ed)

        desc.bind(on_press=self.description)
        hboxLayout.add_widget(desc)

        wol.bind(on_press=self.wolf)
        hboxLayout.add_widget(wol)


        vboxLayout = BoxLayout(orientation="vertical")

        vboxLayout.add_widget(self.txtBox)
        vboxLayout.add_widget(self.out)

        mainLayout.add_widget(hboxLayout)
        mainLayout.add_widget(vboxLayout)
        return mainLayout

    def answer(self, instance):
        # self.out.text = ""
        try:
            self.out.text = ggsGUI.answer_search(self.txtBox.text)
            tts.run(self.out.text)
        except:
            self.out.text = ("The answer searching can't find anything for this... try again or try Wolfram or a description search")

    def edi(self, instance):
        self.out.text = "Edith AI coming soon.."

    def wolf(self, instance):
        try:
            wolfram_res = next(client.query(self.txtBox.text).results).text
            self.out.text = wolfram_res
            tts.run(wolfram_res)
        except:
            self.out.text = ("Wolfram can't find anything for this... try again or try the Wiki")
    def description(self, instance):
        try:
            self.out.text = ggsGUI.disc_search(self.txtBox.text)
            tts.run(self.out.text)
        except:
            self.out.text = ("The description search can't find anything for this... try again or try Wolfram answer search")







# !!!!!!~


# for the colors in printing
class color:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    NORM = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"





#stt


import speech_recognition as sr
import re

class stt():
    def micro():
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        # check that recognizer and microphone arguments are appropriate type
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")
        try:
            # listen and assign
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            # return output
            return recognizer.recognize_google(audio)
        except:
            print("speak up!")

    def a(q):
        ggs.answer_searchSTT(q)
    def d(q):
        ggs.disc_searchSTT(q)
    def wolf(q):
        wolframAiSTT.run(q)

    def run():
        def wakeUp():
            alpha = stt.micro()
            # alpha = input()
            print(alpha)
            try:
                #answer
                if re.search('.+answer', str(alpha)):
                    alpha.split(' ', 1)
                    query = alpha.split(' ' , 1)[1]
                    a(query)
                elif re.search('answer', str(alpha)):
                    alpha.split(' ', 1)
                    query = alpha.split(' ' , 1)[1]
                    a(query)
                #description
                elif re.search('.+description', str(alpha)):
                    alpha.split(' ', 1)
                    query = alpha.split(' ' , 1)[1]
                    d(query)
                elif re.search('description', str(alpha)):
                    alpha.split(' ', 1)
                    query = alpha.split(' ' , 1)[1]
                    d(query)
                #wolf
                elif re.search('.+wolf', str(alpha)):
                    alpha.split(' ', 1)
                    query = alpha.split(' ' , 1)[1]
                    wolf(query)
                elif re.search('wolf', str(alpha)):
                    alpha.split(' ', 1)
                    query = alpha.split(' ' , 1)[1]
                    wolf(query)
                #ERRORS
                else:
                    print("Say it again!")

            except:
                print("Say it again!")


        wakeUp()