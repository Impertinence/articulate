import gtts

from gtts import gTTS
from pygame import mixer

v = gTTS(text='hello world', lang='en', slow=True)
v.save('name1.mp3')

mixer.init()
mixer.music.load('name1.mp3')
mixer.music.play()
