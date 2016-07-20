from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.factory import Factory
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
import configparser
import sys



#read configurations
config = configparser.RawConfigParser()
config.read('config.ini')

#read config values
width = config.getint('Default', 'MAX_WINDOW_WIDTH')
height = config.getint('Default', 'MAX_WINDOW_HEIGHT')
border = config.getint('Default', 'BORDERLESS')

#apply config values
Config.set('graphics','width', width)
Config.set('graphics', 'height', height)
Config.set('graphics', 'borderless', border)
Config.set('input', 'mouse', 'mouse, multitouch_on_demand')


#create main screen:
class MainScreen(Screen):
    def callback_quit(self):
        sys.exit()



class ReadScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file('MainMain.kv')


class MainMainApp(App):
    def build(self):
        return presentation


if __name__ == '__main__':
    MainMainApp().run()