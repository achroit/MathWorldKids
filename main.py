from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.uix.popup import Popup
import taskCreator
import time

# Declare both screens
class MenuScreen(Screen):
    pass


class StartScreen(Screen):
    pass


class AddChooseDifficulty(Screen):
    title = "Addition - Great fun with the + sign"
    category1 = "Up to 5"
    category2 = "Up to 10"
    category3 = "Up to 15"
    category4 = "Up to 20"
    category5 = "Up to 25"
    category6 = "Up to 50"
    category7 = "Up to 75"
    category8 = "Up to 100"
    category9 = "Up to 500"
    category10 = "Up to 1000"


class SubChooseDifficulty(Screen):
    title = "Subtracting - But not less funny "
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
    title = "Multiplication - Double the fun"
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
    title = "Division - Just a fraction of math"
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
    title = "Who is the greatest?"
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
    title = "Challenge - Are your ready?"
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
    errors_made = 0
    round_number = 1
    max_rounds = 15

    task_values = [0, 0, 0, 0, 0, 0]

    current_category = ""
    current_mode = ""

    def new_game(self):
        self.round_number = 0
        self.set_next_task()

    def set_next_task(self):
        operator = ""
        if self.current_mode == "addChooser":
            self.task_values = taskCreator.add_task(int(self.current_category))
            operator = "+"
        elif self.current_mode == "subChooser":
            self.task_values = taskCreator.sub_task(int(self.current_category))
            operator = "-"
        elif self.current_mode == "multiChooser":
            self.task_values = taskCreator.multi_task(int(self.current_category))
            operator = "*"
        elif self.current_mode == "divChooser":
            self.task_values = taskCreator.div_task(int(self.current_category))
            operator = "/"
        elif self.current_mode == "greaterSmallerChooser":
            pass
        elif self.current_mode == "challengeChooser":
            pass

        self.ids.task.text = str(self.task_values[0]) + " " + operator + " " + str(self.task_values[1])
        self.ids.button_1.text = str(self.task_values[2])
        self.ids.button_2.text = str(self.task_values[3])
        self.ids.button_3.text = str(self.task_values[4])
        self.ids.button_4.text = str(self.task_values[5])

        self.ids.label_1.text = "Errors: " + str(self.errors_made)
        self.ids.label_2.text = str(self.current_mode) + str(self.current_category)
        self.ids.label_3.text = str(self.round_number) + " / " + str(self.max_rounds)

        #set all the button backgrounds back to normal
        self.ids.button_1.background_normal = "./data/normal.png"
        self.ids.button_2.background_normal = "./data/normal.png"
        self.ids.button_3.background_normal = "./data/normal.png"
        self.ids.button_4.background_normal = "./data/normal.png"

    def check_answer(self, button_pressed):
        if self.current_mode == "addChooser":
            if self.round_number == self.max_rounds:
                self.manager.current = 'result'
            elif int(button_pressed.text) == self.task_values[0] + self.task_values[1]:
                self.round_number += 1
                self.ids.label_3.text = str(self.round_number) + " / " + str(self.max_rounds)
                self.set_next_task()
            else:
                self.errors_made += 1
                self.ids.label_1.text = "Errors: " + str(self.errors_made)
                button_pressed.background_normal = './data/error.png'

        elif self.current_mode == "subChooser":
            if self.round_number == self.max_rounds:
                self.manager.current = 'result'
            elif int(button_pressed.text) == self.task_values[0] - self.task_values[1]:
                self.round_number += 1
                self.ids.label_3.text = str(self.round_number) + " / " + str(self.max_rounds)
                self.set_next_task()
            else:
                self.errors_made += 1
                self.ids.label_1.text = "Errors: " + str(self.errors_made)
                button_pressed.background_normal = './data/error.png'

        elif self.current_mode == "multiChooser":
            if self.round_number == self.max_rounds:
                self.manager.current = 'result'
            elif int(button_pressed.text) == self.task_values[0] * self.task_values[1]:
                self.round_number += 1
                self.ids.label_3.text = str(self.round_number) + " / " + str(self.max_rounds)
                self.set_next_task()
            else:
                self.errors_made += 1
                self.ids.label_1.text = "Errors: " + str(self.errors_made)
                button_pressed.background_normal = './data/error.png'

        elif self.current_mode == "divChooser":
            if self.round_number == self.max_rounds:
                self.manager.current = 'result'
            elif int(button_pressed.text) == self.task_values[0] / self.task_values[1]:
                self.round_number += 1
                self.ids.label_3.text = str(self.round_number) + " / " + str(self.max_rounds)
                self.set_next_task()
            else:
                self.errors_made += 1
                self.ids.label_1.text = "Errors: " + str(self.errors_made)
                button_pressed.background_normal = './data/error.png'

        elif self.current_mode == "greaterSmallerChooser":
            pass

        elif self.current_mode == "challengeChooser":
            pass


