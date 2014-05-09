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

    def help_text(self):
        return "Here i will provide simple tricks to become faster when\n" \
               "doing mental calculations.\n" \
               "Example: Instead of adding 5 to a digit greater than 5,\n" \
               "its often more simple to subtract 5 and then add 10.\n" \
               " 8 + 5 = ?\n" \
               " 8 - 5 = 3; 3 + 10 = 13\n" \
               "\n"\
               "Or add in two steps, first to get to an more easy number, \n" \
               "then whatever remains.\n" \
               "\n"\
               "587 + 33 = ?\n" \
               "33 = 20 + 13\n" \
               "587 + 13 = 600; 600 + 20 = 620\n" \
               "Therefore 587 + 33 is 620\n" \
               "\n"\
               "More will follow soon!\n"


class AboutScreen(Screen):
    pass


class MathApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(ProgressScreen(name='progress'))
        sm.add_widget(HelpScreen(name='help'))
        sm.add_widget(AboutScreen(name='about'))
        return sm

if __name__ == '__main__':
    MathApp().run()