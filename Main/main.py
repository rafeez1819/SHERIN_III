from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

# Splash Screen that plays Sherin's Logo
class SplashScreen(Screen):
    def on_enter(self):
        layout = BoxLayout()
        self.video = Video(source='Logo_Final.mp4', state='play', options={'eos': 'stop'})
        self.video.bind(on_eos=self.switch_to_main)
        layout.add_widget(self.video)
        self.add_widget(layout)

    def switch_to_main(self, *args):
        self.manager.current = 'main'

# Main App Screen after splash
class MainScreen(Screen):
    def on_enter(self):
        self.clear_widgets()
        layout = BoxLayout()
        label = Label(text='🖤 Hi Captain, Sherin is ready!', font_size='24sp')
        layout.add_widget(label)
        self.add_widget(layout)

        # Optional: enable voice welcome
        # self.say_welcome()

    # Optional: Text-to-Speech greeting (requires pyttsx3)
    # def say_welcome(self):
    #     import pyttsx3
    #     engine = pyttsx3.init()
    #     engine.say("Hi Captain, I'm ready.")
    #     engine.runAndWait()

# Main App controller
class SherinApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    SherinApp().run()
