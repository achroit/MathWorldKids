from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


# Declare both screens
class MenuScreen(Screen):
    pass


class StartScreen(Screen):
    pass


class ProgressScreen(Screen):
    pass


class HelpScreen(Screen):
    pass


class AboutScreen(Screen):
    pass


class MathApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(ProgressScreen(name='progress'))
        sm.add_widget(HelpScreen(name='help'))
        sm.add_widget(AboutScreen(name='help'))
        return sm

if __name__ == '__main__':
    MathApp().run()