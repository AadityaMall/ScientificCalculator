#IMPORTING MODULES
import pyttsx3

#CREATING A CLASS WITH FUNCTIONS
class PlayAudio():
    def __init__(self, voice='male',speakstatus = True):
        self.voice = 'male'
        self.speakstatus = speakstatus
        self.speakWords = {
            '1':'one',
            '2':'two',
            '3':'three',
            '4':'four',
            '5':'five',
            '6':'six',
            '7':'seven',
            '8':'eight',
            '9':'nine',
            '+':'plus',
            '-':'minus',
            'x':'multiplied by',
            '÷':'divided by',
            '%':'percentage',
            'DEL':'delete',
            'C':'clear',
            '0':'zero',
            '.':'dot',
            ',':'comma',
            '=':'equals',
        }
        self.engine = pyttsx3.init()
        v=self.engine.getProperty('voices')
       #SETTING THE VOICE TO MALE
        self.engine.setProperty('voices', v[0].id)
       
    
    def speak(self, content):
        if self.speakstatus == True:
            self.engine.say(self.speakWords[content])
            self.engine.runAndWait()



 



