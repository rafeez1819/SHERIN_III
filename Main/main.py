from kivy.core.audio import SoundLoader
from kivy.uix.video import Video

# sound
s = SoundLoader.load('Assets/notification.mp4')
if s: s.play()

# video widget somewhere in your layout
v = Video(source='Assets/Logo_inm.mp4', state='play')