class ResultScreen(Screen):
    def calculate_result(self, screen):
        if screen.errors_made <= 1:
            self.ids.star_3.source = './data/star.png'
            self.ids.star_2.source = './data/star.png'
            self.ids.star_1.source = './data/star.png'
            self.ids.label.text = 'Excellent!\n\n You are a true Master of Mathematics!'
        elif screen.errors_made <= 3:
            self.ids.star_2.source = './data/star.png'
            self.ids.star_1.source = './data/star.png'
            self.ids.label.text = 'Very good!\n\n Close to perfect. Keep up!'
        elif screen.errors_made <= 5:
            self.ids.star_1.source = './data/star.png'
            self.ids.label.text = 'Good!\n\n Train more to become a master of math!'
        else:
            self.ids.label.text = 'Okay...\n\n Try again to get all the stars!'


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
               "More will follow soon!\n"


class AboutScreen(Screen):

    def about_text(self):
        return "Made by: Jonas\n" \
               "Open source and free of charge \n" \
               "\n" \
               "Features:\n" \
               "  - simple\n" \
               "  - rewarding\n" \
               "  - perfect for kids in elementary school\n" \
               "  - or adults who want to train their brain ;)\n" \
               "  - never gets old, new content is generated procedurally\n" \
               "  - written in Python with the help of Kivy"


class ComingSoonScreen(Screen):
    pass


class PopUpQuit(Popup):
    pass


class MathApp(App):

    sm = ScreenManager(transition=FadeTransition())



    def build(self):

        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(StartScreen(name='start'))
        self.sm.add_widget(ProgressScreen(name='progress'))
        self.sm.add_widget(HelpScreen(name='help'))
        self.sm.add_widget(AboutScreen(name='about'))
        self.sm.add_widget(AddChooseDifficulty(name='addChooser'))
        self.sm.add_widget(SubChooseDifficulty(name='subChooser'))
        self.sm.add_widget(MultiChooseDifficulty(name='multiChooser'))
        self.sm.add_widget(DivChooseDifficulty(name='divChooser'))
        self.sm.add_widget(GreaterSmallerChooseDifficulty(name='greaterSmallerChooser'))
        self.sm.add_widget(ChallengeChooseDifficulty(name='challengeChooser'))
        self.sm.add_widget(GameActionScreen(name='game'))
        self.sm.add_widget(ResultScreen(name='result'))
        self.sm.add_widget(ComingSoonScreen(name='comingsoon'))
        #Bind to keyboard to make the back button under android work
        Window.bind(on_keyboard=self.handle_keyboard)

        self.title = 'MathWorldKids'

        return self.sm

    def handle_keyboard(self, window, key, *largs):
        #keycode 273 equals up button, just for test purposes
        if key == 27 or key == 273:
            if self.sm.current_screen.name == 'game':
                popup = PopUpQuit()
                popup.open()
            elif self.sm.current_screen.name == 'menu':
                quit()

            return True

if __name__ == '__main__':
    MathApp().run()