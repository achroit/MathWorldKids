from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


# Declare both screens
class MenuScreen(Screen):
    pass


class StartScreen(Screen):
    pass


class AddChooseDifficulty(Screen):
    category1 = "Up to 5"
    category2 = "Up to 10"
    category3 = "Up to 15"
    category4 = "Up to 20"
    category5 = "Up to 25"
    category6 = "Up to 35"
    category7 = "Up to 50"
    category8 = "Up to 65"
    category9 = "Up to 75"
    category10 = "Up to 100"


class SubChooseDifficulty(Screen):
    category1 = "Up to 5"
    category2 = "Up to 10"
    category3 = "Up to 15"
    category4 = "Up to 20"
    category5 = "Up to 25"
    category6 = "Up to 35"
    category7 = "Up to 50"
    category8 = "Up to 65"
    category9 = "Up to 75"
    category10 = "Up to 100"


class MultiChooseDifficulty(Screen):
    category1 = "Times of 2"
    category2 = "Times of 3"
    category3 = "Times of 4"
    category4 = "Times of 5"
    category5 = "Times of 6"
    category6 = "Times of 7"
    category7 = "Times of 8"
    category8 = "Times of 9"
    category9 = "Times of 10"
    category10 = "Times of 11 and 12"


class DivChooseDifficulty(Screen):
    category1 = "Times of 2"
    category2 = "Times of 3"
    category3 = "Times of 4"
    category4 = "Times of 5"
    category5 = "Times of 6"
    category6 = "Times of 7"
    category7 = "Times of 8"
    category8 = "Times of 9"
    category9 = "Times of 10"
    category10 = "Times of 11 and 12"


class GreaterSmallerChooseDifficulty(Screen):
    category1 = "Up to 10"
    category2 = "25"
    category3 = "50"
    category4 = "100"
    category5 = "Adding values"
    category6 = "Subtracting values"
    category7 = "Multiplication"
    category8 = "Division"
    category9 = "Mixing 1"
    category10 = "Mixing 2"


class ChallengeChooseDifficulty(Screen):
    category1 = "Adding + Subtracting"
    category2 = "Adding + Subtracting 2"
    category3 = "Multiplication and Division"
    category4 = "Negative Numbers"
    category5 = "A little bit of everything 1"
    category6 = "Longer tasks 1"
    category7 = "Longer tasks 2"
    category8 = "Longer tasks 3"
    category9 = "A little bit of everything 2"
    category10 = "Grande Finale"


class ProgressScreen(Screen):
    pass


class GameActionScreen(Screen):
    #TODO set properties like the type of game played, number of errors
    #TODO implement function that sets the text of the labels and the buttons

    errors_made = 0
    round_number = 1

    current_category = ""
    current_mode = ""

    def thing(self):
        self.ids.task.text = "Rechne 4 + 0 * 1"
        self.ids.button_1.text = "4"
        self.ids.button_2.text = "4"
        self.ids.button_3.text = "4"
        self.ids.button_4.text = "4"

        self.ids.label_1.text = "Errors: " + str(self.errors_made)
        self.ids.label_2.text = str(self.current_mode)
        self.ids.label_3.text = str(self.round_number)


    def lol(self):
        print("lols")


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

    def about_text(self):
        return "Made by: Jonas\n" \
               "Open source and free of charge \n" \
               "\n" \
               "This app has been written to help everyone to be better\n" \
               " at mental arithmetic.\n" \
               "\n" \
               "Features:\n" \
               "  - simple\n" \
               "  - rewarding\n" \
               "  - perfect for kids in elementary school\n" \
               "  - or adults who want to train their brain ;)\n" \
               "  - No ads, they only distract\n" \
               "  - never gets old, new content is generated procedurally\n" \
               "  - written in Python with the help of Kivy"


class MathApp(App):

    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(ProgressScreen(name='progress'))
        sm.add_widget(HelpScreen(name='help'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(AddChooseDifficulty(name='addChooser'))
        sm.add_widget(SubChooseDifficulty(name='subChooser'))
        sm.add_widget(MultiChooseDifficulty(name='multiChooser'))
        sm.add_widget(DivChooseDifficulty(name='divChooser'))
        sm.add_widget(GreaterSmallerChooseDifficulty(name='greaterSmallerChooser'))
        sm.add_widget(ChallengeChooseDifficulty(name='challengeChooser'))
        sm.add_widget(GameActionScreen(name='game'))
        return sm

if __name__ == '__main__':
    MathApp().run()